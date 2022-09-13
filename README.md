# API_Pharmacies

API desenvolvida para visualização dos dados de farmacias.

## Projeto API REST

Objetivo do projeto é de criar uma api rest privada para gerenciar a farmacia que está em busca de dados de (pacientes, farmacias e transações).

- [Poetry](https://python-poetry.org/docs/)
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Gunicorn](https://gunicorn.org)
- [Docker](https://www.docker.com)
- [Flasgger](https://github.com/flasgger/flasgger)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)

## Requisitos  (Linux)
Para rodar esse projeto na sua máquina você irá precisar instalar alguns programas, mas não se preocupe nós vamos ajudar você a executa-lo em sua maquina.

### 1º Poetry

Para a instalação do  [Poetry](https://python-poetry.org/docs/)

### 2º Python 3

Você deve instalar a versão 3.10 ou superior do [Python](https://www.python.org/downloads/).
Caso não tenha [pyenv](https://dev.to/womakerscode/instalando-o-python-com-o-pyenv-2dc7) talvez esse artigo possa ajuda-lo com problemas futuros.

### 3º Git

Documentação  para instalação do [Git](https://git-scm.com/downloads).

Agora vá para o proximo passo.


## Instalação

Agora, vamos para a instalação do projeto.


Entre no diretório onde vamos fazer o clone do nosso projeto.

```bash
# Veja se o diretório está correto no terminal.

$ pwd

# E nesse diretório que vamos colocar nosso projeto

$ /home/projeto/Documents/GitHub/api
```

Agora vamos fazer o clone do projeto.

```bash
# Fazendo o clone do projeto

$ git clone git@github.com:KingPack/api.git

```

### inicializar o ambiente virtual do Poetry.

```bash
# comando para entrar no ambiente virtual.
$ poetry shell
```

Apos inicializar o ambiente virtual, vamos atualizar o poetry.

```bash
$ poetry update

# comando para instalar todas as dependencias do projeto
$ poetry install
```

Pode demorar um pouco para instalar todas as dependências. Então vamos esperar um pouco.

### Executando a API

Variaveis de ambiente
```bash
# Variaveis de ambiente 
$ export FLASK_APP=pharmacies.main.py
$ export FLASK_DEBUG=True
```

```bash
# comando para executar o projeto
$ flask run

Output
 * Serving Flask app 'pharmacies.main.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 960-628-982
 ```
 ## Documentação da API
 
 Documentação das rotas ativas na API: http://localhost:5000/v1/documentation/

### JWT (Autenticação)


### Flask-Login (Extenção Flask)
 

## Docker

Para iniciar a imagem docker use na raiz do projeto

```bash
sudo docker build .

Successfully built e9974939d23f
```

http://localhost:8001/v1/documentation/
