from django.contrib import admin
from shop import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = ['title', 'description']
    list_display = ['title', 'new_price', 'available']
    list_editable = ['new_price', 'available']
    list_filter = ['new_price', 'available']
    readonly_fields = ['created_at', 'slug', 'rating', 'ratings_quantity']
    class Meta:
        model = models.Product

admin.site.register(models.Product, ProductAdmin)
