import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(
        self, nome: str, idade: int
    ) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    cliente1 = Cliente('Renan', 31)
    cc1 = contas.ContaCorrente(123, 123, 0.00, 100.00)
    cliente1.conta = cc1
    print(cliente1)
    print(cliente1.conta)

    cliente2 = Cliente('Thaís', 31)
    cp1 = contas.ContaPoupanca(321, 321, 0.00)
    cliente2.conta = cp1
    print(cliente2)
    print(cliente2.conta)
