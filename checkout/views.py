import secrets
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from checkout.models import Order, BillingAddress
from checkout.forms import BillingDetailsForm

# Create your views here.

@login_required
def checkout(request):
    try:
       new_id = request.session['cart_id']
       cart = Cart.objects.get(id=new_id)
    except:
        new_id = None
        return HttpResponseRedirect(reverse('cart:cart'))

    new_order, created = Order.objects.get_or_create(cart=cart)

    if created:
        new_order.order_id = secrets.token_hex(15)
        new_order.subtotal_price = cart.subtotal_price
        new_order.shipping_price = cart.shipping_price
        new_order.tax_price = cart.shipping_price
        new_order.total_price = cart.total_price
        new_order.save()

    new_order.user = request.user
    new_order.save()

    billing_form = BillingDetailsForm(request.POST or None)
    if billing_form.is_valid():
        new_billing_details = billing_form.save(commit=False)
        new_billing_details.user = request.user
        new_billing_details.save()

    if new_order.status == 'Delivered'or new_order.status == "Abandoned":
        del request.session['cart_id']
        del request.session['total_products']
        return HttpResponseRedirect(reverse('cart:cart'))

    context = {'form': billing_form}
    return render(request, 'checkout.html', context)
