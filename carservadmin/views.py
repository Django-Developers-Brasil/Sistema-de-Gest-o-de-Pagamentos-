from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Colaboradores, Clientes
from .utils import get_user_context
from datetime import date
from django.shortcuts import render, get_object_or_404



@staff_member_required
def Home(request):
    
    context = get_user_context(request)

    # Consulta para obter o total de registros na tabela Clientes
    total_clientes = Clientes.objects.count()

    # Adiciona o total de clientes ao contexto
    context['total_clientes'] = total_clientes

    # Pegando aniversariantes do dia
    hoje = date.today()
    aniversariantes = Clientes.objects.filter(data_nascimento__month=hoje.month, data_nascimento__day=hoje.day)
    
    # Adiciona os aniversariantes ao contexto se houver
    if aniversariantes.exists():
        context['aniversariantes'] = aniversariantes
    
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


def cliente_detail(request, id):
    cliente = get_object_or_404(Clientes, id=id)
    return render(request, 'cliente_detail.html', {'cliente': cliente})
