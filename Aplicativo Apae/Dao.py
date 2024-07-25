import mysql.connector
from ContribuinteObj import Contribuintes

class Conexao:
    def __init__(self) -> None:
        self._host = "localhost"
        self._user = "root"
        self._password = ""
        self._database = "apae"
        self._conn = None
        self._cursor = None

    def conectar(self):
        print('Iniciando conexão...')
        try:
            self._conn = mysql.connector.connect(
                host=self._host,
                user=self._user,
                password=self._password,
                database=self._database
            )
            self._cursor = self._conn.cursor()
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def desconectar(self):
        if self._conn is not None and self._conn.is_connected():
            self._cursor.close()
            self._conn.close()
            print("Conexão encerrada.")


class ConexaoContribuinte(Conexao):
    def __init__(self) -> None:
        super().__init__()

    def inserir_contribuinte(self, contribuinte):
        sql = "INSERT INTO doadores (ativo, tipo, nome, endereco, bairro, celular, valor, numero) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (
            contribuinte.get_ativo(),
            contribuinte.get_tipo(),
            contribuinte.get_nome(),
            contribuinte.get_endereco(),
            contribuinte.get_bairro(),
            contribuinte.get_celular(),
            contribuinte.get_valor(),
            contribuinte.get_numero()
        )
        try:
            self.conectar() 
            if self._cursor:
                self._cursor.execute(sql, valores)
                self._conn.commit()
                print("Contribuinte adicionado com sucesso.")
                return True
            else:
                print("Cursor não inicializado corretamente.")
                return False
        except mysql.connector.Error as err:
            print(f"Erro ao inserir contribuinte: {err}")
            return False
        finally:
            self.desconectar()

    def update_contribuinte(self, id, contribuinte):
        sql = "UPDATE doadores SET ativo = %s, tipo = %s, nome = %s, endereco = %s, bairro = %s, celular = %s, valor = %s, numero = %s WHERE id = %s" 
        valores = (
            contribuinte.get_ativo(),
            contribuinte.get_tipo(),
            contribuinte.get_nome(),
            contribuinte.get_endereco(),
            contribuinte.get_bairro(),
            contribuinte.get_celular(),
            contribuinte.get_valor(),
            contribuinte.get_numero(),
            id
        )
        try:
            self.conectar() 
            if self._cursor:
                self._cursor.execute(sql, valores)
                self._conn.commit()
                print("Contribuinte upgradiado com sucesso.")
                return True
        except mysql.connector.Error as err:
            print("Ocorreu um erro")
        finally:
            self.desconectar()

    def select_all(self):
        sql = "SELECT * FROM doadores"
        self.conectar() 
        self._cursor.execute(sql)
        result = self._cursor.fetchall()
        self.desconectar()
        return result
    
    def select_doador(self,id):
        sql = "SELECT * FROM doadores WHERE id = %s"
        self.conectar() 
        self._cursor.execute(sql,(id,))
        result = self._cursor.fetchall()
        self.desconectar()
        return result
    
    def delete_doador(self,id):
        sql = "DELETE FROM doadores WHERE id = %s"
        try:
            self.conectar()
            self._cursor.execute(sql,(id,))
            self._conn.commit()
            self.desconectar()
            print("Doador deletado com Sucesso!")
            return True
        except mysql.connector.errors as err:
            print(f'Erro {err}')
            return False
        finally:
            self.desconectar()


if __name__ == "__main__":
    conexao = ConexaoContribuinte()
    contribuinte = Contribuintes(1, 'Juridico', 'Marcos', 'Rua Rosangela do Livramento Pinheiro', 'Centro', '32 998540320', '90,90', 30)
    contribuinte2 = Contribuintes(1, 'Juridico', 'Daibo', 'Rua Rosangela do Livramento Pinheiro', 'Centro', '32 998540320', '90,90', 30)
    conexao.delete_doador(4)
