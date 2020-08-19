from django.db import models
from django.conf import settings
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

class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    company_name = models.CharField(max_length=75, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    country = models.CharField(max_length=10, default='Nepal')
    province = models.CharField(max_length=10)
    district = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=25)
    address_line_01 = models.CharField(max_length=25)
    address_line_02 = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=10)
    order_notes = models.TextField(blank=True, null=True)
    date_added = date_added = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username
