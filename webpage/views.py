from django.shortcuts import render
from .utils import get_carserv_data
from django.views.decorators.cache import cache_page


# Aplicando cache de 15 minutos (900 segundos) à view
@cache_page(60 * 15)
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

