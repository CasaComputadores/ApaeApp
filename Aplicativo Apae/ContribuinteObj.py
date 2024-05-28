class Contribuintes:
    
    def __init__(self, nome, endereco, numero, bairro, celular, valor, tipo, ativo, data) -> None:
        self._nome = nome
        self._endereco = endereco
        self._numero = numero
        self._bairro = bairro
        self._celular = celular
        self._valor = valor
        self._tipo = tipo
        self._ativo = ativo
        self._data = data
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def bairro(self):
        return self._bairro
    
    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    @property
    def celular(self):
        return self._celular
    
    @celular.setter
    def celular(self, celular):
        self._celular = celular

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data

    