class Transicao:
    def __init__(self, dicionario):
        self.listaDeAdjacencia = dicionario

    def __str__(self):
        os = ""

        for dd in self.listaDeAdjacencia:
            os += dd.nome + " ->"
            for d in self.listaDeAdjacencia[dd]:
                os += f"{d[0].nome} = {d[1]}km, "
            os += "\n"

        return os