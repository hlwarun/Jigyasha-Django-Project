from django.contrib import admin
from cart.models import Cart, CartItem

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['updated_at', 'created_at', 'id']
    list_filter = ['created_at', 'updated_at']
    readonly_fields = ['subtotal_price', 'tax_price', 'shipping_price' , 'total_price', 'created_at', 'updated_at']
    class Meta:
        model = Cart

class CartItemAdmin(admin.ModelAdmin):
    date_hierarchy: 'added_at'
    search_fields = ['added_at', 'product.title', 'id']
    list_filter = ['added_at']
    readonly_fields = ['product', 'cart', 'quantity', 'size', 'single_total', 'added_at']
    class Meta:
        model = CartItem

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
