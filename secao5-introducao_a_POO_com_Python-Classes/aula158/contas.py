from abc import ABC, abstractmethod


class Conta (ABC):
    def __init__(self, agencia, conta, saldo=0.00):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor): ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')

    def detalhes(self, msg):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')
        print('--')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0.00:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print(f'Não foi possível sacar {valor}')
        print('Seu limite é 0.00')
        self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0.00, limite=0.00):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print(f'Não foi possível sacar {valor}')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')


if __name__ == '__main__':
    cp1 = ContaPoupanca(123, 321)
    cp1.sacar(1)
    cp1.depositar(1)
    cp1.sacar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(123, 321, 0.00, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(100)
