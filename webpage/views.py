from django.shortcuts import render
from .utils import get_carserv_data
from django.views.decorators.cache import cache_page


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
        print('enviado')
        # Mesmo que tenhamos validação no frontend, sempre valide no backend também
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        date = request.POST.get('date')
        message_text = request.POST.get('message')

        # Validação básica
        if not name or not email or not service or not date:
            print('form vazio')     
        else:
            print(f'{name}, {email}, {service} e {date}')
            
    # Passa os dados para o template 'index.html'
    return render(request, 'index.html', {'carserv': carserv})

