from ninja import Router
from .models import CarServ, Newsletter
from ninja.security import django_auth
from django.http import HttpRequest
from ninja.errors import HttpError


# Autenticação personalizada para staff
def staff_only(request: HttpRequest):
    if request.user.is_authenticated and request.user.is_staff:
        return request.user
    raise HttpError(403, "Voce nao tem permissao para acessar este recurso.")


# Criando o router para a API
carserv_router = Router()
newsletter_router = Router()

# Endpoint acessível apenas para staff/admin
@carserv_router.get("/webpage/get/all", tags=["webpage"], auth=staff_only)
def carsev_get_all(request):
    carsev_objects = CarServ.objects.all().values()
    return list(carsev_objects)

# Endpoint acessível apenas para staff/admin
@newsletter_router.get("/newsletter/get/all", tags=["newsletter"], auth=staff_only)
def newsletter_get_all(request):
    newsletter_objects = Newsletter.objects.all().values()
    return list(newsletter_objects)

