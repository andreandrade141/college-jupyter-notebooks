from cmath import e, pi
import sympy as sp
# from IPython.display import display

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
xc = e

error = abs((xc-xaprox)/xc)
print("error: ", error)

# Exercício 3:

x = sp.symbols('x')
f = x**3 - sp.sqrt(x) + sp.sin(x) + sp.exp(x) + sp.log(x) - 4

print("f(x) = ")
print(f)
# display(f, raw=True)

# Exercício 4:
a = 4
print("EQUACAO PARA X = 4")
# Não funciona no vscode sem configurar o terminal padrão para o Ipython
# display(f.subs(x, a))
print(f.subs(x, a))

solvefor4 = f.subs(x, a).evalf()
print("RESOLVE F(4)")
# display(solvefor4)
print(solvefor4)
