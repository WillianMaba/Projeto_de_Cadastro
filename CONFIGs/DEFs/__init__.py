from time import sleep
from CONFIGs.Interface import *
from Database import operadores
from Database.operadores import visualizar_usuarios, visualizar_produtos, atualizar_usuario, atualizar_produto, \
    excluir_usuario, excluir_produto


def menu():
    while True:
        print(linha)
        print('Sistema de Cadastro'.center(40))
        print(linha)
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

        if opcao == 1:
            Cadastrar_Usuário()
        elif opcao == 2:
            Cadastrar_Produto()
        elif opcao == 3:
            visualizar_usuarios()
        elif opcao == 4:
            visualizar_produtos()
        elif opcao == 5:
            atualizar_usuario()
        elif opcao == 6:
            atualizar_produto()
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


def Cadastrar_Usuário():
    while True:
        print(linha)
        print('CADASTRO DE USUÁRIO'.center(40))
        print(linha)
        try:
            ID = int(input('Escolha a ID do usuário: '))
            nome = input('Digite o nome do usuário: ')
            email = input('Digite o email do usuário: ')
            idade = int(input('Digite sua idade: '))
            operadores.cadastrar_usuarios(nome, email, idade)
            print(f'Usuário {nome} cadastrado com sucesso!')
            sleep(2)
        except Exception as e:
            print('Erro ao cadastrar usuário! Tente novamente!')
        if pergunta_continuar('Deseja cadastrar novo usuário? [S/N]: ') == 'n':
            break



def Cadastrar_Produto():
    while True:
        print(linha)
        print('CADASTRO DE PRODUTO'.center(40))
        print(linha)
        try:
            ID = int(input('Escolha a ID do produto: '))
            nome = input('Digite o nome do usuário: ')
            valor = float(input('Digite o valor do produto: '))
            descricao = input('Descrição do produto: ')
            operadores.cadastrar_produtos(nome, valor, descricao)
            print(f'Produto {nome} cadastrado com sucesso!')
            sleep(2)
        except Exception as e:
            print('Erro ao cadastrar Produto! Tente novamente!')
        if pergunta_continuar('Deseja cadastrar novo usuário? [S/N]: ') == 'n':
            break

def visualizar_usuarios():
    operadores.visualizar_usuarios()
    input('Pressione ENTER para voltar ao menu...')

def visualizar_produtos():
    operadores.visualizar_produtos()
    input('Pressione ENTER para voltar ao menu...')


def  atualizar_usuario():


def atualizar_produto():


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