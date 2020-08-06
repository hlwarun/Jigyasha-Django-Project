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
    return HttpResponseRedirect(reverse('cart:cart'))
