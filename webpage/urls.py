from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, Error, contact_view

urlpatterns = [
    path('', index,name='index'),
    path('contact/', contact_view, name='contact'),
    path('404/', Error, name='404'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona a configuração para servir arquivos de mídia durante o desenvolvimento




