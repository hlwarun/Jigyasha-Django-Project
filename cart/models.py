from django.db import models
from shop.models import Product

# Create your models here.
class CartItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    # We closed the Cart in Inverted Comma because Cart represents the class that is not yet defined.
    quantity = models.IntegerField(default=1)
    size = models.IntegerField(default=39)
    single_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.cart.id)

class Cart(models.Model):
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"Cart ID: {self.id}"
