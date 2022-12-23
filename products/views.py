from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Manufacturer
from .forms import ProductForm


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
            platform = request.GET['platform'].split(',')
            platform_sort = '_'.join(platform)
            platforms = [' '.join(platform_sort.split('_'))]
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
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                developer__icontains=query)
            products = products.filter(queries)

            # if value is not found display this message
            if not products:
                messages.info(request,
                              f'We found zero products called {query}')
                return redirect(reverse('products'))

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        # 'platform_sort': platform_sort,
        'search_term': query,
        'current_sorting': current_sorting,
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


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Succesfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product.\
                            Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ edit a product """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product.\
                           Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
