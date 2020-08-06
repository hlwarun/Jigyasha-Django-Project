from django.urls import path
from cart import views

app_name = 'cart'
urlpatterns = [
    path('', views.carts, name='cart'),
    path('<str:slug>/', views.update_cart, name='update_cart'),
]
