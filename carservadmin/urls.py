from .views import Home, Logout, clientes_view, cliente_detail, Cliente_delete
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home, name='home'),
    path('logout/', Logout, name='logout'),
    path('clientes/', clientes_view, name='clientes'),
    path('cliente/<int:id>/', cliente_detail, name='cliente_detail'),
    path('cliente/delete/<int:cliente_id>/', Cliente_delete, name='cliente_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)