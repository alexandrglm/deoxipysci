# EJERCICIO 5
import numpy as np

print("""
# Ejercicio 5. Escalar

Calcula `A * 3`
- Explica qué ocurre con cada elemento

""")

A = np.asarray([ [1, 2], [3, 4] ])
escalar = 3
producto_escalar = A * 3

heredoc_explica = f"""
Dada {A}:

- Cada componente de cada celda/serie de la matriz, se multiplica por el escalar ({escalar}):

 - Dando por resultado el producto escalar:
{producto_escalar}

"""
print(heredoc_explica)