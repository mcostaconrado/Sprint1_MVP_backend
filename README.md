# Sprint1_MVP_frontend
Pós Graduação em Engenharia de Software - PUC-Rio - MVP Sprint 1

Este pequeno projeto é a implementação de um diário de viagens simples. É meu primeiro projeto de backend e, nele, utilizei Python e Flask para construir as rotas de API e a comunicação com o banco de dados SQLite.

O objetivo do projeto é por em prática o que foi ensinado na Sprint 1 do curso, além de começar um portfólio de apresentação profissional.

---
## Como executar 

Primeiramente, é necessário realizar o clone deste repositório:

```
$ git clone https://github.com/mcostaconrado/Sprint1_MVP_frontend.git
```

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
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
