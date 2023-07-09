from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from decimal import Decimal

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product, Quality
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from bag.contexts import bag_contents
from .contexts import checkout_bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
        processed currently, please check your details and try again')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    quality = None

    if request.method == "POST":
        if 'book_quality' in request.POST:
            quality = request.POST['book_quality']
        bag = request.session.get('bag', {})
        print(f'BAG: {bag}')
        text_quality = None
        if quality == '0.60':
            text_quality = 'Fair'
        elif quality == '0.80':
            text_quality = 'Good'
        else:
            text_quality = 'Great'

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            current_bag = checkout_bag_contents(request)
            order.delivery = current_bag['delivery']
            order.grand_total = current_bag['grand_total']
            order.save()
            for item_id, item_data in bag.items():
                try:
                    # product = Product.objects.get(id=item_id)
                    # if isinstance(item_data, int):
                    #     order_line_item = OrderLineItem(
                    #         order=order,
                    #         product=product,
                    #         quantity=item_data,
                    #     )
                    #     order_line_item.save()
                    # else:
                        for quality, quantity in item_data['items_by_quality'].items():
                            quality_instance = None
                            product = get_object_or_404(Product, pk=item_id)
                            if Quality.objects.filter(product=product, name=text_quality).exists():
                                # CHECK BELOW LINE AS IT BROKE BUT ADDITION SEEMS TO WORK
                                # quality_instance = Quality.objects.filter(product=product, price_factor=Decimal(quality))[0]
                                quality_instance = Quality.objects.get(product=product, price_factor=Decimal(quality))
                                print(f'Quality instance: {quality_instance}')
                                print(f'Quality instance type: {type(quality_instance)}')
                            else:
                                quality_instance = Quality.objects.create(product=product, price_factor=Decimal(quality))
                            order_line_item = OrderLineItem(
                                order=order, 
                                product=product,
                                quantity=quantity,
                                book_quality=quality_instance,
                            )
                            order_line_item.save()
                            print(f"orderlineitem: {order_line_item}")
                            print(f"type of orderlineitem: {type(order_line_item)}")
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
            Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'Your bag is currently empty')
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, "Stripe public key is missing")

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:

        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
