# api_bluestorm

Projeto desenvolvido com base na entrevista tecnica na empresa BlueStorm

## Projeto API REST PRIVADA

Objetivo do projeto é de criar uma api rest privada para a clinica que está em busca de um sistema crud para obter informações do banco de dados.

- [Poetry](https://python-poetry.org/docs/)
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Gunicorn](https://gunicorn.org)
- [Postgres](https://www.postgresql.org)
- [Heroku](heroku.com)
- [Docker](https://www.docker.com)
- [Flasgger](https://github.com/flasgger/flasgger)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [Flake8](https://flake8.pycqa.org/en/latest/)

## Requisitos 
Para rodar esse projeto na sua máquina você irá precisar instalar alguns programas, mas não se preocupe nós vamos ajudar você a executa-lo em sua maquina.

### 1º Poetry

Para a instalação do  [Poetry](https://python-poetry.org/docs/)

### 2º Python 3

Você deve instalar a versão 3.9.10 ou superior do [Python](https://www.python.org/downloads/).
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

$ /home/projeto/Documents/GitHub/projeto_api
```

Agora vamos fazer o clone do projeto.

```bash
# Fazendo o clone do projeto

$ t clone git@github.com:KingPack/api.git

# Liste o diretório para ver e entrar no projeto

$ ls | grep api

# retorno 

$ api.git

# Entre no repositorio

$ cd api
```

### Se você chegou ate aqui sem erros, então já devemos estar preparados para inicializar o ambiente virtual do Poetry.

```bash
# comando para entrar no ambiente do poetry
$ poetry shell
```

Apos inicializar o ambiente virtual, vamos atualizar o poetry.

```bash
$ poetry update
```
apos isso, vamo executar 

```bash
# comando para instalar todas as dependencias do projeto
$ poetry install
```

Pode demorar um pouco para instalar todas as dependências. Então vamos esperar um pouco.

### Feito isso está tudo pronto para executar o programa.

Antes de executar não esqueca das variaveis de ambiente , caso tenha esquecido execute:
```bash
# comando para configurar as variaveis de ambiente 
$ export FLASK_APP=api
$ export FLASK_ENV=development
```

```bash
# comando para executar o projeto
$ flask run
```
Se tudo deu certo então voce terá um resultado parecido com esse:

Output
 * Serving Flask app "api_rest" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 813-894-335
 
 ## Parabens por executar o projeto com sucesso!
