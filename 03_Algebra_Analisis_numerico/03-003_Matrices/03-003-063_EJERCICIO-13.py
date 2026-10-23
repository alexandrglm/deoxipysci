# EJERCICIO 13
import numpy as np

print(f"""
# Ejercicio 13. Determinante $2 \times 2$

Calcula a mano el determinante de [3, 1], [2, 5]

""")

a, b, c, d = 3, 1, 2, 5

vector_0 = np.asarray([3, 1])
vector_1 = np.asarray([2, 5])

A = np.asarray([vector_0, vector_1])

print(vector_0, vector_1)
print(A)

A = np.asarray([[a, b], [c, d]])
print(A)

ad = A[0, -1] * A[-1, 0]
cb = A[0, 0] * A[-1, -1]

determinante = ad -cb

print(determinante)

determinante_metodo = np.linalg.det(A)
print(determinante_metodo)


explica = f"""
Determinante de ....
{A}

... es:  {determinante}

- Negativo, está formando un paralelogramo, en sentido HORARIO, 
"""
print(explica)