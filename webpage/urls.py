from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, Error, Contact,newsLetter

urlpatterns = [
    path('', index,name='index'),
    path('404/', Error, name='404'),
    path('contact/', Contact, name='contact'),
    path('newsletter/', newsLetter, name='newsletter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona a configuração para servir arquivos de mídia durante o desenvolvimento




