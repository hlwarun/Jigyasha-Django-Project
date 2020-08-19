from django.shortcuts import render
from django.db.models import Q
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

def search(request):
    try:
        q = request.GET.get('search')
    except:
        q = None
    if q:
        prd = Product.objects.all()
        product = prd.filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(category__iexact=q)).order_by('-created_at')
        context = {'q':q, 'filtered_list':product}
    else:
        product = Product.objects.all().order_by('-created_at')
        context = {'filtered_list':product}
    return render(request, 'filter.html', context)
