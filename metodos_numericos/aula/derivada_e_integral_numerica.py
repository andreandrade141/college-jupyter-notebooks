import numpy as np


def f(x: float) -> float:
    return 4*(x**2)+np.sin(x)-3


def derivada_num(x0: float) -> None:
    h = 0.000001
    _f = (f(x0+h) - f(x0))/h
    print("Exercício 2: ", _f)


def len_vetor(x: np.array) -> None:
    print("Exercício 3", len(x))


def malha_discreta(m: int) -> np.linspace:
    a = 4
    b = 5

    u = np.linspace(a, b, m)
    print("Exercício 4: ", u)
    return u


def exclui_elemento(i: int) -> None:
    m_vetor = 6
    vetor = malha_discreta(m_vetor)
    new_vetor = np.delete(vetor, [i])
    print("Exercício 5: ", new_vetor)


def soma_elementos_vetor() -> None:
    vetor = malha_discreta(6)
    soma = sum(vetor)
    print("Exercício 6:", soma)


def integral_numerica() -> None:
    n = 6
    a = 1
    b = 4

    h = (a-b)/n
    x = np.linspace(a, b, n+1)

    y = np.array([1.0, 2.25, 4.0, 6.25, 9.0, 12.25, 16.0])
    _y = np.delete(y, [1, len(y)-1])

    itr = (h/2)*(y[0] + 2*(sum(_y)) + y[len(y)-1])
    print("Exercício 7: ", itr)


def outra_integral_numerica() -> None:
    n = 5
    a = 1
    b = 2

    h = (a-b)/n
    x = np.linspace(a, b, n)

    def f(x: float) -> float:
        return np.log(x)

    itr = (h/2)*(f(a) + 2*(sum(f(x))) + f(b))
    print("Exercício 8: ", itr)


funcao = f(2)
print("Exercício 1: ", funcao)
derivada_num(2)
len_vetor(np.array([1, 5, 4.2, 23, 104.542]))
malha_discreta(6)
exclui_elemento(4)
soma_elementos_vetor()
integral_numerica()
outra_integral_numerica()
