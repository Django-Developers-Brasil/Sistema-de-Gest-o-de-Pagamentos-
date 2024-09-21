from .views import Home, Logout
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home, name='home'),
    path('logout/', Logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)