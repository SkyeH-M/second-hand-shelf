from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category, BookReview
# removed Quality, QualityVariant from imports
from .forms import ProductForm, BookReviewForm
from profiles.forms import UserProfile

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
            if sortkey == 'bookreview':
                sortkey == 'stars'
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
    print('current_sorting: ', current_sorting)

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
    is_in_wishlist = False
    if product.users_wishlist.filter(id=request.user.id).exists():
        is_in_wishlist = True
    # discounted_price = Product.discounted_price
    # print('PRODUCT averagerating: ', product.averagerating)
    # print('PRODUCT get_rating: ', product.get_rating())
    
    context = {
        'product': product,
        'is_in_wishlist': is_in_wishlist,
        # 'discounted_price': discounted_price,
    }
    template = 'products/book-detail.html'
    
    return render(request, template, context)

@login_required
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

@login_required
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

@login_required
def delete_book(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Book: "{product.title}" has been successfully deleted.')
    return redirect(reverse('books'))


@login_required
def add_book_review(request, product_id):
    """ A view to add a book review """
    product = get_object_or_404(Product, pk=product_id)
    # Add Review
    if request.method == 'POST' and request.user.is_authenticated:
        reviews = product.reviews.all()
        if reviews.filter(user=request.user).exists() and request.user.is_superuser == False:
            messages.info(request, f"Sorry you've already reviewed {product.title}, you can edit your review by clicking the edit button shown on your review card.")
            return redirect(reverse('book_detail', args=[product.id]))
        else:
            stars = request.POST.get('stars', 3)
            content = request.POST.get('content', '')
            review = BookReview.objects.create(
                product=product, user=request.user, stars=stars,
                content=content)
            review.save()
        # below averagerating code suggested by Joshua from tutor support
            product.averagerating = product.get_rating()
            product.save()
            messages.success(request, f"Thanks for reviewing '{product.title}'")
        return redirect('book_detail', product_id=product_id)

    # product = get_object_or_404(Product, pk=product_id)
    # if request.user.is_authenticated:
    #     profile = get_object_or_404(UserProfile, user_id=request.user)
    # else:
    #     profile = None
    # if request.user.is_authenticated:
    #     if request.method == 'POST':
    #         book_form = BookReviewForm(request.POST)
    #         reviews = product.reviews.all()
    #         if reviews.filter(user=request.user).exists():
    #             message.info(request, f"You've already reviewed {product.title}, sorry!")
    #         return redirect(reverse('book_detail', args=[product.id]))

    #         if book_form.is_valid():
    #             book_form.save()
    #             messages.success(request, f"Your review for '{product.title} has been successfully added'")
    #         else:
    #             messages.error(request, f"Sorry, your review couldn't be saved. Please check all form fields are valid")
    #         return redirect(reverse('book_detail', args=[product.id]))
    # book_form = BookReviewForm()
    # product = get_object_or_404(Product, pk=product_id)
    # context = {
    #     'book_form': book_form,
    #     'profile': profile,
    # }
    # template = 'products/book-detail.html'
    return render(request, context)

@login_required
def edit_book_review(request, bookreview_id):
    """ Give users the ability to edit their own reviews """
    if request.user.is_authenticated:
        bookreview = BookReview.objects.get(id=bookreview_id)
        product = bookreview.product
        if request.user == bookreview.user:
            if request.method == 'POST':
                form = BookReviewForm(request.POST, instance=bookreview)
                if form.is_valid():
                    review = form.save(commit=False) #changed review from data
                    review.save() # same as above
                    messages.success(request, f"You've successfully updated your review of {product.title}")
                    return redirect(reverse('book_detail', args=[product.id]))
            else:
                form = BookReviewForm(instance=bookreview)
            return render(request, 'products/edit-book-review.html', {'form': form})
        else:
            messages.warning('Sorry, you can only edit your own reviews')
            return redirect(reverse('book_detail', args=[product.id]))
    else:
        messages.warning('You must be logged in to edit your reviews')
        return redirect(reverse('account_login'))

@login_required
def delete_book_review(request, bookreview_id):
    """ Give users the ability to delete their own reviews """
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        bookreview = BookReview.objects.get(id=bookreview_id)
        product = bookreview.product
        if request.user == bookreview.user:
            bookreview.delete()
            messages.success(request, 'Your book review was successfully deleted')
        return redirect(reverse('book_detail', args=[product.id]))
    else:
        messages.warning('You must be logged in to edit your reviews')
        return redirect(reverse('account_login'))