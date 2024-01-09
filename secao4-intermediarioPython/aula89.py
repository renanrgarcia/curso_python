# dir(usado no debugger), hasattr e getattr em Python
string = 'Luiz'
metodo = 'lower'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)