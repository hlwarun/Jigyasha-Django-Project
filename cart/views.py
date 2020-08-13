from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from shop.models import Product
from cart.models import Cart

# Create your views here.

def carts(request):
    carts = Cart.objects.all()[0]
    context = {'cart':carts}
    return render(request, 'cart.html', context)

def update_cart(request, slug):
    carts = Cart.objects.all()[0]
    try:
        product = Product.objects.get(slug=slug)
    except:
        raise
    if not product in carts.products.all():
        carts.products.add(product)
    else:
        carts.products.remove(product)

    sub_total = 0.00
    total = 0.00
    tax = 0.13
    shipping = 100 # Per item
    for item in carts.products.all():
        sub_total += float(item.new_price)
        total += (float(item.new_price))*(1 + tax) + shipping
    carts.subtotal_price = sub_total
    carts.total_price = total
    carts.save()
    return HttpResponseRedirect(reverse('cart:cart'))
