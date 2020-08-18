from django.urls import path
from checkout import views

app_name = 'checkout'
urlpatterns = [
    path('', views.checkout, name='checkout'),
]
