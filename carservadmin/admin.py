from django.contrib import admin
from .models import Colaboradores, Clientes

@admin.register(Colaboradores)
class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula', 'telefone_celular')
    
    search_fields = ('user__first_name', 'user__last_name', 'matricula')

    # Organizando os campos em grupos (fieldsets)
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('user', 'matricula', 'foto')
        }),
        ('Dados de Contato', {
            'fields': ('telefone_fixo', 'telefone_celular')
        }),
        ('Endereço', {
            'fields': ('endereco', 'bairro', 'cidade', 'estado', 'cep')
        }),
    )

     # Tornar o campo 'user' somente leitura no change view
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Isso verifica se estamos no change view, e não no add view
            return ['user']  # Torna o campo 'user' somente leitura
        return []
    

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email', 'telefone_fixo','telefone_celular', 'idade', 'genero')
    
    search_fields = ('nome_completo', 'email')
    
    # Organizando os campos em grupos (fieldsets)
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome_completo', 'data_nascimento', 'genero', 'foto')
        }),
        ('Dados de Contato', {
            'fields': ('email', 'telefone_fixo', 'telefone_celular')
        }),
        ('Endereço', {
            'fields': ('endereco', 'bairro', 'cidade', 'estado', 'cep')
        }),
        ('Observações', {
            'fields': ('obs',)
        }),
    )

   