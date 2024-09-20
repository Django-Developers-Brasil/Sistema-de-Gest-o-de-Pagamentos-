from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Index, Error, Contact, NewsLetter
from ninja import NinjaAPI
from .api import carserv_router, newsletter_router


# Criando a instância da API
api = NinjaAPI()

# Registrando os routers
api.add_router("/v1/", carserv_router)
api.add_router("/v1/", newsletter_router)


urlpatterns = [
    path('', Index,name='index'),
    path('404/', Error, name='404'),
    path('contact/', Contact, name='contact'),
    path('newsletter/', NewsLetter, name='newsletter'),
    path("api/", api.urls), # http://127.0.0.1:8000/api/v1/webpage/get/all
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adiciona a configuração para servir arquivos de mídia durante o desenvolvimento










