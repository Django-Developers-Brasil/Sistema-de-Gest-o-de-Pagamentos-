## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12 com venv e pip instalados**  

  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

  Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):
 [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)


### Passos para Executar

1. **Clone o repositório via SSH**:
    ```bash
    git clone git@github.com:Django-Dev-Br/Sistema-de-Gest-o-de-Pagamentos-.git
    ```

2. **Crie  um ambiente virtual no diretório root**:

   **Windows**
    ```bash
     python -m venv myvenv  # Windows
    ```
      **Linux**
     ```bash
     python3 -m venv myvenv  # Linux
    ```

3. **Ative o ambiente virtual criado**:

   **Windows**
    ```bash
    myvenv\Scripts\activate  # Windows
    ```

     **Linux**
    ```bash
    source myvenv/bin/activate  # Linux
    ```

4. **Acesse a pasta do projeto Django**:

    ```bash
    cd Sistema-de-Gest-o-de-Pagamentos-
    ```

5. **Instale o Django e as demais dependências**:

   Fazer a instalação após a ativação da virtual env fará com que a instalação seja feita nessa pasta ao invés do computador. Isso significa que o pacote Django não estará disponivel para todos os usuários do computador, mas apenas para o contexto no qual essa venv esteja ativada. Veremos sua ativação logo abaixo.

    **Instalação via gerenciador de dependências PIP**
    ```bash
    pip install django==4.2.15 python-dotenv uv pretty-errors django-ckeditor
    ```
    ----- **OU** -----

    **Instalação via arquivo requirements**
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo requirements.txt é um arquivo de texto que contém uma lista de pacotes a ser instalado em uma venv. É uma boa prática de programação do ecossistema Python.

   [Por que o Django 4 continua sendo a melhor escolha para projetos atuais](https://django.dev.br/blog/por-que-o-django-4-continua-a-ser-a-melhor-escolha-para-projetos-atuais/)

6. **Crie o arquivo `.env` manualmente no diretório root do projeto**:

    **Linux**
    ```bash
    touch .env  # Linux
    ```
    **Windows**
    ```bash
    echo. > .env  # Windows
    ```
   
7. **Gere uma secret key para o django e acione  ao .env**:

    Para gerar uma `SECRET_KEY`, execute o seguinte comando no terminal:

    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

    Copie e cole a senha gerada no local indicado abaixo no seu arquivo .env:
   
   ```plaintext
    SECRET_KEY=sua_chave_secreta_aqui
    ```

8. **Execute as migrações do banco de dados**:

    ```bash
    python manage.py migrate
    ```
    O comando acima criará no diretório raiz o banco de dados db.sqlite3 com o esquema de tabelas do Django

9. **Crie um superusuário para acessar o Django Admin**:

    ```bash
    python manage.py createsuperuser
    ```
    Após, siga as instruções do terminal para criar um usuário e senha. Em regra, usa-se, respectivamente, admin e root. Não é preciso informar o email em ambiente local.

    **OU Carregar o Fixture (backup do banco)**:
    Se precisar restaurar os dados do superusuário a partir do fixture, use o seguinte comando:

    ```bash
    python manage.py loaddata superuser_fixture.json
    ```

    Isso carregará os dados do superusuário armazenados no fixture `superuser_fixture.json`. O superuser é **admin** e a senha é **root**



10. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Acesse no seu navegador os endereços a seguir:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)