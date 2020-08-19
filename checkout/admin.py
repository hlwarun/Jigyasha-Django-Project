from django.contrib import admin
from checkout.models import Order, BillingAddress

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['order_id']
    list_filter = ['created_at', 'updated_at', 'status']
    readonly_fields = ['order_id', 'user', 'cart', 'subtotal_price', 'shipping_price', 'tax_price', 'total_price', 'created_at', 'updated_at']
    class Meta:
        model = Order

class BillingAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_added'
    search_fields = ['user', 'first_name', 'last_name']
    list_filter = ['date_added']
    readonly_fields = ['user', 'first_name', 'last_name', 'company_name', 'phone', 'email', 'country', 'province',
                       'district', 'city', 'address_line_01', 'address_line_02', 'zip_code', 'order_notes', 'date_added']
    class Meta:
        model = BillingAddress


admin.site.register(Order, OrderAdmin)
admin.site.register(BillingAddress, BillingAdmin)
