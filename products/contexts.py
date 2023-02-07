from .models import Product, Manufacturer


def platform_list(request):

    products = Product.objects.all()
    platform = products.values('platform').distinct()
    temp_list = []
    platforms = []
    for c in platform:
        temp_list.append(c['platform'])
    for g in temp_list:
        platforms.append('%20'.join(g.split(' ')))
    links = dict(zip(temp_list, platforms))
    return {
        'platforms': platforms,
        'links': links,
    }


def manufacturer_list(request):

    manufacturers = Manufacturer.objects.all()
    manufacturers = manufacturers.values('name').distinct()

    return {
        'manufacturers': manufacturers,
    }
