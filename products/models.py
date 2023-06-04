from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    language = models.CharField(max_length=254)
    pages = models.IntegerField()
    release_year = models.IntegerField()
    blurb = models.TextField()
    has_quality = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_link = models.ImageField(null=True, blank=True)
    # Very Academy
    users_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)

    def __str__(self):
        return self.title


# class Discounts(models.Model):
#     name = models.CharField(max_length=40)
#     value = models.IntegerField()

#     price = 

#     def twenty()
#         return 
