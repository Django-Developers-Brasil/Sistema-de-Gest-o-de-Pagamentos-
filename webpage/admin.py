from django.contrib import admin
from .models import CarServ, Newsletter
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


@admin.register(CarServ)
class CarServAdmin(admin.ModelAdmin, ExportCsvMixin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    actions = ["export_as_csv"]

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin, ExportCsvMixin):
    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    actions = ["export_as_csv"]
