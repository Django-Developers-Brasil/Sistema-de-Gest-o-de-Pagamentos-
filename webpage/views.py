from django.shortcuts import render
from .utils import get_carserv_data
from django.views.decorators.cache import cache_page
from django.contrib import messages


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
    
    if request.method == 'POST':
        # Mesmo que tenhamos validação no frontend, sempre valide no backend também
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')
        message_text = request.POST.get('message')

        # Validação básica
        if not name or not email or not service or not date:
            messages.error(request, 'Por favor, preencha todos os campos obrigatórios.')
        else:
            messages.success(request, 'Obrigado pelo agendamento! Entraremos em contato em breve!')
            
    # Passa os dados para o template 'index.html'
    return render(request, 'index.html', {'carserv': carserv})


def Contact(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404
    
    # Passa os dados para o template 
    return render(request, 'contact.html', {'carserv': carserv})