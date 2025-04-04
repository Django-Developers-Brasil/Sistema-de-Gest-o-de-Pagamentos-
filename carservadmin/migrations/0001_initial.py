# Generated by Django 4.2.16 on 2024-09-21 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='colaboradores/fotos/', verbose_name='Foto')),
                ('matricula', models.CharField(max_length=20, unique=True, verbose_name='Matrícula')),
                ('telefone_fixo', models.CharField(blank=True, max_length=15, verbose_name='Telefone Fixo')),
                ('telefone_celular', models.CharField(max_length=15, verbose_name='Celular')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='Estado')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='colaborador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
