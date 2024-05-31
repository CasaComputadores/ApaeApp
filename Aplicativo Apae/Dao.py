import mysql.connector

class Conexao:
    def __init__(self) -> None:
        self._host = "localhost"
        self._user = "root"
        self._password = "123456789"
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
            self.cursor = self._conn.cursor()
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")

    def desconectar(self):
        if self._conn is not None and self._conn.is_connected():
            self.cursor.close()
            self._conn.close()
            print("Conexão encerrada.")

if __name__ == "__main__":
    conexao = Conexao()
    conexao.conectar()
    conexao.desconectar()