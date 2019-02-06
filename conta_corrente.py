from cliente import Cliente
from exceptions import SemSaudoError, OperacaoFinanceiraError


class ContaCorrente:
    total_contas_criadas = 0
    transferencias_nao_permitidas = 0
    def __init__(self, cliente, agencia, numero):
        if not isinstance(cliente, Cliente):
            raise TypeError('O titular deve ser do tipo Cliente')
        
        if agencia  <= 0:
            raise ValueError(f'O argumento agencia deve ser maior que 0.", {agencia}')
        
        if numero  <= 0:
            raise ValueError(f'O argumento numero deve ser maior que 0.", {agencia}')
        
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero
        ContaCorrente.total_contas_criadas += 1

    def transferir(self, valor, favorecido):
        if not isinstance(favorecido, ContaCorrente):
            raise TypeError('O favorecido deve ser um objeto do tipo ContaCorrente')
        try:
            self.sacar(valor)
        except SemSaudoError as E:
            ContaCorrente.transferencias_nao_permitidas += 1
            raise OperacaoFinanceiraError('Operação não realizada: ', E)

        favorecido.depositar(valor)
    
    def sacar(self, valor):
        if valor <0:
            raise ValueError('O valor de saque não pode ser negativo')
        if (self.saldo - valor) < 0:
            raise SemSaudoError
        
        self.saldo -= valor

    def depositar(self, valor):
        if valor <0:
            raise ValueError('O valor depositado não pode ser negativo')
        
        self.saldo += valor
