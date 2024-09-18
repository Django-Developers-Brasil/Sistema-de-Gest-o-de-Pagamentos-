from .views import carservadminTest
from django.urls import path

urlpatterns = [
    path('teste/', carservadminTest),
]