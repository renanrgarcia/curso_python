# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os


def limpar_tela():
    return os.system('cls' if os.name == 'nt' else 'clear')


def


def listar(lista=None):
    if lista == None:
        print('Nada a listar')
    return


def desfazer(lista=None):
    if lista == None:
        print('Nada a listar')
    return


def refazer(lista=None):
    if lista == None:
        print('Nada a listar')
    return


resposta = input('Comandos: listar, desfazer, refazer ou limpar: ')

if resposta.lower() == 'limpar':
    limpar_tela()

if resposta.lower() == 'listar':
    listar()
