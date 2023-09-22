from pydantic import BaseModel
from typing import Optional, List
from model.Registro import Registro

class RegistroSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    titulo: str = "Passeio"
    descricao: str = "Toyota"
    imagem: str = "aaa"
    data_registro: str = "15/09/2023"
    
class RegistroViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    titulo: str = "Passseio em xxxxx"
    descricao: str = "Hoje fizemos um passeio, foi muito legal ...."
    imagem: str = "!!!"
    data_registro : str = "15/09/2023"

def apresenta_registro(registro: Registro):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": registro.id,
        "titulo": registro.titulo,
        "descricao": registro.descricao,
        "imagem": registro.imagem,
        "data_registro": registro.data_registro
    }
    
class RegistroBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca por um registro. 
        Deverão ser fornecidos o título da avaliação e a data do registro
    """
    titulo: str = "Passeio com a família em Buenos Aires"
    data_registro: str = "15/09/2023"


class ListagemRegistrosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    veiculos:List[RegistroSchema]
    

def apresenta_registros(registros: List[Registro]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for registro in registros:
        result.append({
            "titulo": registro.titulo,
            "descricao": registro.descricao,
            "imagem": registro.imagem,
            "data_registro": registro.data_registro
        })

    return {"registros": result}


class RegistroDelSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    titulo: str
    data_registro: str
