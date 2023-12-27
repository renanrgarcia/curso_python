# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicar(1, 2, 3, 4, 5)
print(resultado)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.


def par_impar(numero):
    if numero % 2 == 0:
        return f'Número {numero} é par'
    return f'Número {numero} é ímpar'


tipo = par_impar(2)
print(par_impar(2))
