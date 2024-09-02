## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12**  
  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

  Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual):
 [![Watch the video](https://img.youtube.com/vi/eetDeQrv0Rs/0.jpg)](https://youtu.be/eetDeQrv0Rs)

- **Virtualenv**

  Para instalar o pacote `virtualenv` no Python, utilize os seguintes comandos:

  - **Linux**:
    ```bash
    python3 -m pip install virtualenv
    ```

  - **Windows**:
    ```bash
    python -m pip install virtualenv
    ```

### Passos para Executar

1. **Clone o repositório**:
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

4. **Ative o ambiente virtual criado**:

   **Windows**
    ```bash
    myvenv\Scripts\activate  # Windows
    ```

     **Linux**
    ```bash
    source myvenv/bin/activate  # Linux
    ```

6. **Instale o Django**:

   Fazer a instalação após a ativação da virtual env fará com que a instalação seja feita nessa pasta ao invés do computador. Isso significa que o pacote Django não estará disponivel para todos os usuários do computador, mas apenas para o contexto no qual essa venv esteja ativada. Veremos sua ativação logo abaixo.

    **Instalação via gerenciador de dependências PIP**
    ```bash
    pip install django==4.2.15
    ```
    ----- **OU** -----

    **Instalação via arquivo requirements**
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo requirements.txt é um arquivo de texto que contém uma lista de pacotes a ser instalado em uma venv. É uma boa prática de programação do ecossistema Python.

   [Por que o Django 4 continua sendo a melhor escolha para projetos atuais](https://django.dev.br/blog/por-que-o-django-4-continua-a-ser-a-melhor-escolha-para-projetos-atuais/)

8. **Acesse a pasta do projeto Django**:
    ```bash
    cd Sistema-de-Gest-o-de-Pagamentos-
    ```

9. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Acesse no seu navegador o endereço a seguir:

http://127.0.0.1:8000/