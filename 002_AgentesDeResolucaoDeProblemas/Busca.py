from Problema import Problema
from No import No

class Busca:
    def __init__(self):
        self.borda = []
        self.explorados = []

    def buscaEmLargura(self, problema : Problema):
        self.borda.append(problema.estadoInicial)

        while True:
            if len(self.borda) == 0:
                return None

            a = self.borda.pop()
            no = No(a, None, 0)
            self.explorados.append(no.estado)

            for child in problema.transicoes[no.estado]:
                filho = No(child[0], no, 0)

                if filho.estado not in self.explorados and filho not in self.borda:
                    print(filho, '\n')

                    if filho.estado == problema.estadoFinal:
                        return filho
                    self.borda.append(filho.estado)