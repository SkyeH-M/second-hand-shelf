from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<int:product_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:product_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:product_id>/', views.delete_book, name='delete_book'),
]
