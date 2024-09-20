from ninja import Router
from .models import CarServ, Newsletter
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Criando o router para a API
carserv_router = Router()
newsletter_router = Router()

# Endpoint para Carsev (disponível para todos)
@carserv_router.get("/webpage/get/all", tags=["webpage"])
def carsev_get_all(request):
    carsev_objects = CarServ.objects.all().values()
    return list(carsev_objects)


# Endpoint para newsletter (disponível para todos)
@newsletter_router.get("/newsletter/get/all", tags=["newsletter"])
def newsletter_get_all(request):
    newsletter_objects = Newsletter.objects.all().values()
    return list(newsletter_objects)

