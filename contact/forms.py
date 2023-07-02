from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for the contact form for users to submit
    queries or comments
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': 'Add your message here'}))

    class Meta:
        model = Contact
        exclude = ('date-submitted',)
