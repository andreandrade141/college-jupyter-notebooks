from VetorOrd import Vetor_Ordenado


class Busca_Gulosa:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('-----------------')
        print('Atual: {}'.format(atual.rotulo))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
            print('Objetivo: {}'.format(atual.rotulo))
            return
        else:
            vetor = Vetor_Ordenado(len(atual.adjacentes))

            for adjacente in atual.adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado == True
                    vetor.insere(adjacente.vertice)
            vetor.imprime()

        if vetor.valores[0] != None:
            self.buscar(vetor.valores[0])
