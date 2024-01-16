import pessoas
import contas


class Banco():
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[contas.Conta] | None = None,
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True

    def autenticar(self, cliente: pessoas.Cliente, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cliente1 = pessoas.Cliente('Renan', 31)
    cc1 = contas.ContaCorrente(123, 123, 0.00, 100.00)
    cliente1.conta = cc1

    cliente2 = pessoas.Cliente('Thaís', 31)
    cp1 = contas.ContaPoupanca(321, 321, 0.00)
    cliente2.conta = cp1

    banco = Banco()
    banco.clientes.extend([cliente1, cliente2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([123, 321])
    print(banco)
    print()

    if banco.autenticar(cliente1, cc1):
        cc1.depositar(1000)
        print(cliente1.conta)
