from Database.conexao import criarconexao

def criar_tabela():
    con = criarconexao()
    cur = con.cursor()


    cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            idade INTEGER NOT NULL
            )
    ''')

    cur.execute('''CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                valor REAL NOT NULL,
                descricao TEXT NOT NULL
                )
        ''')

    con.commit()
    con.close()