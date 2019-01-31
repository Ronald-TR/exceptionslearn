class LeitorDeArquivo:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        print(f'Abrindo arquivo: {self.arquivo}')
    
    def ler_proxima_linha(self):
        print('Lendo linha...')
        raise IOError()
        return 'Linha de arquivo'

    def dispose(self):
        print('Fechando arquivo.')
