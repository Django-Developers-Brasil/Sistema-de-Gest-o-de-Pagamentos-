from django.contrib import admin
from django.http import HttpRequest
from .models import CarServ

class CarServAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
    
    
admin.site.register(CarServ, CarServAdmin)