

class Vertice:

    def __init__(self, Rotulo, Distobjetivo):
        self.rotulo = Rotulo
        self.visitado = False
        self.distobj = Distobjetivo
        self.adjacentes = []

    def AddAdjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def MostraAdjacente(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:

    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.Astar = vertice.distobj + self.custo


class Grafo:

    # Cidades

    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    arad.AddAdjacente(Adjacente(zerind, 75))
    arad.AddAdjacente(Adjacente(sibiu, 140))
    arad.AddAdjacente(Adjacente(timisoara, 110))

    zerind.AddAdjacente(Adjacente(oradea, 71))
    zerind.AddAdjacente(Adjacente(arad, 75))

    oradea.AddAdjacente(Adjacente(zerind, 71))
    oradea.AddAdjacente(Adjacente(sibiu, 151))

    sibiu.AddAdjacente(Adjacente(oradea, 151))
    sibiu.AddAdjacente(Adjacente(arad, 140))
    sibiu.AddAdjacente(Adjacente(fagaras, 99))
    sibiu.AddAdjacente(Adjacente(rimnicu, 80))

    timisoara.AddAdjacente(Adjacente(arad, 118))
    timisoara.AddAdjacente(Adjacente(lugoj, 111))

    lugoj.AddAdjacente(Adjacente(timisoara, 111))
    lugoj.AddAdjacente(Adjacente(mehadia, 70))

    mehadia.AddAdjacente(Adjacente(lugoj, 70))
    mehadia.AddAdjacente(Adjacente(dobreta, 75))

    dobreta.AddAdjacente(Adjacente(mehadia, 75))
    dobreta.AddAdjacente(Adjacente(craiova, 120))

    craiova.AddAdjacente(Adjacente(dobreta, 120))
    craiova.AddAdjacente(Adjacente(pitesti, 138))
    craiova.AddAdjacente(Adjacente(rimnicu, 146))

    rimnicu.AddAdjacente(Adjacente(craiova, 146))
    rimnicu.AddAdjacente(Adjacente(sibiu, 80))
    rimnicu.AddAdjacente(Adjacente(pitesti, 97))

    fagaras.AddAdjacente(Adjacente(sibiu, 99))
    fagaras.AddAdjacente(Adjacente(bucharest, 211))

    pitesti.AddAdjacente(Adjacente(rimnicu, 97))
    pitesti.AddAdjacente(Adjacente(craiova, 138))
    pitesti.AddAdjacente(Adjacente(bucharest, 101))

    bucharest.AddAdjacente(Adjacente(fagaras, 211))
    bucharest.AddAdjacente(Adjacente(pitesti, 101))
    bucharest.AddAdjacente(Adjacente(giurgiu, 90))


grafo = Grafo()
