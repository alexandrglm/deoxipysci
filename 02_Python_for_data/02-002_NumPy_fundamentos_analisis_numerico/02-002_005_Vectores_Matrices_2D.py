import numpy as np

datos = np.array([    
    [20, 3],    
    [15, 7],    
    [12, 2],    
    [10, 4]
])


print("\n A. Cuando MATRIZ 'np.array([ [20, 3], [15, 7], [12, 2], [10, 4] ])' ... :")
print("   1. print:  \n", datos)
print("   2. Tipo?:                                           ", type(datos))
print("   3. Tipo de dato almacenado (dtype)?:                ", datos.dtype)
print("   4. Dimensiones y tamaño de cada dimension (shape)?: ", datos.shape)
print("   5. Numero de dimensiones (ndim)?:                   ", datos.ndim)
print("\n   Para este ejemplo, `shape` será `(4,2)` y `ndim` será `2`: \n    es una matriz (arreglo bidimensional) de 4 filas y 2 columnas.")

print("\n - Datos del primer producto (primera fila, Precio y Unidades):     ", datos[0, 0])
print(" - Datos del segundo producto (primera fila, Precio y Unidades):    ", datos[1, 1])
print(" - Todos los precios (todas las columnas 0, [:, 0] ):               ", datos[:, 0])
print(" - Todas las unidades (todas columna 1,[:, 0] ):                    ", datos[:, 1])


print("\n ----------- \n")
print("\n - OPERACIONES por AXIS:")
print("       Reduce por DIMENSIONES")

datos = np.array([    
    [20, 3],    
    [15, 7],    
    [12, 2],    
    [10, 4]
])


print("\n   * Suma Por axis=0 (Reduce-Colapsa COLUMNAS, opera VERTICAL):\n", "     ", datos.sum(axis=0))
# [57 16]


print("\n   * Suma Por axis=1 (Reduce-Colapsa FILAS, opera HORIZONTAL): \n", "     ", datos.sum(axis=1))
# [23 22 14 14]