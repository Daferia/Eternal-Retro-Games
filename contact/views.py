from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings


def contact(request):
    ''' Form to contact Store '''

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            enquiry_info = form.cleaned_data['enquiry_info']
            subject = f'Enquiry Message: {enquiry_info}'
            message = 'Thank you for your message. One of our staff will get back to you shortly.'
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email_address']
            client_message = form.cleaned_data['message']

            messages.success(request,
                            'Thank you for your message.\
                            Message has been sent to the Admin.')
            try:
                send_mail(
					subject,
					message,
					client_message,
					[email_from, email]
					)

                # send_mass_mail(subject, message, client_message,
                #         email_from, [email, email_from])
                
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
