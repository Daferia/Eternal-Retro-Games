from django.shortcuts import redirect, render, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_cart(request):
    '''
    View to return shopping cart page
    '''
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    ''' 
    Add a qty of the individual item to the cart
    '''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect(redirect_url)


def update_cart(request, item_id):
    ''' 
    Update a qty of the individual item in cart page
    '''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} to your shopping cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):

    """ Remove items from the shopping cart """

    try:
        product = get_object_or_404(Product, pk=item_id)

        cart.pop(item_id)
        messages.success(request, f'Removed {product.name} to your bag')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
