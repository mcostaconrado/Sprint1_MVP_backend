from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Registro(Base):
    
    __tablename__ = 'registro'
    
    id = Column("pk_registro", Integer, primary_key=True) 
    titulo = Column(String(70))
    descricao = Column(String(500))
    imagem = Column(String(50))
    data_registro = Column(String(10))
    data_insercao = Column(DateTime, default=datetime.now())

    
    def __init__(self, titulo:str, descricao:str, imagem:str, data_registro:str , data_insercao:Union[DateTime, None] = None):
        
        self.titulo = titulo
        self.descricao = descricao
        self.imagem = imagem
        
        self.data_registro = data_registro
        
        if data_insercao:
            self.data_insercao = data_insercao