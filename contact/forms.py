from django import forms
from .models import ContactUs

from crispy_forms.helper import FormHelper


select_contact_method = (
	('email', 'Email'),
	('phone', 'Phone'),
)

class ContactForm(forms.ModelForm):


	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email_address = forms.EmailField(max_length=150)
	contact_method = forms.CharField(required=False, widget=forms.RadioSelect(choices=select_contact_method))
	enquiry_info = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, max_length=2000)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'grey-font product-form-input'

	class Meta:
		model = ContactUs
		fields = '__all__'
	