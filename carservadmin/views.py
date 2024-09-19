from django.shortcuts import HttpResponse

# Create your views here.
def carservadminTest(request):
    return HttpResponse("<h1> Olá, esse é um teste para a rota carservadmin! </h1>")