from Estado import Estado as est

class Data:
    def __init__(self):
        self.dicionario = {}
        self.estados = []

        self.estados.append(est("Oradea"))          # 0
        self.estados.append(est("Zerind"))          # 1
        self.estados.append(est("Arad"))            # 2
        self.estados.append(est("Sibiu"))           # 3
        self.estados.append(est("Timisoara"))       # 4
        self.estados.append(est("Lugoj"))           # 5
        self.estados.append(est("Mehadia"))         # 6
        self.estados.append(est("Drobeta"))         # 7
        self.estados.append(est("Fagaras"))         # 8
        self.estados.append(est("Rimmieu Vilcea"))  # 9
        self.estados.append(est("Craiova"))         # 10
        self.estados.append(est("Pitesti"))         # 11
        self.estados.append(est("Bucharest"))       # 12
        self.estados.append(est("Urziceni"))        # 13
        self.estados.append(est("Hirsova"))         # 14
        self.estados.append(est("Eforie"))          # 15
        self.estados.append(est("Vaslui"))          # 16
        self.estados.append(est("Iasi"))            # 17
        self.estados.append(est("Neamt"))           # 18
        self.estados.append(est("Giurgi"))          # 19

        self.dicionario[self.estados[0]] = {
            "nome": "Oradea",
            "vizinhos": [self.estados[1], self.estados[3]],
            "distancias": [71, 151]
        }

    '''def popularEstados(self):
        self.estados.append(est("Oradea"))          # 0
        self.estados.append(est("Zerind"))          # 1
        self.estados.append(est("Arad"))            # 2
        self.estados.append(est("Sibiu"))           # 3
        self.estados.append(est("Timisoara"))       # 4
        self.estados.append(est("Lugoj"))           # 5
        self.estados.append(est("Mehadia"))         # 6
        self.estados.append(est("Drobeta"))         # 7
        self.estados.append(est("Fagaras"))         # 8
        self.estados.append(est("Rimmieu Vilcea"))  # 9
        self.estados.append(est("Craiova"))         # 10
        self.estados.append(est("Pitesti"))         # 11
        self.estados.append(est("Bucharest"))       # 12
        self.estados.append(est("Urziceni"))        # 13
        self.estados.append(est("Hirsova"))         # 14
        self.estados.append(est("Eforie"))          # 15
        self.estados.append(est("Vaslui"))          # 16
        self.estados.append(est("Iasi"))            # 17
        self.estados.append(est("Neamt"))           # 18
        self.estados.append(est("Giurgi"))          # 19

    def popularDicionario(self):
        

        self.dicionario = {
            self.estados[0] : {
                {'nome' : self.estados[1], 'peso' : 71},
                {'nome' : self.estados[3], 'peso' : 151}
            },
            self.estados[1] : {
                {'nome' : self.estados[0], 'peso' : 71},
                {'nome' : self.estados[2], 'peso' : 75}
            },
            self.estados[2] : {
                {'nome' : self.estados[1], 'peso' : 75},
                {'nome' : self.estados[3], 'peso' : 140},
                {'nome' : self.estados[4], 'peso' : 118}
            },
            self.estados[3] : {
                {'nome' : self.estados[0], 'peso' : 151},
                {'nome' : self.estados[2], 'peso' : 140},
                {'nome' : self.estados[8], 'peso' : 99},
                {'nome' : self.estados[9], 'peso' : 80}
            },
            self.estados[4] : {
                {'nome' : self.estados[2], 'peso' : 118},
                {'nome' : self.estados[5], 'peso' : 111}
            },
            self.estados[5] : {
                {'nome' : self.estados[4], 'peso' : 111},
                {'nome' : self.estados[6], 'peso' : 70}
            },
            self.estados[6] : {
                {'nome' : self.estados[5], 'peso' : 70},
                {'nome' : self.estados[7], 'peso' : 75}
            },
            self.estados[7] : {
                {'nome' : self.estados[6], 'peso' : 75},
                {'nome' : self.estados[10], 'peso' : 120}
            },
            self.estados[8] : {
                {'nome' : self.estados[3], 'peso' : 99},
                {'nome' : self.estados[12], 'peso' : 211}
            },
            self.estados[9] : {
                {'nome' : self.estados[3], 'peso' : 80},
                {'nome' : self.estados[11], 'peso' : 97},
                {'nome' : self.estados[10], 'peso' : 146}
            },
            self.estados[10] : {
                {'nome' : self.estados[7], 'peso' : 120},
                {'nome' : self.estados[9], 'peso' : 146},
                {'nome' : self.estados[11], 'peso' : 138}
            },
            self.estados[11] : {
                {'nome' : self.estados[9], 'peso' : 97},
                {'nome' : self.estados[10], 'peso' : 138},
                {'nome' : self.estados[12], 'peso' : 101}
            },
            self.estados[19] : {
                {'nome' : self.estados[12], 'peso' : 90}
            },
            self.estados[12] : {
                {'nome' : self.estados[8], 'peso' : 211},
                {'nome' : self.estados[11], 'peso' : 101},
                {'nome' : self.estados[13], 'peso' : 85},
                {'nome' : self.estados[19], 'peso' : 90}
            },
            self.estados[13] : {
                {'nome' : self.estados[12], 'peso' : 85},
                {'nome' : self.estados[14], 'peso' : 98},
                {'nome' : self.estados[16], 'peso' : 142}
            },
            self.estados[14] : {
                {'nome' : self.estados[13], 'peso' : 98},
                {'nome' : self.estados[15], 'peso' : 86}
            },
            self.estados[15] : {
                {'nome' : self.estados[14], 'peso' : 86}
            },
            self.estados[16] : {
                {'nome' : self.estados[13], 'peso' : 142},
                {'nome' : self.estados[17], 'peso' : 92}
            },
            self.estados[17] : {
                {'nome' : self.estados[16], 'peso' : 92},
                {'nome' : self.estados[18], 'peso' : 87}
            },
            self.estados[18] : {
                {'nome' : self.estados[17], 'peso' : 87}
            }
        }'''


    def getEstados(self):
        return self.estados

    def getDicionario(self):
        return self.dicionario

    def __str__(self):
        os = ""
        os += self.dicionario[self.estados[0]]["nome"] + " -> "

        for i in range(len(self.dicionario[self.estados[0]]["vizinhos"])):
            os += self.dicionario[self.estados[0]]["vizinhos"][i].getNome() + ":" + str(self.dicionario[self.estados[0]]["distancias"][i]) + " "

        return os