from django.contrib import admin
from root import models

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    # Should return True if adding an object is permitted, False otherwise.
    def has_add_permission(self, request):
        return False

    # Should return True if editing obj is permitted, False otherwise.
    def has_change_permission(self, request, obj=None):
        return True

    # Should return True if deleting obj is permitted, False otherwise.
    def has_delete_permission(self, request, obj=None):
        return False

    class Meta:
        model = models.Banner

admin.site.register(models.Banner, BannerAdmin)
