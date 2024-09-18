from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, Error, Contact, NewsLetter

urlpatterns = [
    path('', Index,name='index'),
    path('404/', Error, name='404'),
    path('contact/', Contact, name='contact'),
    path('newsletter/', NewsLetter, name='newsletter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona a configuração para servir arquivos de mídia durante o desenvolvimento




