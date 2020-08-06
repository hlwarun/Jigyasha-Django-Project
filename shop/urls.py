from django.urls import path
from shop import views

app_name = 'shop'
urlpatterns = [
    path('', views.product, name='product'),
    path('<str:slug>/', views.detail, name='detail'),
]
