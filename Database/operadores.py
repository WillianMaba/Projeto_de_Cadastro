from Database.conexao import criarconexao
from CONFIGs.Interface import linha

def cadastrar_usuarios(nome, email, idade):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''
            INSERT INTO usuarios(nome, email, idade)
            VALUES (?, ?, ?)
            ''',(nome, email, idade))

        con.commit()
        print(f'Usuário {nome} cadastrado com sucesso!')
    except Exception as e:
        print(f'❌ Erro ao cadastrar usuário:{e}')
    finally:
        con.close()


def cadastrar_produtos(nome, valor, descricao):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''
                INSERT INTO produtos(nome, valor, descricao)
                VALUES (?, ?, ?)
                ''', (nome, valor, descricao))

        con.commit()
        print(f'Produto {nome} cadastrado com sucesso!')
    except Exception as e:
        print(f'❌ Erro ao cadastrar produto:{e}')
    finally:
        con.close()


def visualizar_usuarios():
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute("SELECT * FROM usuarios")
        usuarios = cur.fetchall()

        if not usuarios:
            print('⚠️ Nenhum usuário encontrado!')
        else:
            print(linha())
            print("LISTA DE USUÁRIOS")
            print(linha())
            for usuario in usuarios:
                print(f"ID: {usuario[0]}")
                print(f"Nome: {usuario[1]}")
                print(f"Email: {usuario[2]}")
                print(f"Idade: {usuario[3]}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar usuário", e)
    finally:
        con.close()

def visualizar_produtos():
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute("SELECT * FROM produtos")
        produtos = cur.fetchall()

        if not produtos:
            print('⚠️ Nenhum produto encontrado!')
        else:
            print(linha())
            print("LISTA DE PRODUTOS")
            print(linha())
            for produto in produtos:
                print(f"ID: {produto[0]}")
                print(f"Nome: {produto[1]}")
                print(f"Valor: {produto[2]}")
                print(f"Descrição: {produto[3]}")
                print(linha())
    except Exception as e:
        print("❌ Erro ao buscar produto", e)
    finally:
        con.close()


def atualizar_usuario(id_usuarios, nome, email, idade):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE usuarios
                        SET nome = ?, email = ?, idade = ?
                    WHERE id = ?''',(nome, email, idade, id_usuarios))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Usuário ID {id_usuarios} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum Usuário encontrado com ID {id_usuarios}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar Usuário:{e}')
    finally:
        con.close()


def atualizar_produto(id_produtos, nome, valor, descricao):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''UPDATE produtos
                        SET nome = ?, valor = ?, descricao = ?
                    WHERE id = ?''',(nome, valor, descricao, id_produtos))
        con.commit()
        if cur.rowcount > 0:
            print(f'✅ Produto ID {id_produtos} atualizado com sucesso!')
        else:
            print(f'⚠️ Nenhum Produto encontrado com ID {id_produtos}.')
    except Exception as e:
        print(f'❌ Erro ao atualizar Produto:{e}')
    finally:
        con.close()


def excluir_usuario(id_usuarios):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM usuarios WHERE id = ?''', (id_usuarios))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Usuário ID {id_usuarios} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum Usuário encontrado com ID {id_usuarios}.')
    except Exception as e:
        print(f'❌ Erro ao excluir Usuário:{e}')
    finally:
        con.close()

def excluir_produto(id_produtos):
    con = criarconexao()
    cur = con.cursor()

    try:
        cur.execute('''DELETE FROM produtos WHERE id = ?''', (id_produtos))
        con.commit()
        if cur.rowcount > 0:
            print(f'🗑️ Produtos ID {id_produtos} excluído com sucesso!')
        else:
            print(f'⚠️ Nenhum Produtos encontrado com ID {id_produtos}.')
    except Exception as e:
        print(f'❌ Erro ao excluir Produtos:{e}')
    finally:
        con.close()