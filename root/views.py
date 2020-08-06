from django.shortcuts import render
from shop.models import Product
from root.models import Banner

# Create your views here.

def home(request):
    data = Product.objects.all()[:9]
    new = Product.objects.order_by('-created_at')[:9]
    featured = Product.objects.all()[:9]
    offers = Product.objects.all()[:9]
    banner = Banner.objects.all()

    context = {'data':data, 'new':new, 'featured':featured, 'offers':offers, 'banner':banner}

    return render(request, 'index.html', context)
