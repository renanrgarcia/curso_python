# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Renan'
pessoa['sobrenome'] = 'Reis Garcia'

print(pessoa[chave])

pessoa[chave] = 'Thaís'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('Não EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')