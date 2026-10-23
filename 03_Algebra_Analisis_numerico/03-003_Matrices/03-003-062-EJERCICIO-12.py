# EJERCICIOP 12
import numpy as np

print(f"""
# Ejercicio 12. Determinante  III

Calcula el determinante de:

[1, 2], [3, 4]

- Indica qué resultado obtienes
- Explica qué implica respecto a la existencia de su matriz inversa
""")

A = np.array([ [1, 2], [3, 4] ])


determinante_A = (A[0, 0] * A[1, 0]) - (A[0, 1] * A[1, 1])
A_inversa = np.linalg.det(A)

A_close_cero = np.isclose(determinante_A, 0)
A_matrix_rank = np.linalg.matrix_rank(A)

print(A)
print(determinante_A)
print(A_inversa)
print(A_close_cero)
print(A_matrix_rank)


explica = f"""
Que la matriz:
{A}

... tenga un determinante valor:    {determinante_A}

... significa que:

1.  No es una matriz singular, pues su valor no es cercano a 0
2. Sus filas y columnas, sus valores, son independientes
3. Ninguna de sus filas es un producto de las otras
5. Es decir, no hay información repetida o derivada de las demás
4. Gráficamente sus lineas forman un paralelográmo con un área definida

"""