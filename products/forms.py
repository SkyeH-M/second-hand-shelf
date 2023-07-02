from django import forms
from .models import Product, Category, BookReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('has_quality',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class BookReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        fields = ('content', 'stars',)
