# EJERCICIO 13
import numpy as np


"""
# Ejercicio 10. Determinante I
Calcula manualmente el determinante de:

[2, 3], [1, 4]
"""

A = np.array([[2, 3], [1, 4]])

print(A)

determinante_manual_explica = f"""
En primer lugar, sí tiene determinante por cumplir la condición de ser una matriz cuadrada.

La determinante la calculamos tal que:

D(A) es igual al producto escalar de Diagonal Principal menos el producto de la Secundaria

Dada    
    [2, 3]
    [1, 4]

1.  Diaginal Principal es   2 * 4
2.  Diagonal Secundaria es  3 * 1

3. La determinante de la matriz dada será   5
"""

print(determinante_manual_explica)

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


