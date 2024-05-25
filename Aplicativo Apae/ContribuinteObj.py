class Contribuintes:
    
    def __init__(self, nome: str, endereco: str, numero:int, bairro:str, celular:str, valor:float, tipo:bool, ativo:bool) -> None:
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.bairro = bairro
        self.celular = celular
        self.valor =  valor
        self.tipo = tipo
        self.ativo = ativo
    
    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    

    @property
    def endereco(self):
        return self.endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.endereco = endereco

    @property
    def numero(self):
        return self.numero
    
    @numero.setter
    def numero(self, numero):
        self.numero = numero

    @property
    def bairro(self):
        return self.bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self.bairro = bairro

    @property
    def celular(self):
        return self.celular
    
    @celular.setter
    def celular(self, celular):
        self.celular = celular

    @property
    def valor(self):
        return self.valor
    
    @valor.setter
    def valor(self, valor):
        self.valor = valor

    @property
    def tipo(self):
        return self.tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo

    @property
    def ativo(self):
        return self.ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self.ativo = ativo



    