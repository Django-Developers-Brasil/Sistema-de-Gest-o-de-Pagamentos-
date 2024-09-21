from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Colaboradores, Clientes
from .utils import get_user_context


@staff_member_required
def Home(request):
    
    context = get_user_context(request)
    
    return render(request, 'home.html', context)


def Logout(request):
    logout(request)
    return redirect('/c-panel/login/') 


@staff_member_required
def clientes_view(request):
    # Pega todos os clientes usando ORM
    clientes = Clientes.objects.all()

    # Pega o contexto do usuário e colaborador
    context = get_user_context(request)

    # Adiciona a lista de clientes ao contexto
    context['clientes'] = clientes

    return render(request, 'clientes.html', context)