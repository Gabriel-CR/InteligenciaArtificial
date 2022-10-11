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

    '''
    def buscaCustoUniforme(self, problema : Problema):
        self.borda.append(problema.estadoInicial)

        while True:
            if len(self.borda) == 0:
                return None

            no = No(self.borda.pop(0), None, 0)

            if no.estado == problema.estadoFinal:
                return no

            self.explorados.append(no.estado)

            for filho in problema.transicoes[no.estado]:
                filho = No(filho[0], no, filho[1] + no.custoCaminho)
                if filho.estado not in self.explorados and filho not in self.borda:
                    self.borda.append(filho)
    '''