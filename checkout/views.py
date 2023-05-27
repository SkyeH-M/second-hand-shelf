from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is currently empty')
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N7yRFDNZYfoGn9uTTwxhhFPIssmihRgvwg7GUalUjbjjmRpMreT6chmBh52Uw4BKrdkXNV2e3TLe1QAhtbSLJt700atFRELyv'
    }

    return render(request, template, context)
