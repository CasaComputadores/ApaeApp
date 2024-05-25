import sqlite3
from ContribuinteObj import Contribuintes

# Criando a classe de SQL para manipular Contribuintes
class ContribuinteConexao:
    def __init__(self) -> None:
        self.banco = sqlite3.connect('banco_apae.db')
        self.cursor = self.banco.cursor()

   
    def fechar_conexao(self) -> None:
        self.banco.close()

    #cria um novo contribuinte
    def inserir_contribuinte(self, contribuinte):

        
        self.cursor.execute("""
            INSERT INTO contribuintes (nome, endereco, numero, bairro, celular, valor, tipo, ativo) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            contribuinte.nome, 
            contribuinte.endereco, 
            contribuinte.numero, 
            contribuinte.bairro, 
            contribuinte.celular, 
            contribuinte.valor, 
            contribuinte.tipo, 
            contribuinte.ativo
        ))
        self.banco.commit()

    
    def editar_contribuinte(self, codigo, contribuinte):
        self.cursor.execute("""
            UPDATE contribuintes SET nome = ?, endereco = ?, numero = ?, bairro = ?, celular = ?, valor = ?, tipo = ?, ativo = ? WHERE id = ?
        """, (
            contribuinte.nome, 
            contribuinte.endereco, 
            contribuinte.numero, 
            contribuinte.bairro, 
            contribuinte.celular, 
            contribuinte.valor, 
            contribuinte.tipo, 
            contribuinte.ativo,
            codigo
        ))
        self.banco.commit()

    def deletar_contribuinte(self,codigo):
        self.cursor.execute("DELETE FROM contribuintes WHERE id = ?", (
            codigo,
        ))
        self.banco.commit()

    #Selecionando os contribuintes de acordo com nome ou codigo
    def selecionar_contribuinte(self,codigo=None, nome=None):
        if codigo:
            print("Selecionando contribuinte pelo código:", codigo)
            self.cursor.execute("SELECT * FROM contribuintes WHERE id = ?", (codigo,))
        elif nome:
            print("Selecionando contribuinte pelo nome:", nome)
            self.cursor.execute("SELECT * FROM contribuintes WHERE nome = ?", (nome,))
        else:
            print("Erro")
        
        columns = [column[0] for column in self.cursor.description]
    
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        
        print(f'"resultado"{results}')
        





if __name__ == "__main__":
    contribuinte1 = Contribuintes("joao", "rua1", 12, "centro", "(32)999-999", 15.40, True, True)
    conexao = ContribuinteConexao()
    conexao.selecionar_contribuinte(None,"joao")
    conexao.fechar_conexao()

        
