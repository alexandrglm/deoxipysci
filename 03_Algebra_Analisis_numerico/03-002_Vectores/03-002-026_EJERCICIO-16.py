import numpy as np

heredoc = """
## Ejercicio 16. Caso límite

¿Qué sucede al calcular la similitud del coseno entre `u = np.array([0, 0])` y `v = np.array([1, 2])` con la fórmula anterior? 
Explica por qué.

"""

u, v = np.asarray([0, 0]), np.asarray([1, 2])

euclideas_rapidas = ( (np.linalg.norm(u)) * (np.linalg.norm(v)) )

valor_similitud_coseno = u @ v / euclideas_rapidas

# print(valor_similitud_coseno)

heredoc_explica = """
Una o varias de las componentes de un vector puede ser 0, pero NUNCA todos, ni la suma de todas las componentes puede ser 0.
A nivel de programación obtenemos un NaN en toda regla.
Es decir, no puede medirse un ángulo cuando la suma de componentes es 0.
No tiene sentido. Por eso es un caso límite.

SI EL VECTOR COMPLETO es CERO, JAMAS TENDRAS UNA DIRECCION DEFINIDA
"""
print(heredoc_explica)