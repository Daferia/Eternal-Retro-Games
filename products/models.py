from django.db import models

class Manufacturer (models.Model):

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    

    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    platform = models.CharField(max_length=35, blank=False, null=False)
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    year_of_release = models.IntegerField(null=True, blank=True,)
    genre = models.CharField(max_length=35, blank=True, null=True)
    publisher = models.CharField(max_length=35, blank=True, null=True)
    user_review = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    developer = models.CharField(max_length=35, blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)   


    def __str__(self):
        return self.name