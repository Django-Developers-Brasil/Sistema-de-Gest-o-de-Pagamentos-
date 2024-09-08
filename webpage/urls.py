from django.urls import path
from .views import index, Error

urlpatterns = [
    path('', index,name='index'),
    path('404.html/', Error, name='404'),
]





