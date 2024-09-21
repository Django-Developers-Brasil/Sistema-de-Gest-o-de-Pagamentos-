from .models import Colaboradores

def get_user_context(request):
    """
    Retorna um dicionário com os dados do usuário e colaborador logado.
    """
    if request.user.is_authenticated:
        # Tenta obter os dados do colaborador relacionado ao usuário
        try:
            colaborador = request.user.colaborador  # O campo 'colaborador' vem do related_name
            foto = colaborador.foto.url if colaborador.foto else None  # Verifica se a foto existe
        except Colaboradores.DoesNotExist:
            colaborador = None
            foto = None
        
        # Retorna o contexto com os dados do usuário
        return {
            'nome': request.user.first_name,
            'sobrenome': request.user.last_name,
            'email': request.user.email,
            'foto': foto,
        }
    else:
        return {}
