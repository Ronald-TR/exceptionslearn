from exceptions import SemSaudoError

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao


class ContaCorrente:

    def __init__(self, cliente, agencia, numero):
        assert (type(cliente) is Cliente), 'O titular deve ser do tipo Cliente'
        
        self.saldo = 100
        self.cliente = cliente
        self.agencia = agencia
        self.numero = numero

    def transferir(self, valor, favorecido):
        if not type(favorecido) is ContaCorrente:
            raise TypeError('O favorecido deve ser um objeto do tipo ContaCorrente')
        
        self.sacar(valor)
        favorecido.depositar(valor)
        return self
    
    def sacar(self, valor):
        if valor <0: raise ValueError('O valor de saque não pode ser negativo')
        if (self.saldo - valor) < 0: raise SemSaudoError
        
        self.saldo -= valor
        return self

    def depositar(self, valor):
        if valor <0: raise ValueError('O valor depositado não pode ser negativo')
        self.saldo += valor
        return self
