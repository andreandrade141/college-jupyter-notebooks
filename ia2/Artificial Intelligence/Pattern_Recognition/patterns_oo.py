import os
import math
from random import random
import numpy as np


class PatternRecognition():
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

    def __init__(self) -> None:
        pass
