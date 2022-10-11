from Dados import Data
from No import No
from Transicao import Transicao
from Problema import Problema
from Busca import Busca
from Mapa import Mapa

if __name__ == "__main__":
    dados = Data()
    transicao = Transicao(dados.dicionario)

    # indo de Arad para Bucharest
    problema = Problema(dados.getEstados(), dados.estados[2], transicao.listaDeAdjacencia, dados.estados[12], 0)
    busca = Busca()

    no = busca.buscaEmLargura(problema)

    '''
        imprime o caminho
        caminho = Bucharest -> Pitesti -> Craiova -> Drobeta -> Mehadia -> Lugoj -> Timisoara -> Arad
    '''
    while no is not None:
        print(no.estado)
        no = no.pai