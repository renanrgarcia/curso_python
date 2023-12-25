# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 1, 2, 3, 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ] # 2
]

# p, b, *_, ap, u = lista
# print(p, ap, u)

# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')