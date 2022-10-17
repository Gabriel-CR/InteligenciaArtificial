from Estado import Estado as est

class Data:
    def __init__(self):
        self.dicionario = {}
        self.estados = []
        self.heuristica = {}

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
        self.estados.append(est("Giurgiu"))         # 19

        self.dicionario = {
            self.estados[0] : [
                (self.estados[1], 71), (self.estados[3], 151)
            ],
            self.estados[1] : [
                (self.estados[0], 71), (self.estados[2], 75)
            ],
            self.estados[2] : [
                (self.estados[1], 75), (self.estados[3], 140), (self.estados[4], 118)
            ],
            self.estados[3] : [
                (self.estados[0], 151), (self.estados[2], 140), (self.estados[8], 99), (self.estados[9], 80)
            ],
            self.estados[4] : [
                (self.estados[2], 118), (self.estados[5], 111)
            ],
            self.estados[5] : [
                (self.estados[4], 111), (self.estados[6], 70)
            ],
            self.estados[6] : [
                (self.estados[5], 70), (self.estados[7], 75)
            ],
            self.estados[7] : [
                (self.estados[6], 75), (self.estados[10], 120)
            ],
            self.estados[8] : [
                (self.estados[3], 99), (self.estados[12], 211)
            ],
            self.estados[9] : [
                (self.estados[3], 80), (self.estados[10], 146), (self.estados[11], 97)
            ],
            self.estados[10] : [
                (self.estados[7], 120), (self.estados[9], 146), (self.estados[11], 138)
            ],
            self.estados[11] : [
                (self.estados[9], 97), (self.estados[10], 138), (self.estados[12], 101)
            ],
            self.estados[12] : [
                (self.estados[8], 211), (self.estados[11], 101), (self.estados[13], 85), (self.estados[19], 90)
            ],
            self.estados[13] : [
                (self.estados[12], 85), (self.estados[14], 98), (self.estados[16], 142)
            ],
            self.estados[14] : [
                (self.estados[13], 98), (self.estados[15], 86)
            ],
            self.estados[15] : [
                (self.estados[14], 86)
            ],
            self.estados[16] : [
                (self.estados[13], 142), (self.estados[17], 92)
            ],
            self.estados[17] : [
                (self.estados[16], 92), (self.estados[18], 87)
            ],
            self.estados[18] : [
                (self.estados[17], 87)
            ],
            self.estados[19] : [
                (self.estados[12], 90)
            ]
        }

        self.heuristica = {
            self.estados[0] : 380,
            self.estados[1] : 374, 
            self.estados[2] : 366,
            self.estados[3] : 253,
            self.estados[4] : 329,
            self.estados[5] : 244,
            self.estados[6] : 241,
            self.estados[7] : 242,
            self.estados[8] : 176,
            self.estados[9] : 193,
            self.estados[10] : 160,
            self.estados[11] : 100,
            self.estados[12] : 0,
            self.estados[13] : 80,
            self.estados[14] : 151,
            self.estados[15] : 161,
            self.estados[16] : 199,
            self.estados[17] : 226,
            self.estados[18] : 234,
            self.estados[19] : 77
        }

    def __str__(self):
        os = ""

        for a in self.heuristica:
            os += f"{a.nome} -> {self.heuristica[a]} \n"

        return os 