from django.shortcuts import render
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
]
