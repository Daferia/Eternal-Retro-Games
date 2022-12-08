from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Manufacturer

def all_products(request):
    '''
    A view for all products including searches
    '''
    products = Product.objects.all()

    if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        summary__icontains=query)
            products = products.filter(queries)


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

