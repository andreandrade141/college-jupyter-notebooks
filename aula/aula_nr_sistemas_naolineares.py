import numpy as np


def norma_infinita():  # Cálculo da norma infinita
    x = np.zeros((3, 1))
    x = np.array([[2.0], [-9.0], [7.0]])

    print("x: \n", x)

    n_inf = np.linalg.norm(x, np.inf)

    print("\n||x||_inf: ", n_inf)


def invocar_funcao():
    def f(x):
        y = x**2 + np.sin(x) + np.exp(x)
        return y
    y = f(3)
    print("\n\nf(3.0)= ", y)


def funcao_vetorial():
    def f(x):
        y = np.zeros((2, 1))
        y[0][0] = x[0][0]**2+x[1][0]
        y[1][0] = x[0][0]*x[1][0]
        return y

    x = np.zeros((2, 1))
    x = np.array([[3.0], [5.0]])

    print("\n\nfvetorial((3,5))= \n", f(x))


def funcao_vetorial2():
    def f(x):
        y = np.zeros((2, 2))
        y[0][0] = x[0][0]+x[1][0]
        y[0][1] = x[0][0]*x[1][0]
        y[1][0] = np.sin(x[0][0])
        y[1][1] = np.exp(x[1][0])

        return y

    x = np.zeros((2, 1))
    x = np.array([[4.0], [3.0]])

    print("\n\n fvetorial2x2((4, 3))= \n", f(x))


def sistema_n_linear1():
    pass


norma_infinita()
invocar_funcao()
funcao_vetorial()
funcao_vetorial2()
