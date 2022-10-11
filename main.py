from Dados import Data
from No import No
from Transicao import Transicao
from Problema import Problema
from Busca import Busca

if __name__ == "__main__":
    dados = Data()
    transicao = Transicao(dados.dicionario)

    # indo de Oradea para Giurgiu
    problema = Problema(dados.getEstados(), dados.estados[0], transicao.listaDeAdjacencia, dados.estados[19], 0)
    busca = Busca()


    no = busca.buscaEmLargura(problema)

    # imprime o caminho
    # caminho = Giurgiu -> Bucharest -> Pitesti -> Rimmieu Vilcea -> Sibiu -> Oradea
    while no is not None:
        print(no.estado.nome)
        no = no.pai
