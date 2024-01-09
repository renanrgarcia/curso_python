"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Minha solução
# if len(lista_a) > len(lista_b):
#     for i in range(len(lista_b)):
#         lista_soma.append(lista_a[i] + lista_b[i])
# else:
#     for i in range(len(lista_a)):
#         lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# Minha solução otimizada
# lista_soma = [
#     lista_a[i] + lista_b[i]
#     for i in range(min(len(lista_a), len(lista_b)))
# ]

# print(lista_soma)

# Solução 1 
# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# Solução 2
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)