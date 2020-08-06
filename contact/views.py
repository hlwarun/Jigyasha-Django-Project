from django.shortcuts import render
from contact.models import ContactU

# Create your views here.

def contact(request):
    address = ContactU.objects.all()
    context = {'address':address}
    
    return render(request, 'contact.html', context)
