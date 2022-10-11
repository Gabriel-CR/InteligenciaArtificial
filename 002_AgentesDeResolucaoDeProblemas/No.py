class No:
    def __init__(self, estado=None, pai=None, custo=0):
        self.estado = estado
        self.pai = pai
        self.custo = custo

    def __str__(self):
        return f"Estado: {self.estado} \nCusto: {self.custo} \nPai: {self.pai.estado.nome if self.pai else 'None'}"