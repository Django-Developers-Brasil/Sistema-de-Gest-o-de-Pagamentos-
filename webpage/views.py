from django.shortcuts import render, redirect
from .utils import get_carserv_data, is_valid_email
from django.views.decorators.cache import cache_page
from django.contrib import messages
from .models import Newsletter


# Aplicando cache de 15 minutos (900 segundos) à view
@cache_page(60 * 15)
def Error(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404

    return render(request, '404.html', {'carserv': carserv})


def Index(request):
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


def NewsLetter(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404
    
    if request.method == 'POST':
        email = request.POST.get('email')

        # Verifica se o email foi submetido e se é válido
        if email and is_valid_email(email):
            try:
                # Verifica se o email já está cadastrado
                newsletter_entry, created = Newsletter.objects.get_or_create(email=email)
                
                if created:
                    messages.success(request, 'Email cadastrado com sucesso!')
                else:
                    messages.warning(request, 'Email já cadastrado.')
            except Exception as e:
                messages.error(request, f'Ocorreu um erro ao tentar salvar o email: {e}')
        else:
            messages.error(request, 'Email inválido. Por favor, insira um email válido.')
        
        # Redireciona para a página de index (ou qualquer outra página)
        return redirect('index')  # Substitua 'index' pelo nome correto da URL

    return redirect('index')



def Contact(request):
    carserv = get_carserv_data()
    if not carserv:
        return render(request, '404.html', status=404)  # Renderiza a página 404
    
    if request.method == 'POST':
        # Mesmo que tenhamos validação no frontend, sempre valide no backend também
        name = request.POST.get('nome')
        email = request.POST.get('email')
        ddd = request.POST.get('ddd')
        prefixo = request.POST.get('prefixo')
        sufixo = request.POST.get('sufixo')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')
      
        # Validação básica
        if not name or not email or not assunto or not mensagem:
            messages.error(request, 'Por favor, inform nome, email, assunto e sua mensgem.')
        else:
            messages.success(request, 'Obrigado pelo contato! Responderemos em breve!')
    
    
    # Passa os dados para o template 
    return render(request, 'contact.html', {'carserv': carserv})
