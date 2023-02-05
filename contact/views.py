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
            client_email = form.cleaned_data['email_address']
            client_message = form.cleaned_data['message']

            messages.success(request,
                            'Thank you for your message.\
                            Message has been sent to the Admin.')
            try:
                   email_messages = (
                                (subject, message, email_from, [client_email]),
                                (subject, client_message, email_from, [email_from]),
                )
                   send_mass_mail(email_messages)
                # # Email to client
                # send_mail(
                # 	subject,
                # 	message,
                # 	email
                # 	)

                # # Email to admin email with client message
                # send_mail(
                # 	subject,
                # 	client_message,
                # 	email_from
                # 	)
            
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
