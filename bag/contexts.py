from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from checkout.models import OrderLineItem

def bag_contents(request):

    bag_items = []
    total = 0
    item_price = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'quality': quality,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            # item_prices = {}
            for quality, quantity in item_data['items_by_quality'].items():
                total += quantity * product.price * Decimal(quality)
                item_price = product.price * Decimal(quality)
                # item_prices[quality] = item_price
                product_count += quantity
                text_quality = None
                if quality == '0.60':
                    text_quality = 'Fair'
                elif quality == '0.80':
                    text_quality = 'Good'
                else:
                    text_quality = 'Great'
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'quality': quality,
                    'text_quality': text_quality,
                    'amended_price': quantity * product.price * Decimal(quality),
                    # item_price shows individually calculated price per product
                    'item_price': item_price
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
        # free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - (total + delivery)
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total 

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_price': item_price,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
