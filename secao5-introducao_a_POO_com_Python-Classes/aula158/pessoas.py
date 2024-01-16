from abc import ABC, abstractmethod
from contas import ContaCorrente, ContaPoupanca


class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    @abstractmethod
    def nome(self): ...

    @nome.setter
    @abstractmethod
    def nome(self, valor): ...

    @property
    @abstractmethod
    def idade(self): ...

    @idade.setter
    @abstractmethod
    def idade(self, valor):
        self._idade = valor


class Cliente(Pessoa):
    def __init__(
        self, nome: str, idade: int,
        conta_poupanca: ContaPoupanca, conta_corrente: ContaCorrente
    ) -> None:
        super().__init__(nome, idade)
        self.conta_poupanca = conta_poupanca
        self.conta_corrente = conta_corrente

    @Pessoa.nome.setter
    def nome(self, valor):
        self.nome = valor


if __name__ == '__main__':
    c1 = Cliente('Renan', 31, (123, 123, 10), (321, 321, 10, 10))
