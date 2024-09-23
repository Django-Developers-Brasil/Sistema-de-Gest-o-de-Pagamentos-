from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Colaboradores, Clientes
from .utils import get_user_context
from datetime import date
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages

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
    # Pega o contexto do usuário e colaborador
    context = get_user_context(request)

    # Pega todos os clientes usando ORM
    clientes = Clientes.objects.filter(deleted_at__isnull=True)

    # Adiciona a lista de clientes ao contexto
    context['clientes'] = clientes

    return render(request, 'clientes.html', context)


def cliente_detail(request, id):

    context = get_user_context(request)

    # Pega o cliente usando ORM pelo ID
    cliente = get_object_or_404(Clientes, id=id)
     # Adiciona o cliente ao contexto
    context['cliente'] = cliente

    return render(request, 'cliente_detail.html', context)

def Cliente_delete(request, cliente_id):
    if request.method == 'POST':
        cliente = get_object_or_404(Clientes, id=cliente_id)
        cliente.deleted_at = timezone.now()  # Define a data atual no campo deleted_at
        cliente.save()
        messages.success(request, f'Cliente {cliente.nome_completo} excluído!')
        return redirect('clientes')  # Redireciona para a view 'clientes'
    return redirect('clientes')  # Redireciona se não for POST