from django.shortcuts import render
from .utils import get_carserv_data
from django.views.decorators.cache import cache_page
from django.contrib import messages
from django.template import loader
from .forms import ContactForm
from django.http import HttpResponse

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


def contact_view(request):
    success_message = False  # Inicialmente, não há mensagem de sucesso
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Processa o formulário (envio de e-mail ou salvar no banco de dados)
            # Aqui você pode salvar os dados ou enviar um e-mail
            success_message = True  # Define como verdadeiro para exibir o alerta
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success_message': success_message})
