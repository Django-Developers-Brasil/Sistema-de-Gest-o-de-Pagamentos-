from django.shortcuts import render
from .models import CarServ


def Error(request):
    # Busca o único registro do modelo CarServ
    carserv = CarServ.objects.first()

    return render(request,'404.html', {'carserv': carserv})

def index(request):
    # Busca o único registro do modelo CarServ
    carserv = CarServ.objects.first()

    # Passa os dados para o template
    return render(request, 'index.html', {'carserv': carserv})  

"""
Django Sehll Interaction Example

Digite no terminal:

>>> python manage.py shell
>>> from webpage.models import CarServ
>>> carserv = CarServ.objects.first()
>>> print(carserv.__dict__)

"""