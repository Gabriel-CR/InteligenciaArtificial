from time import sleep
from Problema import Problema
from No import No
import heapq

class Busca:
    def __init__(self):
        self.borda = []         # guarda os nós que ainda não foram explorados
        self.explorados = []    # guarda os nós que já foram explorados

    def findPesoEstado(self, lista, estado):
        for i in range(len(lista)):
            if lista[i][0] == estado:
                return i

    def buscaEmLargura(self, problema: Problema):
        self.borda.append(problema.estadoInicial)
        root = No(problema.estadoInicial, None, 0)

        while True:
            if len(self.borda) == 0:
                return None

            a = self.borda.pop()
            indice = self.findPesoEstado(problema.transicoes[root.estado], a)

            no = No(a, root, root.custo + (0 if (indice == None) else problema.transicoes[root.estado][indice][1]))
            self.explorados.append(no)

            for child in problema.transicoes[no.estado]:
                filho = No(child[0], no, no.custo + child[1])
                # print(filho.estado)

                if (filho.estado not in self.explorados) and (filho not in self.borda):
                    if filho.estado == problema.estadoFinal:
                        return filho
                    self.borda.append(filho.estado)
                    root = filho.pai