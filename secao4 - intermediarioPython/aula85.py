lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))
lista = [
    [(x, letra) for letra in 'Renan']
    for x in range(3)
]

# print(lista)

# Aula YouTube
# 1. Utilização
# def divisaoFn(x, y):
#     return x / y


# def multiplicacaoFn(x, y):
#     return x * y


# def potenciacaoFn(x, y):
#     return x ** y


# numeros = [1, 2, 3, 4, 5]
# # novos_numeros = []
# # for numero in numeros:
# #     novos_numeros.append(numero)

# divisao = [divisaoFn(numero, 2) for numero in numeros]
# multiplicacao = [multiplicacaoFn(numero , 2) for numero in numeros]
# quadrado = [potenciacaoFn(numero, 2) for numero in numeros]

# print(numeros)
# print(divisao)
# print(multiplicacao)
# print(quadrado)

# 2. Condicionais
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# novos_numeros = [numero for numero in numeros if numero > 5]
# impares = [numero for numero in numeros if numero % 2 != 0]
# pares = [numero for numero in numeros if numero % 2 == 0]
# outro_if = [
#     numero
#     if numero != 6 else 600
#     for numero in pares
# ]

# print(numeros)
# print(novos_numeros)
# print(impares)
# print(pares)
# print(outro_if)

# 3. Linhas e colunas
# linhas_e_colunas = [
#     (x, y)
#     if y != 2 else (x, y * 1000)
#     for x in range(1,11)
#     for y in range(1, 6)
#     if x != 2
# ]

# print(linhas_e_colunas)

# 4. Strings
# string = 'Renan Garcia'
# numero_de_letras = 2
# nova_string = '.'.join([
#     string[indice:indice + numero_de_letras] 
#     for indice in range(0, (len(string)), numero_de_letras)
# ])
# print(nova_string)

# 5. Listas
# nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
# novos_nomes = [
#     f'{nome[:-1].lower()}{nome[-1].upper()}'
#     for nome in nomes
# ]
# print(novos_nomes)

# 6. FlatMap
numeros = [
    [numero, numero ** 2]
    for numero in range(10)
]
flat = [
    y
    for x in numeros
    for y in x
]
print(numeros)
print(flat)

