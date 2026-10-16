# EJERCICIO 1
heredoc = """
Crea un array NumPy con los números `5, 10, 15, 20, 25`.
Crea otro array con dos dimensiones (matriz).

Imprime sus tipo, lo que almacenan, sus `shape`, su número de dimensiones y explícalo.
"""
import numpy as np

numeros = np.array( [5, 10, 15, 20, 25] )

print(type(numeros))
print(numeros.dtype)

print(numeros.shape)

print(numeros.ndim)
print("\n`5, 10, 15, 20, 25` es ... Array de numpy, (5,) cinco elementos, en 1 dimension")

# matriz
matriz = np.array(
    [
        [12, 6],
        [20, 10],
        [50, 25],
        [32, 16],
        [102, 51]
    ]
)
print(matriz)
print(type(matriz))
print(matriz.dtype)

print(matriz.shape)

print(matriz.ndim)

print("\n", matriz)
print("Es ... Array de numpy, es matriz, ...\n   no debemos confundir la creación con el metodo np.matrix que es para CLASES, lo hacemos igualmente con np.array...\n    (5,2) cinco elementos en columna 0 y 2 elementos en columna 1....\n    en DOS dimensiones")


# CORRECCION DETALLADA

"""

# shape, ndim y dtype

EL primer array:
    numeros = np.array([5, 10, 15, 20, 25])

Resultados esperados:
    numeros.shape  # (5,)
    numeros.ndim   # 1
    numeros.dtype  # int64

La interpretación de (5,) es una dimensión que contiene cinco elementos.

Pero, para una matriz, y saber definirla bien...:

    matriz = np.array([
        [12, 6],
        [20, 10],
        [50, 25],
        [32, 16],
        [102, 51]
    ])

- shape devuelve (5, 2): 
    - cinco filas y dos columnas.

> [!IMPORTANT]
> NO significa cinco elementos en la columna 0 y dos en la columna 1...  
> Significa que hay cinco posiciones en el primer eje y dos en el segundo.

"""