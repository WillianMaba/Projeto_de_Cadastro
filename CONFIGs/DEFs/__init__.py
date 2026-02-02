from time import sleep
from CONFIGs.Interface import *
from Database import operadores



def menu():
    while True:
        print(linha())
        print('Sistema de Cadastro'.center(40))
        print(linha())
        print('1 - Cadastrar usuário\n'
              '2 - Cadastrar produto\n'
              '3 - Visualizar usuários\n'
              '4 - Visualizar produtos\n'
              '5 - Atualizar cadastro usuário\n'
              '6 - Atualizar cadastro produto\n'
              '7 - Apagar cadastro de usuário\n'
              '8 - Apagar cadastro de produto\n'
              '0 - Sair')
        try:
            opcao = int(input('Escolha sua opção: '))
        except ValueError:
            print('Digite apenas uma das opções acima!')
            continue


        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            cadastrar_produto()
        elif opcao == 3:
            visualizar_usuarios()
        elif opcao == 4:
            visualizar_produtos()
        elif opcao == 5:
            atualizar_usuarios()
        elif opcao == 6:
            atualizar_produtos()
        elif opcao == 7:
            excluir_usuario()
        elif opcao == 8:
            excluir_produto()
        elif opcao == 0:
            print(linha())
            print('ENCERRANDO PROGRAMA...')
            print('Muito Obrigado! Volte Sempre!')
            print(linha())
            break
        else:
            print('Opção inválida!')


def pergunta_continuar(msg):
    while True:
        resp = input(msg).strip().lower()
        if resp in ['s', 'sim']:
            return 's'
        elif resp in ['n', 'nao', 'não']:
            return 'n'
        else:
            print('Digite Apenas S, N, Sim, Não')


def cadastrar_usuario():
    while True:
        print(linha())
        print('CADASTRO DE USUÁRIO'.center(40))
        print(linha())
        try:
            nome = input('Digite o nome do usuário: ')
            email = input('Digite o email do usuário: ')
            idade = int(input('Digite sua idade: '))
            valido, msg = operadores.validar_usuario(nome, email, idade)
            if not valido:
                print(f'⚠️ {msg}')
                continue
            operadores.cadastrar_usuarios(nome, email, idade)
            print(f'Usuário {nome} cadastrado com sucesso!')
            sleep(2)
        except Exception as e:
            print('Erro ao cadastrar usuário! Tente novamente!')
        if pergunta_continuar('Deseja cadastrar novo usuário? [S/N]: ') == 'n':
            break



def cadastrar_produto():
    while True:
        print(linha())
        print('CADASTRO DE PRODUTO'.center(40))
        print(linha())
        try:
            nome = input('Digite o nome do produto: ')
            valor = float(input('Digite o valor do produto: '))
            descricao = input('Descrição do produto: ')
            valido, msg = operadores.validar_produto(nome, valor, descricao)
            if not valido:
                print(f'⚠️ {msg}')
                continue
            operadores.cadastrar_produtos(nome, valor, descricao)
            print(f'Produto {nome} cadastrado com sucesso!')
            sleep(2)
        except Exception as e:
            print('Erro ao cadastrar Produto! Tente novamente!')
        if pergunta_continuar('Deseja cadastrar novo produto? [S/N]: ') == 'n':
            break

def visualizar_usuarios():
    operadores.visualizar_usuarios()
    input('Pressione ENTER para voltar ao menu...')

def visualizar_produtos():
    operadores.visualizar_produtos()
    input('Pressione ENTER para voltar ao menu...')


def atualizar_usuarios():
    print(linha())
    print('Atualizar Cadastro de Usuários'.center(40))
    print(linha())

    try:
        id_usuario = int(input('ID do Usuário: '))
        nome = input('Novo Nome: ')
        email = input('Novo Email: ')
        idade = int(input('Nova Idade: '))
        operadores.atualizar_usuario(id_usuario, nome, email, idade)
        print('✅ Registro atualizado com sucesso!')
        sleep(1)
    except ValueError:
        print('⚠️ Idade e ID devem ser números!')


def atualizar_produtos():
    print(linha())
    print('Atualizar Cadastro de Produtos'.center(40))
    print(linha())

    try:
        id_produto = int(input('ID do Produto: '))
        nome = input('Novo Nome: ')
        valor = float(input('Novo valor: '))
        descricao = input('Nova Descrição: ')
        operadores.atualizar_produto(id_produto, nome, valor, descricao)
        print('✅ Registro atualizado com sucesso!')
        sleep(1)
    except ValueError:
        print('⚠️ ID e Valor devem ser números.')


def excluir_usuario():
    while True:
        try:
            id_usuario = int(input('Digite o ID do Usuário que deseja apagar: '))
            operadores.excluir_usuario(id_usuario)
        except ValueError:
            print('Digite apenas números inteiros!')
        except Exception as e:
            print(f'Erro ao excluir usuário: {e}')

        if pergunta_continuar('Deseja apagar outro Usuário? [S/N]: ') == 'n':
            break

def excluir_produto():
    while True:
        try:
            id_produto = int(input('Digite o ID do produto que deseja apagar: '))
            operadores.excluir_produto(id_produto)
        except ValueError:
            print('Digite apenas números inteiros!')
        except Exception as e:
            print(f'Erro ao excluir produto: {e}')

        if pergunta_continuar('Deseja apagar outro produto? [S/N]: ') == 'n':
            break