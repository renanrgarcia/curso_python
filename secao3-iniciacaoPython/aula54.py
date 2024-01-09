"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista = []

while True:

    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao.lower() == 'i':
       os.system('cls')
       valor = input("Valor: ")
       lista.append(valor)

    elif opcao.lower() == 'a':
        indice_str = input('Digite um índice para apagar: ')
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')

    elif opcao.lower() == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Nada para listar.')
        
        for indice, valor in enumerate(lista):
                print(indice, valor)
    else:
        print('Por favor, escolha i, a ou l.')