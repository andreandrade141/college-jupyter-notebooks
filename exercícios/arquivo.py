"""
    ANDRÉ LUÍS SEBASTIÃO ANDRADE - 104004
"""
import numpy as np


def tlinha(A, i, j):
    buffer = A[i]
    A[i] = A[j]
    A[j] = buffer
    return A


def mlinha(A, i, alfa):
    A[i] = alfa*A[i]
    return A


def slinha(A, i, k, alfa):
    A[i] = A[i] + alfa*A[k]
    return A


def step_gauss(A, k):
    L = range(len(A))
    for j in L[k+1:]:
        m = -A[j, k]/A[k, k]
        A = slinha(A, j, k, m)
    return A


def triangular(A, B):
    L = len(A)
    for k in range(L):
        if A[k, k] != 0:
            A = step_gauss(A, k)
            print(A)
        else:
            print(' falhou no passo '), k
    solve_triangular(A, B)
    return A


def solve_triangular(A, B):
    x3 = B[2, 0]/A[2, 2]

    def x2():
        x2 = (B[1, 0]-x3)/A[1, 1]
        return x2

    def x1():
        x1 = (B[0, 0]-x2()-x3)/A[0, 0]
        return x1

    print(f'SOLUCOES: x1:{x1()}, x2:{x2()}, x3{x3}')


a = np.array([[2, 1, 3],
              [-1, -3, 2],
              [3, 1, -3]])
b = np.array([[-1],
              [12],
              [0], ])

B = triangular(a, b)
