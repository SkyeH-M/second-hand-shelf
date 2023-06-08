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

# QUALITY_VARIANTS = (
#     ('Fair', 'Fair'),
#     ('Good', 'Good'),
#     ('Great', 'Great'),
# )

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
    # Yuksel Celik
    # variant = models.CharField(max_length=10, choices=QUALITY_VARIANTS, default='Great')
    # rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_link = models.ImageField(null=True, blank=True)
    # Very Academy
    users_wishlist = models.ManyToManyField(User, related_name="user_wishlist", blank=True)
    # Rating and Review

    # def __str__(self):
    #     return self.title
    # # Book Quality 
    # QUALITY_VARIANTS = (
    #     ('fair', 'Fair'),
    #     ('good', 'Good'),
    #     ('great', 'Great'),
    # )
    # quality = models.CharField(max_length=10, choices=QUALITY_VARIANTS, default='Great')

    # @property
    # def discounted_price(self):
    #     if self.quality == 'fair':
    #         return self.price * 0.6
    #     elif self.quality == 'good':
    #         return self.price * 0.8
    #     else:
    #         return self.price

# class Quality(models.Model):
#     """ Model to map relationship between quality of book and its price """
#     class Meta:
#         verbose_name_plural = 'Qualities'

#     name = models.CharField(max_length=20)
#     code = models.CharField(max_length=10, blank=True, null=True)

#     def __str__(self):
#         return self.name


# class QualityVariants(models.Model):
#     class Meta:
#         verbose_name_plural = 'Variants'

#     title = models.CharField(max_length=30)
#     price = models.DecimalField(decimal_places=2, max_digits=6)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quality = models.ForeignKey(Quality, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


class BookReview(models.Model):
    """
    A model for users to rate and reviews books, and for users
    to see ratings and reviews from all other users 
    """
    product = models.ForeignKey(Product, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(Product, related_name="user_reviews", on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
