from django.db import models
from django.contrib.auth.models import User


class Colaboradores(models.Model):
    # Relaciona com o modelo User (OneToOneField)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='colaborador')
    
    # Foto do colaborador
    foto = models.ImageField(upload_to='colaboradores/fotos/', blank=True, null=True, verbose_name="Foto")
    
    # Matrícula alfanumérica
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")

    # Telefones
    telefone_fixo = models.CharField(max_length=15, blank=True, verbose_name="Telefone Fixo")
    telefone_celular = models.CharField(max_length=15, verbose_name="Celular")

    # Endereço completo no padrão brasileiro
    endereco = models.CharField(max_length=255, verbose_name="Endereço")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    cidade = models.CharField(max_length=100, verbose_name="Cidade")
    estado = models.CharField(max_length=2, choices=[
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
        ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ], verbose_name="Estado")
    cep = models.CharField(max_length=9, verbose_name="CEP")  # Formato: 12345-678

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.matricula}"
    
    class Meta:
        verbose_name = "Colaborador"  # Nome no singular
        verbose_name_plural = "Colaboradores"  # Nome no plural
