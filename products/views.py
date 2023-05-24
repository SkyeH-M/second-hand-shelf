from django.shortcuts import render, get_object_or_404
from .models import Product


def all_books(request):
    """ A view to display all books, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/books.html', context)


def book_detail(request, product_id):
    """ A view to display individual book details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/book-detail.html', context)
