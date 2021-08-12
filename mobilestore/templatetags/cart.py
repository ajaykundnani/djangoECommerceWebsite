
from django import template

register = template.Library()


@register.filter(name='cartqty')
def cartqty(product,cart):
    
    keys = cart.keys()
    
    for id in keys:
        if int(id) == product.id:
           # print(cart.get(id))
            q = cart.get(id)
            q = int(q)
            
            return q
    return 0;


@register.filter(name='prtotal')
def prtotal(product,cart): 
    return product.p_price * cartqty(product , cart);

@register.filter(name='totalP')
def totalP(product , cart):
    sum = 0;
    for p in product:
        sum += prtotal(p , cart)

    return sum
