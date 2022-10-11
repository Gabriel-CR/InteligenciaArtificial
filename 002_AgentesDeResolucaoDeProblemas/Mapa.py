class Mapa:
    def __init__(self, cidades):
        self.cidades = cidades

    def __str__(self):
        os = ""

        for dd in self.cidades:
            os += dd.nome + " ->"
            for d in self.cidades[dd]:
                os += f"{d[0].nome} = {d[1]}km, "
            os += "\n"

        return os