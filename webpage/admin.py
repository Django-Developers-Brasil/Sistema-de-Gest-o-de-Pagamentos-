from django.contrib import admin
from .models import CarServ, Newsletter
from django.utils.html import format_html
import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta.model_name)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar Selecionados"

# Admin Customizado para CarServ
@admin.register(CarServ)
class CarServAdmin(admin.ModelAdmin, ExportCsvMixin):
    # Exibição dos campos na listagem
    list_display = ['company_name', 'email', 'phone', 'webpage_link', 'api_icon']

    # Campos de busca
    search_fields = ['company_name', 'email', 'phone']

    # Fieldsets para organizar os campos
    fieldsets = (
        ('Informações da Empresa', {
            'fields': ('company_name', 'endereco', 'email', 'phone', 'logo')
        }),
        ('Horários de Funcionamento', {
            'fields': ('working_hours_weekdays', 'working_hours_saturday')
        }),
        ('Redes Sociais', {
            'fields': ('twitter', 'facebook', 'linkedin', 'youtube', 'instagram')
        }),
        ('Links', {
            'fields': ('terms_of_service', 'privacy_policy')
        }),
        ('Visibilidade das Seções', {
            'fields': (
                'show_navbar', 'show_carousel', 'show_carousel_cars', 
                'show_services', 'show_about_us', 'show_our_numbers', 
                'show_book', 'show_our_technicians', 'show_testimonials', 
                'show_footer'
            )
        }),
        ('Imagens da Landing Page', {
            'fields': (
                'icon', 'img_carrousel1', 'img_carrousel2', 
                'img_about', 'img_numbers', 'img_book', 'img_footer'
            )
        }),
        ('Esquema de Cores', {
            'fields': (
                'color_primary', 'color_secondary', 'color_success', 
                'color_danger', 'color_warning', 'color_info', 
                'color_light', 'color_dark'
            )
        }),
    )

    # Ações personalizadas
    actions = ["export_as_csv"]

    # Função para exibir o link da página web no admin
    def webpage_link(self, obj):
        return format_html(
            '<a href="https://carserv.django.dev.br" target="_blank" title="Ir para o site"><img src="/static/webpage/img/url_icon.svg" alt="Webpage"></a>'
        )
    webpage_link.short_description = 'Home Page'

    

     # Função para exibir o link da página web no admin
    def api_icon(self, obj):
        return format_html(
            '<a href="/api/v1/webpage/get/all" target="_blank" title="Ver dados na API"><img src="/static/webpage/img/api_icon.svg" alt="Webpage"></a>'
        )
    api_icon.short_description = 'API'

    # Desabilitar a permissão de mudança para não superadmins
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False  # Usuários não superadmins não podem modificar os registros
        return super().has_change_permission(request, obj)

    # Desabilitar a permissão de adicionar e deletar registros
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

# Admin para Newsletter
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['email', 'created_at','api_icon']
    search_fields = ['email']

    actions = ["export_as_csv"]

   # Função para exibir o ícone da API no admin
    def api_icon(self, obj):
        return format_html(
            '<a href="/api/v1/newsletter/getByid/{}" target="_blank" title="Ver dados na API"><img src="/static/webpage/img/api_icon.svg" alt="API"></a>'.format(obj.id)
        )
    api_icon.short_description = 'api_newsletter_all'

    # Desabilitar a permissão de mudança para não superadmins
    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False  # Usuários não superadmins não podem modificar os registros
        return super().has_change_permission(request, obj)

    # Desabilitar a permissão de adicionar e deletar registros
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
