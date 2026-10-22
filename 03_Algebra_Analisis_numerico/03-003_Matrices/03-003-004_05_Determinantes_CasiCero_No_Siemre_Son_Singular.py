import numpy as np

matriz_componentes_tolerancia = 1e-5 * np.eye(3)
determinante = np.linalg.det(matriz_componentes_tolerancia)

print(matriz_componentes_tolerancia)
print(determinante)

print(np.isclose(determinante, 0))
print(np.isclose(determinante, 0, atol=1e-15))

print(np.linalg.matrix_rank(matriz_componentes_tolerancia))

# np.linalg.matrix_rank() un pooco más a fondo
A = np.array([ [1, 2], [3, 4] ])
P = np.array([ [2, 0, 1], [1, 3, 2], [1, 1, 4] ])
S = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
U = np.array([ [2, 1, 3], [0, 4, 1], [0, 0, 5] ])

print(np.linalg.matrix_rank(A))
print(np.linalg.matrix_rank(P))
print(np.linalg.matrix_rank(S))
print(np.linalg.matrix_rank(U))

