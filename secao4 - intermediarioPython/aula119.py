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


def listar(tarefas):
    print()
    if not tarefas:
        print('Nada a listar')
        print()
        return

    print("TAREFAS:")
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nada a desfazer')
        print()
        return

    tarefa = tarefas.pop()
    print(f'{tarefa} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nada a refazer')
        print()
        return

    tarefa_refeita = tarefas_refazer.pop()
    print(f'{tarefa} adicionada à lista de tarefas.')
    tarefas.append(tarefa_refeita)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    tarefas.append(tarefa)
    listar(tarefas)
    return f'\n Tarefa incluída! \n'


tarefas_refazer = []
tarefas = []

while True:
    tarefa = input(
        'Comandos: limpar, listar, desfazer ou refazer  \n'
        'Digite uma tarefa ou comando: '
    )

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'limpar': lambda: limpar_tela(),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(
        tarefa) is not None else comandos['adicionar']
    comando()

    # if tarefa.lower() == 'limpar':
    #     limpar_tela()

    # elif tarefa.lower() == 'listar':
    #     listar(tarefas)

    # elif tarefa.lower() == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)

    # elif tarefa.lower() == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)

    # else:
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
