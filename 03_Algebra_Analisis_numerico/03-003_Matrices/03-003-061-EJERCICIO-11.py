# EJERCICIO 11
import numpy as np

print(f"""
# Ejercicio 11. Determinante II

Calcula el mismo determinante con `np.linalg.det(A)`. 
Compara el resultado con el cálculo manual.
""")


vector_0, vector_1 = np.asarray( [2, 3] ), np.asarray([1, 4])

print(vector_0)
print(vector_1)

A_de_vector = np.asarray([ vector_0, vector_1 ])
A = np.asarray([ [2, 3], [1, 4] ])

print(A_de_vector)

a, b = vector_0[0], vector_0[1]
c, d = vector_1[0], vector_1[1]

ad = (a * d)
bc = (b * c)

determinante_manual_desde_vectores = ad - bc
print(a, b, c, d)



a2, b2, c2, d2 = A[0, 0], A[0, 1], A[1, 0], A[1, 1]
print(a2, b2, c2, d2)

a2d2 = (a2 * d2)
b2c2 = (b2 * c2)

determinante_manual_desde_matriz = a2d2 - b2c2

determinante_np = np.linalg.det(A)
determinante_de_vector = np.linalg.det(A_de_vector)

print(A)
print(determinante_np)
print(determinante_de_vector)
print(determinante_manual_desde_vectores)
print(determinante_manual_desde_matriz)
print(np.isclose(determinante_manual_desde_vectores, determinante_np))
print(np.isclose(determinante_manual_desde_matriz, determinante_np))
print(np.isclose(determinante_de_vector, determinante_np))

