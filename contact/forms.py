from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import ContactUs


select_contact_method = (
    ('email', 'Email'),
    ('phone', 'Phone'),
)


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'

    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('Please enter your country code\
                               if outside the UK...')}), label=(
        "Phone number"), required=False)
    contact_method = forms.CharField(required=False,
                                     widget=forms.RadioSelect
                                     (choices=select_contact_method))
    enquiry_info = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'grey-font product-form-input'
