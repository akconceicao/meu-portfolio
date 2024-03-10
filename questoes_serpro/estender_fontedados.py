class FonteDeDados:
    def __init__(self, endereco):
        raise NotImplementedError()

    def proximoDado(self):
        raise NotImplementedError()

    def possuiDados(self):
        raise NotImplementedError()


class FonteArquivo(FonteDeDados):
    def __init__(self, endereco):
        self.endereco = endereco
        self.arquivo = None

        try:
            self.arquivo = open(self.endereco, 'r')
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")

    def proximoDado(self):
        if self.arquivo:
            linha = self.arquivo.readline()
            if linha:
                return linha.strip()
            else:
                self.arquivo.close()
                return None
        else:
            return None

    def possuiDados(self):
        if self.arquivo:
            linha = self.arquivo.readline()
            if linha:
                return True
            else:
                self.arquivo.close()
                return False
        else:
            return False


# Exemplo de uso:
endereco_arquivo = 'C:\\Java Projects\\legordin.txt'
fonte = FonteArquivo(endereco_arquivo)

while fonte.possuiDados():
    dado = fonte.proximoDado()
    if dado is not None:
        print(dado)
