from django.db import models
from shop.models import Product

# Create your models here.

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Cart ID: {self.id}"
