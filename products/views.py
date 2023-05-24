from django.shortcuts import render
from .models import Product


def all_books(request):
    """ A view to display all books, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)
