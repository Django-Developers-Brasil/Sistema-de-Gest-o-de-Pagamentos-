from .views import Home
from django.urls import path

urlpatterns = [
    path('', Home, name='home'),
]