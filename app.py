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
produto_tag = Tag(name="Veículo", description="Adição, visualização e remoção de produtos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/registro', tags=[produto_tag],
          responses={"200": RegistroViewSchema})#, "409": ErrorSchema, "400": ErrorSchema})
def add_registro(form: RegistroSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    registro = Registro(
        titulo=form.titulo,
        descricao=form.descricao,
        imagem=form.imagem,
        data_registro=form.data_registro
        )
    logger.debug(f"Adicionando registro do dia: '{registro.data_registro}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(registro)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado registro do dia '{registro.data_registro}'")
        return apresenta_registro(registro), 200
    
    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar produto '{registro.data_registro}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(e)
        logger.warning(f"Erro ao adicionar produto '{registro.data_registro}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/registros', tags=[produto_tag],
         responses={"200": ListagemRegistrosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Produto cadastrados

    Retorna uma representação da listagem de produtos.
    """
    logger.debug(f"Coletando produtos ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    registros = session.query(Registro).all()
    print(len(registros))    
    if not registros:
        # se não há produtos cadastrados
        return {"registros": []}, 200
    else:
        logger.debug(f"%d registros econtrados" % len(registros))
        # retorna a representação de produto
        
        return apresenta_registros(registros), 200
'''
@app.get('/registro', tags=[produto_tag],
         responses={"200": RegistroViewSchema, "404": ErrorSchema})
def get_registro(query: RegistroBuscaSchema):
   
    """Faz a busca por um Registro a partir do id do produto
    Retorna uma representação dos produtos e comentários associados.
    """
    
    registro_id = query.id
    
    logger.debug(f"Coletando dados sobre produto #{registro_id}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    registro = session.query(Registro).filter(Registro.id == registro_id).first()

    if not registro:
        # se o produto não foi encontrado
        error_msg = "Registro não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{registro_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{registro.nome}'")
        # retorna a representação de produto
        return apresenta_registro(registro), 200

'''
@app.delete('/registro', tags=[produto_tag],
            responses={"200": RegistroDelSchema, "404": ErrorSchema})
def del_produto(query: RegistroBuscaSchema):
    """Deleta um Produto a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    data_registro = unquote(unquote(query.data_registro))
    
    logger.debug(f"Deletando dados sobre produto #{data_registro}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Registro).filter(Registro.data_registro == data_registro).delete()
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