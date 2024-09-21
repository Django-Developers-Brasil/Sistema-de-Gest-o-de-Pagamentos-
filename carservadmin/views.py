from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Colaboradores


@staff_member_required
def Home(request):
     # Verifica se o usuário está autenticado
    if request.user.is_authenticated:
        # Tenta obter os dados do colaborador relacionado ao usuário
        try:
            colaborador = request.user.colaborador  # O campo 'colaborador' vem do related_name
            foto = colaborador.foto.url if colaborador.foto else None  # Verifica se a foto existe
        except Colaboradores.DoesNotExist:
            colaborador = None
            foto = None
        
        # Passa os dados para o contexto
        context = {
            'nome': request.user.first_name,
            'sobrenome': request.user.last_name,
            'email': request.user.email,
            'foto': foto,  # Adiciona a foto ao contexto
        }
    else:
        context = {}
    
    return render(request, 'home.html', context)



def Logout(request):
    logout(request)
    return redirect('/c-panel/login/') 