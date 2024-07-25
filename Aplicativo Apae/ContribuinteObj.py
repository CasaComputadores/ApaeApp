class Contribuintes:
    
    def __init__(self, ativo, tipo, nome, endereco, bairro, celular, valor, numero) -> None:
        self._nome = nome
        self._endereco = endereco
        self._numero = numero
        self._bairro = bairro
        self._celular = celular
        self._valor = valor
        self._tipo = tipo
        self._ativo = ativo
    
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_endereco(self):
        return self._endereco
    
    def set_endereco(self, endereco):
        self._endereco = endereco

    def get_numero(self):
        return self._numero
    
    def set_numero(self, numero):
        self._numero = numero

    def get_bairro(self):
        return self._bairro
    

    def set_bairro(self, bairro):
        self._bairro = bairro

    def get_celular(self):
        return self._celular
    
    def set_celular(self, celular):
        self._celular = celular

    def get_valor(self):
        return self._valor
   
    def set_valor(self, valor):
        self._valor = valor

    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, tipo):
        self._tipo = tipo


    def get_ativo(self):
        return self._ativo
    

    def set_ativo(self, ativo):
        self._ativo = ativo

if __name__ == "__main__":
    contribuinte = Contribuintes(1, 'Fisico', 'Marcos', 'Rua Rosangela do Livramento Pinheiro', 'Centro', '32 998540320', '90,90', 30)
    print(contribuinte.get_nome())