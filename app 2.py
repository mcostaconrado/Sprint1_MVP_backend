from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session
from model.Registro import Registro
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
registro_tag = Tag(name="Registro", description="Adição, visualização e remoção de registros de viagem à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/registro', tags=[registro_tag],
          responses={"200": RegistroViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_registro(form: RegistroSchema):
    """Adiciona um novo Registro de viagem à base de dados

    Retorna uma representação dos registros, com detalhes sobre a experiência.
    """
    registro = Registro(
        titulo=form.titulo,
        descricao=form.descricao,
        imagem=form.imagem,
        data_registro=form.data_registro
        )
    
    logger.debug(f"Adicionando registro '{registro.titulo}' do dia '{registro.data_registro}'")
    
    try:
        # criando conexão com a base
        session = Session()
        # adicionando registro de viagem
        session.add(registro)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado registro '{registro.titulo}' do dia '{registro.data_registro}'")
        return apresenta_registro(registro), 200
    
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(e)
        logger.warning(f"Erro ao adicionar registro '{registro.titulo}' do dia '{registro.data_registro}, {error_msg}")
        return {"mesage": error_msg}, 400
    '''
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{registro.data_registro}', {error_msg}")
        return {"mesage": error_msg}, 409
    '''


@app.get('/registros', tags=[registro_tag],
         responses={"200": ListagemRegistrosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Registros cadastrados na base de dados

    Retorna uma representação da listagem dos registros e todas as suas informações.
    """
    logger.debug(f"Capturando registros da base de dados...")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    registros = session.query(Registro).all()
    print(len(registros))    
    if not registros:
        # se não há registros cadastrados
        return {"registros": []}, 200
    else:
        logger.debug(f"%d registros econtrados" % len(registros))
        # retorna a representação de registro
        
        return apresenta_registros(registros), 200

@app.get('/registro', tags=[registro_tag],
         responses={"200": RegistroViewSchema, "404": ErrorSchema})
def get_registro(query: RegistroBuscaSchema):
   
    """Faz a busca por um Registro a partir do id do produto
    Retorna uma representação dos produtos e comentários associados.
    """

    titulo = query.titulo 
    data_registro = query.data_registro
    
    logger.debug(f"Coletando dados sobre {titulo} do dia {data_registro}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    registro = session.query(Registro).filter(Registro.titulo == titulo and Registro.data_registro == data_registro).first()

    if not registro:
        # se o produto não foi encontrado
        error_msg = "Registro não encontrado na base :/"
        logger.warning(f"Erro ao encontrar registro '{titulo}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Registro encontrado!")
        # retorna a representação de produto
        return apresenta_registro(registro), 200

@app.delete('/registro', tags=[registro_tag],
            responses={"200": RegistroDelSchema, "404": ErrorSchema})
def del_produto(query: RegistroBuscaSchema):
    """Deleta um Registro a partir do título e data informados

    Retorna uma mensagem de confirmação da remoção.
    """
    print(query)
    titulo_registro = query.titulo
    data_registro = unquote(unquote(query.data_registro))
    
    print(titulo_registro)
    print(data_registro)
    
    logger.debug(f"Deletando dados sobre produto #{data_registro}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Registro).filter(Registro.data_registro == data_registro and Registro.titulo == titulo_registro).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado produto #{data_registro}")
        return {"mesage": "Produto removido", "id": data_registro}
    else:
        # se o produto não foi encontrado
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{data_registro}', {error_msg}")
        return {"mesage": error_msg}, 404