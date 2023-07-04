from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm


def contact_us(request):
    """
    Display Contact Us page and form, then
    sends this form to site manager
    """
    if request.method == 'POST':
        """ Send user an email to acknowledge their message """
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            content = request.POST.get('content')
            contact = form.save()
            customer_email = email
            email_subject = render_to_string(
                'contact/contact_confirmation_emails/' +
                'contact-email-subject.txt',
                {'contact': contact})
            email_body = render_to_string(
                'contact/contact_confirmation_emails/contact-email-body.txt',
                {'contact': contact,
                    'contact_email': settings.DEFAULT_FROM_EMAIL})

            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [customer_email]
            )
            messages.success(request, 'Thank you for sending us a message \
            we aim to respond within 48 hours')
            return redirect(reverse('home'))
        else:
            messages.error(request, "Your message couldn't be sent, please \
            check all information in the form is provided, and correct then \
            try again. Thank you")
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
