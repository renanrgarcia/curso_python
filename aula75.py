# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def multiplicar(base):
    def multiplicacao_por(numero):
        return base * numero
    return multiplicacao_por

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

numero = int(input('Digite um número que queira multiplicar: '))
base = input('Digite em quantas vezes quer multiplicar o número: ')

if base == '2':
    print(duplicar(numero))
elif base == '3':
    print(triplicar(numero))
elif base == '4':
    print(quadruplicar(numero))