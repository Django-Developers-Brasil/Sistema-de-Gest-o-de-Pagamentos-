from django.shortcuts import render
from .models import CarServ
import logging


# Cria um logger
logger = logging.getLogger('django')


def Error(request):
    try:
        # Tentando buscar o primeiro registro do modelo CarServ
        carserv = CarServ.objects.first()
        if not carserv:
            # Registra o erro no arquivo de log
            logger.error("Erro ao carregar dados da landing page: Nenhum registro encontrado.")
            return render(request, '404.html', status=404)  # Renderiza a página 404
    except Exception as e:
        # Registra o erro no arquivo de log
        logger.error(f"Erro ao carregar dados da landing page: {str(e)}")
        # Renderiza o template 404 em caso de erro
        return render(request, '404.html', status=404)

    return render(request,'404.html', {'carserv': carserv})


def index(request):
    try:
        # Tentando buscar o primeiro registro do modelo CarServ
        carserv = CarServ.objects.first()
        if not carserv:
            # Registra o erro no arquivo de log
            logger.error("Erro ao carregar dados da landing page: Nenhum registro encontrado.")
            return render(request, '404.html', status=404)  # Renderiza a página 404
    except Exception as e:
        # Registra o erro no arquivo de log
        logger.error(f"Erro ao carregar dados da landing page: {str(e)}")
        # Renderiza o template 404 em caso de erro
        return render(request, '404.html', status=404)

    # Passa os dados para o template 'index.html'
    return render(request, 'index.html', {'carserv': carserv})

"""
Django Sehll Interaction Example

Digite no terminal:

>>> python manage.py shell
>>> from webpage.models import CarServ
>>> carserv = CarServ.objects.first()
>>> print(carserv.__dict__)

"""