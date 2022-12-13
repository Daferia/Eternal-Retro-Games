from django import template

register = template.Library() 

# look up create custom tags and filter on django docs


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

