from django.urls import path
from .views import index, Error, terms_of_service

urlpatterns = [
    path('', index,name='index'),
    path('404/', Error, name='404'),
    path('terms/', terms_of_service, name='terms_of_service'),
]





