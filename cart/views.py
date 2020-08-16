from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from shop.models import Product
from cart.models import Cart, CartItem

# Create your views here.

def carts(request):
    try:
        new_id = request.session['cart_id']
    except:
        new_id = None
    if new_id:
        carts = Cart.objects.get(id=new_id)
        context = {'cart':carts}
    else:
        # You may pass a message "Your Cart is Empty!" as context if you want
        context = {}
    return render(request, 'cart.html', context)

def update_cart(request, slug):
    request.session.set_expiry(123456)
    # Check if a cart already exists
    try:
        # If the cart already exists, grab that cart
        new_id = request.session['cart_id']
    except:
        # If there is no cart, create a new cart
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        new_id = new_cart.id

    carts = Cart.objects.get(id=new_id)
    try:
        product = Product.objects.get(slug=slug)
    except:
        pass

    cart_item, created = CartItem.objects.get_or_create(product=product)

    if created:
        print("Hello there")

    if not cart_item in carts.items.all():
        carts.items.add(cart_item)
    else:
        carts.items.remove(cart_item)

    sub_total = 0.00
    total = 0.00
    tax = 0.13
    shipping = 100 # Per item
    for item in carts.items.all():
        each_total = float(item.product.new_price) * item.quantity
        sub_total += each_total
        total += (float(item.new_price))*(1 + tax) + shipping
    request.session['total_products'] = carts.items.count()
    carts.subtotal_price = sub_total
    carts.total_price = total
    carts.save()
    return HttpResponseRedirect(reverse('cart:cart'))
