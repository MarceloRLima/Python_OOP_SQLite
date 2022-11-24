import sqlite3

class BaseDados:
    #Atributos
    conexao = None
    cursor = None

    #Método construtor
    def __init__(self):
        self.conexao = sqlite3.connect("basedados/imdb.db")
        self.cursor = self.conexao.cursor()

    def __del__(self):
        self.conexao.commit()
      