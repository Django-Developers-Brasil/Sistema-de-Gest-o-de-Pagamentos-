from django.contrib import admin
from .models import Colaboradores

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula', 'telefone_celular')
    search_fields = ('user__first_name', 'user__last_name', 'matricula')

