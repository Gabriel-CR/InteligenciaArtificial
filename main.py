from Dados import Data
from No import No
from Transicao import Transicao
from Problema import Problema

if __name__ == "__main__":
    dados = Data()
    transicao = Transicao(dados.dicionario)

    problema = Problema(dados.getEstados(), dados.estados[0], transicao.listaDeAdjacencia, dados.estados[12], 0)

    transicao = Transicao(problema.transicoes)

    print(problema)
    