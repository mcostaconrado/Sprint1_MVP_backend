from pydantic import BaseModel
from typing import Optional, List
from model.veiculo import Veiculo

class VeiculoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    montadora: str = "Toyota"
    modelo: str = "Corolla"
    
class VeiculoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    montadora: str = "Toyota"
    modelo: str = "Corolla"


def apresenta_veiculo(veiculo: Veiculo):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": veiculo.id,
        "montadora": veiculo.montadora,
        "modelo": veiculo.modelo
    }

class ListagemVeiculosSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    veiculos:List[VeiculoSchema]

def apresenta_veiculos(veiculos: List[Veiculo]):
    """ Retorna uma representação do produto seguindo o schema definido em
        ProdutoViewSchema.
    """
    result = []
    for veiculo in veiculos:
        result.append({
            "montadora": veiculo.montadora,
            "modelo": veiculo.modelo
        })

    return {"veiculos": result}

class VeiculoDelSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada.
    """
    message: str
    modelo: str
    
class VeiculoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do modelo.
    """
    modelo: str = "Teste"
