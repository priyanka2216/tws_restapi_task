from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True

    return False;
# ye filter function use krege cart count ke liye
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)

    return 0;

'''ye filter ka use es liye kiya  hai taki user quantity increase kre toh uska price bhi apne aap multiple ho 
jaye jaise quantity 2 hai toh double ho jaye 3 hai toh jo price hai usse * 3 se multipe krdo'''
@register.filter(name='price_total')
def price_total(product,cart):
    return product.price * cart_quantity(product , cart)

#cart mai sare product ka total niklne ke liye hum ye filter function ka use krege
@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0;
    for p in products:
        sum += price_total(p,cart)
    return sum

