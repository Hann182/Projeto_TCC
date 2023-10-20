import sqlite3

class sqlite_db:
    def __init__(self, banco = None): # Cria banco de dados
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self,banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexao feita")
        except sqlite3.Error as e:
            print("Conexao nao feita")

#db = sqlite_db("user.db")

#def cria_tabela(self):
        #cur = self.cursor
        #cur.execute("""IF NOT EXISTS CREATE TABLE usuarios(
            #id_usuarios integer primary key autoincrement,
            #nome varchar(20) NOT NULL,
            #senha varchar(4) NOT NULL
            #)""")

    def crud(self,query):
             cur = self.cursor
             cur.execute(query)
             self.conn.commit()

    def dados(self,query):
         cur= self.cursor
         cur.execute(query)
         return cur.fetchall()

#db = sqlite_db("5.db")
#
#db.cria_tabela()  
#db.crud("UPDATE usuarios SET nome = 'Jorge'")
#print(db.dados("SELECT * FROM usuarios"))
#db.cria_tabela()