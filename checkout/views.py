from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is currently empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N7yRFDNZYfoGn9uTTwxhhFPIssmihRgvwg7GUalUjbjjmRpMreT6chmBh52Uw4BKrdkXNV2e3TLe1QAhtbSLJt700atFRELyv'
    }

    return render(request, template, context)
