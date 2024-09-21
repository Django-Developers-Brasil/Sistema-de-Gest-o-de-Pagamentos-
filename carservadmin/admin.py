from django.contrib import admin
from .models import Colaboradores, Clientes

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula', 'telefone_celular')
    search_fields = ('user__first_name', 'user__last_name', 'matricula')

from django.contrib import admin
from .models import Clientes

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone_fixo','telefone_celular', 'idade', 'genero')
    search_fields = ('nome_completo', 'email')

    # Campos editáveis no admin
    fields = ('nome_completo', 'email', 'telefone_fixo', 'telefone_celular', 'endereco', 'data_nascimento', 'genero', 'obs')
