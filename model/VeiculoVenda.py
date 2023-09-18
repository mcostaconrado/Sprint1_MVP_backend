class VeiculoVenda:
    
    def __init__(self, placa, ano_fabricacao, ano_modelo, quilometragem, valor, desconto):
        self.__placa = placa
        self.__ano_fabricacao = ano_fabricacao
        self.__ano_modelo = ano_modelo
        self.__quilometragem = quilometragem        
        self.__valor = valor
        self.__desconto = desconto
        
    # MÉTODOS GET

    def get_placa(self):
        return self.__placa

    def get_chassi(self):
        return self.__chassi

    def get_ano_fabricacao(self):
        return self.__ano_fabricacao

    def get_ano_modelo(self):
        return self.__ano_modelo

    def get_quilometragem(self):
        return self.__quilometragem
    
    def get_valor(self):
        return self.__valor
    
    def get_desconto(self):
        return self.__desconto
    
    # MÉTODOS SET     
    def set_valor(self, valor):
        self.__valor = valor
    
    def set_placa(self, placa):
        self.__placa = placa
        
    def set_desconto(self, desconto):
        self.__desconto = desconto