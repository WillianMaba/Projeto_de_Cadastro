import sqlite3

def criarconexao():
    conexao = sqlite3.connect('database.db')
    return conexao