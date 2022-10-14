from Problema import Problema
from No import No
import heapq

class Busca:
    def __init__(self):
        self.borda = []         # guarda os nós que ainda não foram explorados
        self.explorados = []    # guarda os nós que já foram explorados

    def buscaEmLargura(self, problema : Problema):
        self.borda.append(problema.estadoInicial)
        root = No(problema.estadoInicial, None, 0)

        while True:
            if len(self.borda) == 0:
                return None

            a = self.borda.pop()
            no = No(a, root, 0)
            self.explorados.append(no)

            for child in problema.transicoes[no.estado]:
                filho = No(child[0], no, 0)

                if filho.estado not in self.explorados and filho not in self.borda:
                    if filho.estado == problema.estadoFinal:
                        return filho
                    self.borda.append(filho.estado)
                    root = filho.pai

    def buscaCustoUniforme(self, problema : Problema):
        self.borda.append(problema.estadoInicial)
        root = No(problema.estadoInicial, None, 0)

        while True:
            if len(self.borda) == 0:
                return None
            
            no = No(self.borda.pop(), root, 0)

            if no.estado == problema.estadoFinal:
                return no

            self.explorados.append(no.estado)

            for child in problema.transicoes[no.estado]:
                filho = No(child[0], no, 0)

                if filho.estado not in self.explorados and filho not in self.borda:
                    self.borda.append(filho)
