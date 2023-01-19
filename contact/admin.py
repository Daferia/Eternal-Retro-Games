from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email_address',
		'date',
	]

admin.site.register(ContactUs, ContactUsAdmin)