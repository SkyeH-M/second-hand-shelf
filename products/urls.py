from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:product_id>', views.book_detail, name='book_detail'),
]
