# EJERCICIO 1
import numpy as np

print("""
# Ejercicio 1. Dimensiones

Crea una matriz con los valores [[1, 2], [3, 4], [5, 6]].
    - Indica su shape, ndim y size
    - Explica qué representa cada resultado
""")

matriz = np.array([ [1, 2], [3, 4], [5, 6]  ])


dim_1, dim_2, dim_3 = np.asarray([[1,2], [3, 4], [5, 6]])
matriz_para_complicados_de_la_vida = np.asmatrix([ dim_1, dim_2, dim_3 ])

print(matriz)
print(matriz_para_complicados_de_la_vida)
print(matriz == matriz_para_complicados_de_la_vida)

heredoc_explica = f"""
Para la matriz [1, 2], [3, 4], [5, 6]:
    - Shape es 3,2: {matriz.shape} 
        Recibimos la forma de este array multidimensional (3D)
          Tres ejes-dimensiones, dos componentes por cada expresión-array

    - Dimesiones, 3:    {matriz.ndim}
        Tal como nos dice shape, el atributo .ndim es directo para explicar las dimensiones
            Tres dimensiones, tres ejes, tres series de valores

    - Tamaño, 6 valores reales o no:   {matriz.size}
        El atributo .size nos dice el total de valores, de las componentes
            Los valores son reales, es decir, no son None's. 
            Size no diferencia entre ello, se ajusta a que cada serie tenga el mismo numero de componentes
"""
print(heredoc_explica)