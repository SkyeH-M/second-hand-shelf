from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import get_object_or_404
from decimal import Decimal

from .models import Order, OrderLineItem
from .views import checkout
from products.models import Product, Quality
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """ Send a confirmation email to user """
        customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def checkout_quality(request):
        if request.method == "POST":
            if 'book_quality' in request.POST:
                quality = request.POST['book_quality']
                bag = request.session.get('bag', {})
                text_quality = None
                if quality == '0.60':
                    text_quality = 'Fair'
                elif quality == '0.80':
                    text_quality = 'Good'
                else:
                    text_quality = 'Great'
            for item_id, item_data in json.loads(bag).items():
                product = Product.objects.get(id=item_id)
                for quality, quantity in item_data['items_by_quality'].items():
                    quality_instance = None
                    if Quality.objects.filter(product=product, name=text_quality).exists():
                        quality_instance = Quality.objects.get(product=product, price_factor=Decimal(quality))
                    else:
                        quality_instance = Quality.objects.create(product=product, price_factor=Decimal(quality))
                        print(f"QUALITY INSTANCE{quality_instance}")
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                        book_quality=quality_instance,
                    )
                    order_line_item.save()

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f"Unhandled webhook received: {event['type']}",
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )
        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = (
                    shipping_details.address.line1
                )
                profile.default_street_address2 = (
                    shipping_details.address.line2
                )
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f"Webhook received: {event['type']} | "
                        f"SUCCESS: Verified order already in database",
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                self.checkout_quality(request=self.request, bag=bag, order=order)

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | ERROR: {e}",
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f"Webhook received: {event['type']}\
             | SUCCESS: Created order in webhook",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200)
