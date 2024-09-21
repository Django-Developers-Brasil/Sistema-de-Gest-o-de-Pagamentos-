from .views import Home, Logout, clientes_view
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home, name='home'),
    path('logout/', Logout, name='logout'),
    path('clientes/', clientes_view, name='clientes'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)