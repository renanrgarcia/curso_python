"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}.')
# else:
#     print(f'O texto digitado não é um número inteiro.')

# entrada = input('Digite um número: ')

# try:
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'
#     if par_impar:
#         par_impar_texto = 'par'
#     print(f'O número {entrada_int} é {par_impar_texto}.')
# except:
#     print(f'O texto digitado não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Que horas são em números inteiros? ')

# if entrada.isdigit():
#     horario_int = int(entrada)
#     if horario_int >= 0 and horario_int <= 11:
#         print('Bom dia')
#     elif horario_int >= 12 and horario_int <= 17:
#         print('Boa tarde')
#     elif horario_int >= 18 and horario_int <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora.')
# else:
#     print('Você não digitou um horário válido.')

# entrada = input('Que horas são em números inteiros? ')

# try:
#     horario_int = int(entrada)
#     if horario_int >= 0 and horario_int <= 11:
#         print('Bom dia')
#     elif horario_int >= 12 and horario_int <= 17:
#         print('Boa tarde')
#     elif horario_int >= 18 and horario_int <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora.')
# except:
#     print('Você não digitou um horário válido.')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

entrada = input('Qual seu primeiro nome? ')
tamanho_nome = len(entrada)

if tamanho_nome >= 1:
    if tamanho_nome < 5:
        print('Seu nome é curto.')
    elif tamanho_nome < 7:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Por favor digite algo.')
