import numpy as np

heredoc = """
# 10. Comprender `u * v`

Con los vectores del ejercicio 2,
-  ¿qué devuelve `u * v`?
-  ¿Por qué ese resultado no es todavía el producto escalar?

"""
print(heredoc)

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

operacion_vectorizada = u * v
print(operacion_vectorizada)
heredoc_explica = """
Obtenemos un Array con las componentes separadas, se ha ejecutado la operación de multiplicación
de cada componente, como una operación vectorizada típica.
Por eso no tenemos aún el producto escalar, que sería la suma de las componentes (en este caso, 32).

"""
print(heredoc_explica)