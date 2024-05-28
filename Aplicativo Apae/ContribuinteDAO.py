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
            INSERT INTO contribuintes (nome, endereco, numero, bairro, celular, valor, tipo, ativo, data) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            contribuinte.nome, 
            contribuinte.endereco, 
            contribuinte.numero, 
            contribuinte.bairro, 
            contribuinte.celular, 
            contribuinte.valor, 
            contribuinte.tipo, 
            contribuinte.ativo,
            contribuinte.data
        ))
        self.banco.commit()

    
    def editar_contribuinte(self, codigo, contribuinte):
        self.cursor.execute("""
            UPDATE contribuintes SET nome = ?, endereco = ?, numero = ?, bairro = ?, celular = ?, valor = ?, tipo = ?, ativo = ?, data = ? WHERE id = ?
        """, (
            contribuinte.nome, 
            contribuinte.endereco, 
            contribuinte.numero, 
            contribuinte.bairro, 
            contribuinte.celular, 
            contribuinte.valor, 
            contribuinte.tipo, 
            contribuinte.ativo,
            contribuinte.data,
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

        return results
    
    def selecionar_todos(self):
        self.cursor.execute("SELECT * FROM contribuintes")
        columns = [column[0] for column in self.cursor.description]
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return results


if __name__ == "__main__":
    conexao = ContribuinteConexao()
    conexao.fechar_conexao()

        
