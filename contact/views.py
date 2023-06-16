from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


def contact_us(request):
    """
    Display Contact Us page and form, then
    sends this form to site manager 
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form['name'],
            # email = form['email'],
            # subject = form['subject'],
            # content = form['content']
            # Below method prints only values whereas above prints whole form
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            content = request.POST.get('content')
            form.save()
            print(name, email, subject, content) # all logging correct info,
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
