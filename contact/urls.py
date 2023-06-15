from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    # path('', views.contact_us, name='contact_us'), success page
]