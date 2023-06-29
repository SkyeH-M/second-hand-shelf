from django.contrib import admin
from .models import Product, Category, BookReview, Quality


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'category',
        'price',
        # 'rating',
        'image_link',
    )
    # exclude = ('users_wishlist',)

    readonly_fields=('users_wishlist', 'averagerating',)
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BookReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'stars',
        'content',
        'date_added',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Quality)
