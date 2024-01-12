# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, mutiplicador):
        self._mutiplicador = mutiplicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._mutiplicador
        return interno


@Multiplicar(2)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
