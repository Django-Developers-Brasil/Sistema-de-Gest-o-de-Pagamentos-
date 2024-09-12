from django.shortcuts import render
from .utils import get_carserv_data

def Error(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404

    return render(request, '404.html', {'carserv': carserv})

def index(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404

    # Passa os dados para o template 'index.html'
    return render(request, 'index.html', {'carserv': carserv})

