from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Manufacturer

def all_products(request):
    '''
    A view for all products including searches
    '''
  
    products = Product.objects.all()
    platform_list = None
    query = None
    manufacturers = products.values('manufacturer__name').distinct()
    platforms = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'platform' in request.GET:
            platforms = request.GET['platform'].split(',')
            products = products.filter(platform__in=platforms)

        if 'manufacturer' in request.GET:
            manufacturers = request.GET['manufacturer'].split(',')
            products = products.filter(manufacturer__name__in=manufacturers)
            manufacturers = Manufacturer.objects.filter(name__in=manufacturers)
            platform_list = products.values('platform').distinct()

        if 'q' in request.GET:
            query = request.GET['q']

            # if not data is enter into searchbar
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                        developer__icontains=query)
            products = products.filter(queries)

            # if value is not found display this message
            if not products:
                messages.info(request, f'We found zero products called {query}')
                return redirect(reverse('products'))

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting':current_sorting,
        'search_manufacturers': manufacturers,
        'search_platform': platform_list,

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

