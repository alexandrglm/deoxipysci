import numpy as np

heredoc = """
# 7. NumPy II

Escribe el código para calcular la norma euclídea del vector `[1, 2, 2]`
y señala el resultado esperado.
"""
print(heredoc)

vector = np.array([1, 2, 2])

heredoc_explica = """
A ojo, 3.
L2 o Euclídea es la raíz de la suma de los cuadrados de cada componente del vector.

Dado f{vector} que contiene tres componentes, siendo 1, 2, 2,

- El método en NumPy es np.linalg.norm()
- La sintaxis requiere al menos un argumento.
- Ese argumento, debe ser el vector.
- Por defecto, si no se le dan más argumentos, calculará la L2 Euclídea.
- El argumento para definir que norma calcular es ord=
-   ord = 1, para L1
-   ord = 2, para Euclídea
-   ord = np.inf, para Infinito (le damos el float np.inf) 


Por tanto, el código para calcular la euclídea del vector dado es:

vector = np.array([1, 2, 2])
l2 = np.linalg.norm(vector)

print(l2)

"""
print(heredoc_explica)

l2 = np.linalg.norm(vector)

print(l2)
