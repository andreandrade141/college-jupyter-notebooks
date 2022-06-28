import os
import math
from random import random
import numpy as np


'''
Reconhecedor de padrões à partir de um dataset de imagens.
By André Andrade.
----------------------------------------------------------

Método:
Recebe uma matriz de posições (0,1) e converte em um vetor de 15 posições
para injetar dentro da rede neural para identificar o número que esse 
vetor representa.

Estrutura da Rede:
Camada de entrada = 15 neurônios.
Camada de saída = 10 neurônios.
Completamente conexa (1 Bias para cada neurônio.).

Padrão da Imagem: 5x3
__**__  ____**  ******  ******
**__**  ____**  ____**  ____**
**__**  ____**  ******  __****  
**__**  ____**  **____  ____**
__**__  ____**  ******  ******

Vetor de entrada:
x = [p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15]
0 = [0 1 0 1 0 1 1 0 1 1 0 1 0 1 0]
1 = [0 0 1 0 0 1 0 0 1 0 0 1 0 0 1]

Vetor de saída:
y = [ y0 y1 y2 y3 y4 ... y9]
yn -> Dígito representado pela imagem (0-9)
ex: Dígito 0 : [1 0 0 0 0 0 0 0 0]
Dígito 1 : [0 1 0 0 0 0 0 0 0]
'''


atributos = np.array(
    [
        [  # 0
            0, 1, 0,
            1, 0, 1,
            1, 0, 1,
            1, 0, 1,
            0, 1, 0,
        ],
        [  # 1
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
        ],
        [  # 2
            1, 1, 1,
            0, 0, 1,
            1, 1, 1,
            1, 0, 0,
            1, 1, 1,
        ],
        [  # 3
            1, 1, 1,
            0, 0, 1,
            0, 1, 1,
            0, 0, 1,
            1, 1, 1,
        ],
        [  # 4
            1, 0, 1,
            1, 0, 1,
            1, 1, 1,
            0, 0, 1,
            0, 0, 1,
        ],
        [  # 5
            1, 1, 1,
            1, 0, 0,
            1, 1, 1,
            0, 0, 1,
            1, 1, 1,
        ],
        [  # 6
            1, 1, 1,
            1, 0, 0,
            1, 1, 1,
            1, 0, 1,
            1, 1, 1,
        ],
        [  # 7
            1, 1, 1,
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
            0, 0, 1,
        ],
        [  # 8
            1, 1, 1,
            1, 0, 1,
            1, 1, 1,
            1, 0, 1,
            1, 1, 1,
        ],
        [  # 9
            1, 1, 1,
            1, 0, 1,
            1, 1, 1,
            0, 0, 1,
            0, 0, 1,
        ]
    ]
)


classe = np.zeros((10, 10))
np.fill_diagonal(classe, 1)


# Modelando o Perceptron

w = np.zeros((15, 10))
wb = np.zeros((10,))
alfa = 0.1


def f(x: float) -> float:
    return 1 / (1+math.exp(-x))

# Criando valores aleatórios de peso


def init_pesos() -> None:
    for j in range(10):
        wb[j] = np.random.random()
        for i in range(15):
            w[i][j] = np.random.random()


def previsao(x: float) -> list:
    _y = np.zeros((10,))
    for j in range(10):
        soma = wb[j]
        for i in range(15):
            soma += w[i][j]*x[i]

        _y[j] = f(soma)

    return _y


def atualiza_pesos(x: float, y: float, _y: list) -> None:

    for j in range(10):
        ej = y[j] - _y[j]
        wb[j] = wb[j] + alfa * ej
        for i in range(15):
            w[i][j] = w[i][j] + alfa * ej * x[i]


def emq() -> float:
    erroTotal = 0
    nInstancia = atributos.shape[0]
    for i in range(10):
        _y = previsao(atributos[i])
        y = classe[i]
        for j in range(10):
            erroTotal += (y[j] - _y[j]) ** 2

        return (erroTotal / nInstancia) / 10


# Laço de Treino
instanciaAtual = 0
epoca = 0
erroAtual = emq()

print("Epoca: ", epoca, "Erro de Treinamento: ", erroAtual)
while erroAtual > 0.1 and epoca < 1000:
    x = atributos[instanciaAtual]
    _y = previsao(x)
    y = classe[instanciaAtual]

    atualiza_pesos(x, y, _y)

    instanciaAtual += 1

    erroAtual = emq()

    if instanciaAtual >= atributos.shape[0]:
        print("Epoca: ", epoca, "Erro de Treinamento: ", erroAtual)
        instanciaAtual = 0
        epoca += 1


def argMax(y):
    maximo = -float('inf')
    indice = -1
    for i in range(y.shape[0]):
        if y[i] > maximo:
            maximo = y[i]
            indice = i
    return i


# Fase de Teste
for i in range(atributos.shape[0]):
    _y = previsao(atributos[i])
    print(i, argMax(_y))
