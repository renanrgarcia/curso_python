"""
Iterando strings com while
"""
nome = 'Renan Garcia'
indice = 0
nova_str = ''

while indice < len(nome):
    letra = nome[indice]
    nova_str += f'*{letra}'
    indice += 1

print(nova_str)