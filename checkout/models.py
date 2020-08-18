from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart

# Create your models here.

User = get_user_model()

STATUS = (
    ('Ordered','Ordered'),
    ('Shipped','Shipped'),
    ('Abandoned','Abandoned'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    order_id = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    subtotal_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=12, default='Ordered', choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id
