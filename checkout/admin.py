from django.contrib import admin
from checkout.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['order_id']
    list_filter = ['created_at', 'updated_at', 'status']
    readonly_fields = ['order_id', 'cart', 'user', 'subtotal_price', 'shipping_price', 'tax_price', 'total_price', 'created_at', 'updated_at']
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)
