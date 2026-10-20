# EJERCICIO 3
import numpy as np

print("""
# Ejercicio 3. Interpretación

Si una matriz tiene shape == (4, 3), 
¿cuántas filas, columnas y elementos contiene?
"""
)

heredoc_explica = """
Para shape (4, 3):
 - Cuatro filas
 - Tres columnas
 - 12 elementos 
 - Pero que tenga en el eje X 4 filas NO significa que sea "4D!"
"""

ejemplo_4_3 = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 8], [10, 11, 12] ])
print(ejemplo_4_3.shape)
print(ejemplo_4_3.ndim)



ejemplo_hipercubo_para_dejar_de_fallar_en_ndims = np.array([
    [
        [
            [1, 2], [3, 4]
        ],
        [
            [5, 6], [7, 8]
        ]
    ],
    [
        [
            [9, 10], [11, 12]
        ],
        [
            [13, 14], [15, 16]
        ]
    ]

])

print(ejemplo_hipercubo_para_dejar_de_fallar_en_ndims.shape)
print(ejemplo_hipercubo_para_dejar_de_fallar_en_ndims.ndim)
print(ejemplo_hipercubo_para_dejar_de_fallar_en_ndims[1, 0, 0, 1])