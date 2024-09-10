from django.contrib import admin
from .models import CarServ


class CarServAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # Retorne False para desabilitar a opção de deletar
        return False
    
admin.site.register(CarServ, CarServAdmin)