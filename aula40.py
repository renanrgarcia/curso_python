""" Calculadora com while """


print('Bem-vindo à calculadora!')
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Qual operação deseja fazer? (/*+-): ')
    num1_float = 0
    num2_float = 0
    numeros_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    operadores_permitidos = '/*+-'

    if operador not in operadores_permitidos:
        print('Operador digitado inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Confira o resultado abaixo:')
    if operador == '+':
        print(f'{num1_float}+{num2_float} =', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float}-{num2_float} =', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float}*{num2_float} =', num1_float * num2_float)
    elif operador == '/':
        print(f'{num1_float}/{num2_float} =', num1_float / num2_float)

    sair = input('Você quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break