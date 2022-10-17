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
    # dar erro indo de Oradea para Vaslui
    problema = Problema(dados.getEstados(), dados.estados[0], transicao.listaDeAdjacencia, dados.estados[12], 0)
    busca = Busca()

    no = busca.buscaEmLargura(problema)

    '''
        imprime o caminho
        caminho = Bucharest -> Pitesti -> Craiova -> Drobeta -> Mehadia -> Lugoj -> Timisoara -> Arad
    '''
    if not no:
        print("sem caminho")
    else:
        while no.pai is not None:
            print(f"Estado: {no.estado}, Peso: {no.custo}")
            no = no.pai