from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    quality = None

    if 'book_quality' in request.POST:
        quality = request.POST['book_quality']

    text_quality = None
    if quality == '0.60':
        text_quality = 'Fair'
    elif quality == '0.80':
        text_quality = 'Good'
    else:
        text_quality = 'Great'

    bag = request.session.get('bag', {})

    if quality:
        if item_id in list(bag.keys()):
            if quality in bag[item_id]['items_by_quality'].keys():
                bag[item_id]['items_by_quality'][quality] += quantity
                messages.success(request,
                                 f"Updated quality '{text_quality}' "
                                 f"{product.title} quantity to "
                                 f"{bag[item_id]['items_by_quality'][quality]}") 
            else:
                bag[item_id]['items_by_quality'][quality] = quantity
                messages.success(request, f"Added quality '{text_quality}' "
                                 f"{product.title} to your bag")
        else:
            bag[item_id] = {'items_by_quality': {quality: quantity}}
            messages.success(request, f"Added quality '{text_quality}' "
                             f"{product.title} to your bag")
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f"Updated {product.title}"
                             f"quantity to {bag[item_id]}")
        else:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.title} to your bag")

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    quality = None
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

    if quality:
        if quantity > 0:
            bag[item_id]['items_by_quality'][quality] = quantity
            messages.success(request, f"Updated quality '{text_quality}' "
                             f"{product.title} quantity to "
                             f"{bag[item_id]['items_by_quality'][quality]}")
        else:
            del bag[item_id]['items_by_quality'][quality]
            if not bag[item_id]['items_by_quality']:
                bag.pop(item_id)
                messages.success(request, f"Removed quality '{text_quality}' "
                                 f"{product.title} from your bag")
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f"Added {product.title} to your bag")

        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.title} from your bag")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        quality = None
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

        if quality:
            del bag[item_id]['items_by_quality'][quality]
            if not bag[item_id]['items_by_quality']:
                bag.pop(item_id)
                messages.success(request, f"Removed quality '{text_quality}' "
                                 f"{product.title} from your bag")
        else:
            bag.pop(item_id)
            messages.success(request, f"Removed {product.title} from your bag")

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
