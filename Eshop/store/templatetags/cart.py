from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    print(product, cart)
    keys = cart.keys()
    for id in keys:
        if id == 'null':
            return False
        else:
            if int(id) == product.id:
                return True
    return False

@register.filter(name='product_quantity')
def product_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == 'null':
            return False
        else:
            if int(id) == product.id:
                return cart.get(id)
    return False

@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if id == 'null':
            return False
        else:
            if int(id) == product.id:
                return cart.get(id)
    return False

@register.filter(name='product_total')
def product_total(product, cart):
   return product.price * cart_quantity(product, cart)

@register.filter(name='total_amount')
def total_amount(product, cart):
    sum = 0
    for p in product:
        sum += product_total(p, cart)

    return sum

@register.filter(name='total')
def total(order):
    total = order.quantity * order.price

    return total
