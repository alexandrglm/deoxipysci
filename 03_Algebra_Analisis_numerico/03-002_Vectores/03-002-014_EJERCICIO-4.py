import numpy as np

heredoc = """
# 4. NumPy

Si el vector es igual a un array que contiene tres componentes (10 - 20 - 30)
- ¿qué devuelven `v.shape`, `v.ndim` y `v.size`?

"""
print(heredoc)

vector = np.array([10, 20, 30])

print("\n Vector de tres componentes 10 / 20 / 30 -> vector = np.array([10,20,30]) : ", vector)
print("\n ¿Qué devuelve shape? -> Filas y Columnas. Ejes y Dimensiones.\n  Como es un array simple, unidimensional, nos dice la cantidad de componentes, en formato (COMPONENTES,(vacio), (3,)")
print("\n ¿Qué devuelve ndim? El numero de dimensiones. Este array es unidimensional, entonces una sola dimensión (1)" )
print("\n ¿Y, el método size? -> Devuelve el numero de coimponenes también, cuántos valores diferentes tiene el array")

print(vector.shape)
print(vector.ndim)
print(vector.size)