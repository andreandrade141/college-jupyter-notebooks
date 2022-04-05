from cmath import e, pi
import sympy as sp

# Exercício 1:

x1 = 0.0
x1abs = abs(x1)
print(x1abs)

x2 = 5.0
x2abs = abs(x2)
print(x2abs)

x3 = -pi
x3abs = abs(x3)
print(x3abs)

# Exercício 2:

xaprox = 2.72
x = e

error = abs((x-xaprox)/x)
print("error: ", error)
