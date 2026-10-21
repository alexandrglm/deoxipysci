# EJERCICIO 9
import numpy as np

print("""
# Ejercicio 9.  Transpuesta III

Explica brevemente la diferencia entre `A.T` y `A * A` utilizando una matriz NumPy de ejemplo
""")

A = np.array([[1, 2, 3], [10, 20, 30]])

A_producto_de_hadamard = A * A

A_transpuesta = A.T.copy()

explica = f"""
Dada la matriz :
{A}

- "A * A" es una multiplicación ELEMENTO A ELEMENTO (producto de Hadamard)
    - Devolverá una matriz con las misma forma y dimensiones
    - En este caso, multiplicando cada componente por sí misma

{A_producto_de_hadamard}

- "A.T" es la transpuesta
    - Es decir, estamos cambiando la forma
    - Sus filas, por sus columnas, y viceversa
    - En ningún caso estamos modificando las componentes
    - Seguiremos teniendo una sola matriz de vuelta, pero donde era [1, 2, 3], [10, 20, 30] ...
    - ... tendremos [1, 10], [2, 20], [3, 30] 
    
{A_transpuesta}
"""
print(explica)


