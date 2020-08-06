from django.shortcuts import render
from about.models import Team

# Create your views here.

def about(request):
    data = Team.objects.all()
    context = {'data':data}
    return render(request, 'about.html', context)
