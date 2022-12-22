from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from profiles.models import UserProfile


def contact(request):
    ''' Form to contact Store '''

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],

            }
            email_confirmation = body.get('email')
            message = "\n".join(body.values())
            messages.success(request,
                             'Thank you for your message.\
                             Message has been sent to the Admin.')
            try:
                send_mail(subject, message,
                          'daferia@gmail.com', ['daferia@gmail.com'])
                send_mail(subject,
                          message, email_confirmation, [email_confirmation])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect(reverse('home'))
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
