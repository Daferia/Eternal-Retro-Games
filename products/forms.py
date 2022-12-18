from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Manufacturer


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        manufacturers = Manufacturer.objects.all()
        firendly_names = [(c.id, c.get_friendly_name()) for c in manufacturers]

        self.fields['manufacturer'].choices = firendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'grey-font product-form-input'
