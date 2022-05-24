# import os
import random
import math
import numpy as np
# import pandas as pd

# Atributos
dataset = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])
# Classe
output = np.array([0, 0, 0, 1])

wb = random.random()
w1 = random.random()
w2 = random.random()


def f(x: float) -> int:
    # Função de ativação: degrau unitário.
    if x >= 0:
        return 1
    return 0


def previsao(x1: float, x2: float) -> int:
    # Função saída do perceptron.
    prev = f(x1*w1 + x2*w2 + wb)
    print(prev)
    return prev


def ErroMedioQuadratico() -> float:
    # Função do erro de treinamento do algoritmo.
    erro = 0
    for i in range(dataset.shape[0]):
        # output previsto.
        _y = previsao(dataset[i][0], dataset[i][1])
        erro += (output[i] - _y)**2
        return erro/dataset.shape[0]


# Fase de Treino.
erro_anterior = float('inf')
erro_atual = ErroMedioQuadratico()
alfa = 0.01
# instancia atual
i = 0
epocas = 0

while erro_atual > 0:
    # Prever com os pesos atuais
    _y = previsao(dataset[i][0], dataset[i][0])
    erro = output[i] - _y

    # Atualizar os pesos.
    wb = wb + alfa*(erro)
    w1 = w1 + alfa*erro*dataset[i][0]
    w2 = w2 + alfa*erro*dataset[i][1]

    # Próxima instância.
    i += 1
    if i >= dataset.shape[0]:
        # Atualiza a época.
        epocas += 1
        i = 0
    if erro != 0:
        erro_anterior = erro_atual
        erro_atual = ErroMedioQuadratico()
    print("Erro Atual: ", erro_atual, wb, w1, w2)
print("Epocas necessárias: ", epocas)

# Previsão após o treinamento.
