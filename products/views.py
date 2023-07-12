from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from .models import Product, Category, BookReview, Quality
from .forms import ProductForm, BookReviewForm


def all_books(request):
    """ A view to display all books, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'direction' in request.GET:
            direction = request.GET['direction']

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'averagerating':
                if direction == 'desc':
                    products = products.order_by(F(
                    'averagerating').desc(nulls_last=True))
                elif direction == 'asc':
                    products = products.order_by(F(
                    'averagerating').asc(nulls_last=True))
            else:
                if sortkey == 'name':
                    sortkey = 'lower_name'
                    products = products.annotate(lower_name=Lower('title'))
                if sortkey == 'category':
                    sortkey = 'category__name'
                if sortkey == 'bookreview':
                    sortkey = 'stars'

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
    is_in_wishlist = False
    selected_quality = None
    if product.users_wishlist.filter(id=request.user.id).exists():
        is_in_wishlist = True

    if request.method == 'POST':
        quality_id = request.POST.get('quality')
        if quality_id:
            selected_quality = get_object_or_404(
                                                 Quality,
                                                 pk=quality_id,
                                                 product=product
            )
    context = {
        'product': product,
        'is_in_wishlist': is_in_wishlist,
        'selected_quality': selected_quality,
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
            messages.success(request, f'Successfully updated book: '
                             f"'{product.title}'")
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
    messages.success(request, f'Book: "{product.title}" \
                     has been successfully deleted.')
    return redirect(reverse('books'))


@login_required
def add_book_review(request, product_id):
    """ A view to add a book review """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST' and request.user.is_authenticated:
        reviews = product.reviews.all()
        if reviews.filter(user=request.user).exists():
            if request.user.is_superuser is False:
                messages.info(request, f"Sorry you've already reviewed "
                              f"{product.title}, you can edit your "
                              f"review by clicking the edit button shown"
                              f" on your review card.")
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
            messages.success(request, f"Thanks for reviewing "
                             f"'{product.title}'")
        return redirect('book_detail', product_id=product_id)

    return render(request)


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
                    review = form.save(commit=False)
                    review.save()
                    messages.success(request, f"You've successfully updated "
                                     f"your review of {product.title}")
                    return redirect(reverse('book_detail', args=[product.id]))
            else:
                form = BookReviewForm(instance=bookreview)
            return render(request, 'products/edit-book-review.html',
                          {'form': form})
        else:
            messages.warning(request, 'Sorry, you can only edit your own reviews')
            return redirect(reverse('book_detail', args=[product.id]))
    else:
        messages.warning(request, 'You must be logged in to edit your reviews')
        return redirect(reverse('account_login'))


@login_required
def delete_book_review(request, bookreview_id):
    """ Give users the ability to delete their own reviews """
    if request.user.is_authenticated:
        # bookreview = BookReview.objects.get(id=bookreview_id)
        bookreview = get_object_or_404(BookReview, pk=bookreview_id)
        product = bookreview.product
        # star_rating = bookreview.stars
        if request.user == bookreview.user:
            bookreview.delete()
            # Update averagerating value
            # review_number = product.reviews.count()
            # if review_number > 0: #1
            #     total_rating = product.reviews.aggregate(total_rating=Sum('stars'))['total_rating']
            #     current_averagerating = total_rating / review_number
            # else:
            #     current_averagerating = None
            # product.averagerating = current_averagerating
            # product.save()
            messages.success(request, 'Your book review was \
                             successfully deleted')
        return redirect(reverse('book_detail', args=[product.id]))
    else:
        messages.warning(request, 'You must be logged in to edit your reviews')
        return redirect(reverse('account_login'))
