'''
André Luís Andrade - 104004
Brena Oliveira - 94858
Gabrielly Haddad - 100872

'''

import numpy as np


def f(x: float) -> float:
    return 2*(x**3) + np.log(x) + np.cos(x)


def derivada_num(x0: float) -> float:
    h = 0.000001

    _f = (f(x0+h) - f(x0))/h
    print("Derivada: ", _f)


def integral_num() -> float:
    n = 5
    a = 4
    b = 4.5

    h = (a-b)/n
    x = np.linspace(a, b, n)

    itr = (h/2)*(f(a) + 2*(sum(f(x))) + f(b))
    print("Integral: ", itr)
    pass


derivada_num(2)
integral_num()
