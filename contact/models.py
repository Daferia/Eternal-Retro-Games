from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactUs(models.Model):

    class Meta:
        verbose_name = "Client Message"
        verbose_name_plural = "Client Messages"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    phone_number = PhoneNumberField(blank=True)
    contact_method = models.CharField('Contact', max_length=20)
    enquiry_info = models.CharField('Enquiry Info', max_length=50)
    message = models.TextField(max_length=5000)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email_address
