from cliente import Cliente
from conta_corrente import ContaCorrente
from exceptions import SemSaudoError

try:
    ContaCorrente(None, 0, 0)
except TypeError as e:
    print(e)

cliente_1 = Cliente('Cliente 1', 123456789, 'Carpinteiro')
cliente_2 = Cliente('Cliente 2', 123, 'Designer')

cc_cliente_1 = ContaCorrente(cliente_1, 100, 9909)
cc_cliente_2 = ContaCorrente(cliente_2, 101, 9909)

try:
    cc_cliente_1.transferir(100, cc_cliente_2)
    cc_cliente_1.transferir(0, cc_cliente_2)
except ValueError as e:
    print(e)
except SemSaudoError as e:
    print(e)
else:
    print('Este código só será executado se não houver excessões no bloco try')
finally:
    print('Este código sempre será executado')
    print(cc_cliente_1.saldo)
