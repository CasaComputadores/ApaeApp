from Dao import *
from ContribuinteObj import *

# Criando a classe de SQL para manipular Contribuintes
class ContribuinteConexao (Conexao):
    
    def __init__(self) -> None:
         super().__init__()
    
    #cria um novo contribuinte
    def inserir_contribuinte(self, contribuinte):
        query = "INSERT INTO doadores(ativo, tipo, nome, endereco, bairro, telefone, valor, numero) VALUES (?,?,?,?,?,?,?,?);"

        if self._conn is None or not self._conn.is_connected():
            print("Não há conexão estabelecida.")
            return None
        #try:
        self.cursor.execute(query, (
            contribuinte.tipo,
            contribuinte.ativo,
            contribuinte.nome,
            contribuinte.endereco,
            contribuinte.bairro,
            contribuinte.celular,
            contribuinte.valor,
            contribuinte.numero ))
        self._conn.commit()
        #except mysql.connector.Error as err:
        #   print(f"Erro ao executar a query: {err}")
        

    '''
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

        return results
    
    def selecionar_todos(self):
        self.cursor.execute("SELECT * FROM contribuintes")
        columns = [column[0] for column in self.cursor.description]
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return results
'''

if __name__ == "__main__":
    contribuinte1 = Contribuintes(1, "PF", "daibo", "rua", "rua", "não tenho", 2.45, 2)
    conexao = ContribuinteConexao()
    conexao.conectar()
    conexao.inserir_contribuinte(contribuinte1)
    #conexao.fechar_conexao()

