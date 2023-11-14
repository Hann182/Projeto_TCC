import os
import sqlite3

class sqlite_db:
    def __init__(self, banco=None): # Cria banco de dados
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexao feita")
        except sqlite3.Error as e:
            print("Conexao nao feita")

    def cria_tabela(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE IF NOT EXISTS usuarios(
            id_usuarios integer primary key autoincrement,
            nome varchar(20) NOT NULL,
            senha varchar(4) NOT NULL
        )""")

    def crud(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def dados(self,query):
        cur=self.cursor
        cur.execute(query)
        return cur.fetchall()

caminho_pasta_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'Banco')
db = sqlite_db(os.path.join(caminho_pasta_banco, 'banco.db'))

db.cria_tabela()