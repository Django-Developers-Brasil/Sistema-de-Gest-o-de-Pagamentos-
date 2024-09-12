from django.db import models
from colorfield.fields import ColorField


class CarServ(models.Model):
    # Informações da empresa
    company_name = models.CharField(max_length=255, verbose_name="Nome da Empresa")
    endereco = models.CharField(max_length=255, verbose_name="Endereço da Empresa", null=True, blank=True)
    logo = models.ImageField(upload_to='carserv/images/', verbose_name="Logo da Empresa", null=True, blank=True)
    email = models.EmailField(verbose_name="Email da Empresa")
    phone = models.CharField(max_length=20, verbose_name="Telefone da Empresa")
    
    # Horários de funcionamento
    working_hours_weekdays = models.CharField(max_length=255, verbose_name="Horário de Funcionamento (Segunda a Sexta)")
    working_hours_saturday = models.CharField(max_length=255, verbose_name="Horário de Funcionamento (Sábado)")

    # Redes sociais e links
    twitter = models.URLField(null=True, blank=True, verbose_name="Twitter")
    facebook = models.URLField(null=True, blank=True, verbose_name="Facebook")
    linkedin = models.URLField(null=True, blank=True, verbose_name="LinkedIn")
    youtube = models.URLField(null=True, blank=True, verbose_name="YouTube")
    instagram = models.URLField(null=True, blank=True, verbose_name="Instagram")
    terms_of_service = models.URLField(null=True, blank=True, verbose_name="Termos de Serviço")
    privacy_policy = models.URLField(null=True, blank=True, verbose_name="Política de Privacidade")

    # Controle de visibilidade das seções
    show_navbar = models.BooleanField(default=True, verbose_name="Exibir Barra de Navegação")
    show_carousel = models.BooleanField(default=True, verbose_name="Exibir Carrossel")
    show_carousel_cars = models.BooleanField(default=True, verbose_name="Exibir o carro no Carrossel")
    show_services = models.BooleanField(default=True, verbose_name="Exibir Seção de Serviços")
    show_about_us = models.BooleanField(default=True, verbose_name="Exibir Seção 'Sobre Nós'")
    show_our_numbers = models.BooleanField(default=True, verbose_name="Exibir Nossos Números")
    show_book = models.BooleanField(default=True, verbose_name="Exibir Agendamento")
    show_our_technicians = models.BooleanField(default=True, verbose_name="Exibir Nosso Time")
    show_testimonials = models.BooleanField(default=True, verbose_name="Exibir Depoimentos")
    show_footer = models.BooleanField(default=True, verbose_name="Exibir Rodapé")

    # Imagens da Landing Page
    icon = models.ImageField(upload_to='carserv/images/', verbose_name="Icon da Empresa") 
    img_carrousel1 = models.ImageField(upload_to='carserv/images/', verbose_name="Imagem 1 do Banner")
    img_carrousel2 = models.ImageField(upload_to='carserv/images/', verbose_name="Imagem 2 do Banner")
    img_about = models.ImageField(upload_to='carserv/images/', verbose_name="Imagemda seção sobre")
    img_numbers = models.ImageField(upload_to='carserv/images/', verbose_name="Imagem da seção números")
    img_book = models.ImageField(upload_to='carserv/images/', verbose_name="Imagem da agendamento")
    img_footer = models.ImageField(upload_to='carserv/images/', verbose_name="Imagem do rodape")

    # Esquema de cores com django-colorfield
    color_primary = ColorField(help_text="Cor padrão: #BB101F", verbose_name="Cor Primária", null=True, blank=True)
    color_secondary = ColorField(help_text="Cor padrão: ", verbose_name="Cor Secundária", null=True, blank=True)
    color_success = ColorField(help_text="Cor padrão: ", verbose_name="Cor Sucesso", null=True, blank=True)
    color_danger = ColorField(help_text="Cor padrão: ", verbose_name="Cor Perigo", null=True, blank=True)
    color_warning = ColorField(help_text="Cor padrão: ", verbose_name="Cor Aviso", null=True, blank=True)
    color_info = ColorField(help_text="Cor padrão: ", verbose_name="Cor Informação", null=True, blank=True)
    color_light = ColorField(help_text="Cor padrão: ", verbose_name="Cor Clara", null=True, blank=True)
    color_dark = ColorField(help_text="Cor padrão: ", verbose_name="Cor Escura", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company_name



