# Sprint1_MVP_backend
Pós Graduação em Engenharia de Software - PUC-Rio - MVP Sprint 1

Este pequeno projeto é a implementação do backend de um diário de viagens simples. É meu primeiro projeto de backend e, nele, utilizei Python e Flask para construir as rotas de API e a comunicação com o banco de dados SQLite. Para realizar a comunicação entre o banco de dados e a linguagem de programação, foi utilizada a técnica ORM com SQLAlchemy. 

O objetivo do projeto é por em prática o que foi aprendido na Sprint 1 do curso, além de começar um portfólio de apresentação profissional.

---
## Como executar 

Primeiramente, é necessário realizar o clone deste repositório:

```
$ git clone https://github.com/mcostaconrado/Sprint1_MVP_backend.git
```

O repositório conta com o arquivo `requirements.txt`. Nele, se encontram todas as bibliotecas Python que terão que ser instaladas para que o projeto possa ser executado.
É recomendado, embora não obrigatório, realizar essas instalações em um ambiente virtual do tipo [virtualenv], a fim de não se misturar versões com outros possíveis projetos na máquina. Utilizando a versão 3.9 do Python, essa etapa pode ser realizada com os comandos a seguir:

```
$ python3.9 -m venv env_app
$ source env_app/bin/activate
```

Após isso, já no ambiente virtual, é realizado o download de dependências do projeto com o comando a seguir:

```
(env_app)$ pip install -r requirements.txt
```

Finalmente, para executar a API, basta digitar o comando abaixo:

```
(env_app)$ pip install -r requirements.txt
$ flask run --host 0.0.0.0 --port 5000
```

Também é possível rodar o código acima adicionando, ao fim, o parâmetro `--reload`. Este parâmetro faz com que o servidor da aplicação seja reinicado automaticamente após qualquer mudança do código fonte. Pode ser útil em casos de desenvolvimento e debug.

Para verificar o status da API em execução, basta abrir o link abaixo no navegador:
[http://localhost:5000/#/](http://localhost:5000/#/)

Para encerrar o servidor, basta digitar Ctrl + C no terminal de execução, e ele será interrompido.

Para sair do ambiente virtual, digite o comando a seguir:
```
(env_app)$ pip install -r requirements.txt
```