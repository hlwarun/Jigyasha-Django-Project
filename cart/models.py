from django.db import models
from shop.models import Product

# Create your models here.
class CartItem(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        self.product.title

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    items = models.ManyToManyField(CartItem, blank=True)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Cart ID: {self.id}"
