# Sprint1_MVP_backend
Pós Graduação em Engenharia de Software - PUC-Rio - MVP Sprint 1

Este pequeno projeto é a implementação de um diário de viagens simples. É meu primeiro projeto de backend e, nele, utilizei Python e Flask para construir as rotas de API e a comunicação com o banco de dados SQLite.

O objetivo do projeto é por em prática o que foi aprendido na Sprint 1 do curso, além de começar um portfólio de apresentação profissional.

---
## Como executar 

Primeiramente, é necessário realizar o clone deste repositório:

```
$ git clone https://github.com/mcostaconrado/Sprint1_MVP_backend.git
```

O repositório conta com o arquivo `requirements.txt`. Neles, se encontram todas as libs Python que terão que ser instaladas para que o projeto possa ser executado.
É recomendado, embora não obrigatório, realizar essas instalações em um ambiente virtual do tipo [virtualenv], a fim de não se misturar versões com outros possíveis projetos na máquina. Essa etapa pode ser realizada com os comandos a seguir:

```
$ python3.9 -m venv env_app
$ source env_app/bin/activate
```

Após isso, já no ambiente virtual, é realizado o download de dependências do projeto com o comando a seguir:

```
(env_app)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
