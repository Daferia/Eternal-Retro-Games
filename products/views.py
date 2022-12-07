from django.shortcuts import render, get_object_or_404
from .models import Product, Manufacturer

def all_products(request):
    '''
    A view for all products including searches
    '''
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''
    A view for show single item details
    '''
    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }

    return render(request, 'products/product_detail.html', context)

