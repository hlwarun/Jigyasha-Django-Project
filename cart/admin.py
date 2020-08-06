from django.contrib import admin
from cart.models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['updated_at', 'created_at', 'id']
    list_filter = ['created_at', 'updated_at']
    # readonly_fields = ['products', 'total_price', 'created_at', 'updated_at']
    class Meta:
        model = Cart

admin.site.register(Cart)
