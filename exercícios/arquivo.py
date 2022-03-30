import numpy as np

matriz = []
v_constante = []

def solucao():
    res = np.linalg.solve(matriz, v_constante)
    return res

def triangular_superior():
    pass

def solucao_triangular_superior():
    pass

def main():
    solve = solucao()
    superior = triangular_superior()
    tri_solve = solucao_triangular_superior()

    print("RESOLUÇÃO DA MATRIZ A PELO VETOR CONSTANTE B:")
    print("Matriz A:", matriz)
    print("Vetor B:", v_constante)
    print("-----------------------------")
    print("Resolucao: ", solve)
    print("Triangular: ", superior)
    print("Resolucao Triangular: ", tri_solve)

main()
