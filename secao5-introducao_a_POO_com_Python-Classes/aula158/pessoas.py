from abc import ABC
import contas


class Pessoa(ABC):
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade
        self.conta = contas.Conta

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor


class Cliente(Pessoa):
    ...
