import numpy as np

heredoc = """
Dados los vectores f{u}=(3,4) y f{v}=(2,5) :

 - Calcula su producto escalar
 - Explica brevemente las operaciones.

"""

u = np.array([3, 4])
v = np.array([2, 5])

heredoc_explica = """
Visualmente, recogemos las componentes de cada vector, y multiplicamos
cada uno por el otro (cada posición del uno por la correspondiente del otro).

[3, 4] * [2, 5] = [(3 * 2) + (4 * 5)] = [6 + 20] = 26

El producto escalar de ambos vectores es 26.

Tenemos varios métodos con numpy, que desarrollamos en el resto de ejercicios.
Pero, estos son:

- Sin método, la suma de la operación vectorizada ( sum(u * v) )

- Método más sencillo, @, Multiplicación matricial (u @ v)

- Método np.dot(u, v)

- Método np.sum(u * v ), tan sencillo como el método @

"""
print(heredoc_explica)