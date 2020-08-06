from django.shortcuts import render
from shop.models import Product
from about.models import Team

# Create your views here.

def product(request):
    data = Product.objects.all()
    new = Product.objects.order_by('-created_at')
    featured = Product.objects.all()
    offers = Product.objects.all()

    team = Team.objects.all()

    context = {'data':data, 'new':new, 'featured':featured, 'offers':offers, 'team':team}

    return render(request, 'product_list.html', context)

def detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product':product}
    return render(request, 'single-product.html', context)
