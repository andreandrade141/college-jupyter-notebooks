from A_star import AEstrela
from Grafo_A import Grafo

grafo = Grafo()

busca = AEstrela(grafo.bucharest)
busca.buscar(grafo.oradea)
