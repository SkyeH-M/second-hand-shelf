from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    quality = None
    if 'book_quality' in request.POST:
        quality = request.POST['book_quality']
    bag = request.session.get('bag', {})

    if quality:
        if item_id in list(bag.keys()):
            if quality in bag[item_id]['items_by_quality'].keys():
                bag[item_id]['items_by_quality'][quality] += quantity
            else:
                bag[item_id]['items_by_quality'][quality] = quantity
        else:
            bag[item_id] = {'items_by_quality': {quality: quantity}}
    else: 
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
