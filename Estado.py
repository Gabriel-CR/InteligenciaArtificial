class Estado:
    def __init__(self, nome : str):
        self.nome = nome

    def getNome(self):
        return self.nome

    def __str__(self):
        return self.nome