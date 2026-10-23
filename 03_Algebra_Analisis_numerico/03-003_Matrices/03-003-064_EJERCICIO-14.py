# EJERCICIO 14
import numpy as np

print(f"""
# Ejercicio 14. Determinante - Tiene inversa?

Sin usar NumPy, ¿es invertible [2, 4], [1, 2]$? 
Justifica con su determinante.

""")

A = np.asarray([[2, 4], [1, 2]])

explica = f"""
Dada la matriz ...:
{A}

- A ojo, determinante es CERO, 
D =2 * 2 - 4 * 1 = 0

- Comprobado con el método:
{np.linalg.det(A)}

- Por si queda alguna duda:
{np.isclose(np.linalg.det(A), 0)}

"""
print(explica)