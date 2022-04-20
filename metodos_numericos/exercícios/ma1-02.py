"""
    INTEGRANTES:
    ANDRÉ LUÍS SEBASTIÃO ANDRADE - 104004
    BRENA FREITAS DE OLIVEIRA - 94858
"""


def newton(f, df, x0, ed, itmax):
    L = range(1, itmax+1)
    it = 0
    a = x0
    for i in L:
        raiz = a
        if df(raiz) != 0:
            raiz = raiz-f(raiz)/df(raiz)
            erro = raiz-a
            a = raiz
            it = i
        else:
            it = itmax+1
            break
        if abs(erro) <= ed:
            break
    if it > itmax:
        it = 0.25
    elif it == itmax:
        it = 0.75
    return [raiz, erro, it]


# Funções
def f(x): return x**3 - x - 4
def df(x): return 3*x**2-1


L = newton(f, df, 1.5, 0.0001, 100)
print(L)
