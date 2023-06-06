from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
# removed Quality, QualityVariant from imports
from .forms import ProductForm

def all_books(request):
    """ A view to display all books, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('title')) 
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('books'))
            
            queries = Q(title__icontains=query) | Q(blurb__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/books.html', context)


def book_detail(request, product_id):
    """ A view to display individual book details """

    product = get_object_or_404(Product, pk=product_id)
    discounted_price = Product.discounted_price
    # quality = get_object_or_404(Quality)
    # if product.variant == 'Fair':
    #     product.price = int(product.price * 0.6)
    # elif product.variant == 'Good':
    #     product.price = int(product.price * 0.8)
    # else:
    #     product.price = product.price
    
    context = {
        'product': product,
        'discounted_price': discounted_price,
        # 'quality': quality,
    }
    
    return render(request, 'products/book-detail.html', context)

def add_book(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added book')
            return redirect(reverse('book_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
            Please ensure all information is correct')
    else:
        form = ProductForm()
    template = 'products/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_book(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated book: "{product.title}"')
            return redirect(reverse('book_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please \
            ensure all information is correct.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing book: "{product.title}"')

    template = 'products/edit_book.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

def delete_book(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Book: "{product.title}" has been successfully deleted.')
    return redirect(reverse('books'))
