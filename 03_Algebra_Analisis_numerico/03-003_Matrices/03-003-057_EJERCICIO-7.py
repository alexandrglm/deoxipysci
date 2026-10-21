# EJERCICIO 7
import numpy as np

print("""
# Ejercicio 7. Transpuestas I

Crea una matriz de forma `(2, 3)` con los valores [1, 2, 3], [4, 5, 6]:

    - Calcula su transpuesta e indica su `shape`.
""")

A = np.array([ [1, 2, 3], [4, 5, 6] ])

transpuesta_metodo = np.transpose(A)
transpuesta_atajo = A.T

print(A)
print(transpuesta_metodo)
print(A.shape)
print(transpuesta_metodo.shape)