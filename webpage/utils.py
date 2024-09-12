import logging
from .models import CarServ

# Cria um logger
logger = logging.getLogger('django')

def get_carserv_data():
    try:
        # Tentando buscar o primeiro registro do modelo CarServ
        carserv = CarServ.objects.first()
        if not carserv:
            # Registra o erro no arquivo de log
            logger.error("Erro ao carregar dados da landing page: Nenhum registro encontrado.")
            return None
        return carserv
    except Exception as e:
        # Registra o erro no arquivo de log
        logger.error(f"Erro ao carregar dados da landing page: {str(e)}")
        return None


"""
Django Sehll Interaction Example

Digite no terminal:

>>> python manage.py shell
>>> from webpage.models import CarServ
>>> carserv = CarServ.objects.first()
>>> print(carserv.__dict__)

"""