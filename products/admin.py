from django.contrib import admin
from .models import Product, Manufacturer

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'manufacturer',
        'selling_price',
        'image',
    )

    ordering = ('name',)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)