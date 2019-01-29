class SemSaudoError(Exception):
    def __str__(self):
        return 'Saudo insuficiente para efetuar a transação'

class SemPermissaoError(Exception):
    def __str__(self):
        return 'O cliente não possui permissão para esta ação'
