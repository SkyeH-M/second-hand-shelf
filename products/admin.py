from django.contrib import admin
from .models import Product, Category, BookReview, Quality
# removed Quality, QualityVariants from imports 


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'category',
        'price',
        # 'rating',
        'image_link',
    )

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
# class QualityAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'code',
#     )


# class QualityVariantsAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'product',
#         'quality',
#         'price',
#     )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(BookReview, BookReviewAdmin)
admin.site.register(Quality)
# admin.site.register(QualityVariants, QualityVariantsAdmin)
