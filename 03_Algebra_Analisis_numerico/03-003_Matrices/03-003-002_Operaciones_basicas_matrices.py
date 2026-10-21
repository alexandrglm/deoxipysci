import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[10, 20],
              [30, 40]])


print("""

- DADAS ESTAS DOS MATRICES:

        A = np.array([[1, 2],
                    [3, 4]])

        B = np.array([[10, 20],
                    [30, 40]])

 * VISUALIZADO:

       A = [1   2]        B = [10  20]
           [3   4]            [30  40]

""")

# 1. OPERACIONES DIRECTAS (elemento a elemento)

suma = A + B
resta = A - B
producto = A * B
division = B / A 

print(f"""
- OPERACIONES BASICAS DIRECTAS (ELEMENTO a ELEMENTO)

 - Suma directa:
{suma}

 - Resta directa:
{resta}

 - Multiplicación directa, (NO es la matricial):
{producto}

 - División directa:
{division}
""")


# 2. MULTIPLICACIÓN POR ESCALAR

A_por_3 = A * 3
B_por_5 = B * 5

print(f"""
- MULTIPLICACIÓN POR ESCALAR (cada componente por el mismo número)

 - A por 3:
{A_por_3}

 - B por 5:
{B_por_5}
""")



# 3. MULTIPLICACIÓN MATRICIAL CON NUMPY

matricial_arroba = A @ B
matricial_dot = np.dot(A, B)
suma_de_productos = np.sum(A * B)  # OJO: es un número, no una matriz

print(f"""
- MULTIPLICACIÓN MATRICIAL (matriz @ matriz)

 Cada elemento del resultado se calcula con UNA FILA de A y UNA COLUMNA de B,
 multiplicando y sumando (como un producto escalar)

 - A @ B:
{matricial_arroba}

 - np.dot(A, B):
{matricial_dot}

 AL IGUAL QUE CON VECTORES (1D), ambos métodos dan los mismos valores...
 ...
 PERO np.sum(A * B) NO sirve aquí:
   - A * B multiplica posiciones iguales (elemento a elemento)
   - np.sum() suma TODOS esos productos y devuelve UN SOLO NÚMERO
   - np.sum(A * B) = {suma_de_productos}   (un escalar, nunca una matriz)
""")



# 4. LA MULTIPLICACIÓN MATRICIAL, DESCOMPUESTA A MANO

"""
REGLA DE LA MULTIPLICACION MATRICIAL:

C[i, j] = A[i, 0] * B[0, j]  +  A[i, 1] * B[1, j]
            parte 1                 parte 2

Fíjate en el índice del medio: el SEGUNDO índice de A es el PRIMERO de B
  - A recorre su fila   -> columnas 0, 1
  - B recorre su columna -> filas 0, 1

"""

## PASO 1: los 8 valores individuales
matriz_A_fila0_col0 = A[0, 0]
matriz_A_fila0_col1 = A[0, 1]
matriz_A_fila1_col0 = A[1, 0]
matriz_A_fila1_col1 = A[1, 1]

matriz_B_fila0_col0 = B[0, 0]
matriz_B_fila0_col1 = B[0, 1]
matriz_B_fila1_col0 = B[1, 0]
matriz_B_fila1_col1 = B[1, 1]

print(f"""
- PASO 1. LOS 8 VALORES INDIVIDUALES

    A[0,0]={matriz_A_fila0_col0}   A[0,1]={matriz_A_fila0_col1}
    A[1,0]={matriz_A_fila1_col0}   A[1,1]={matriz_A_fila1_col1}

    B[0,0]={matriz_B_fila0_col0}  B[0,1]={matriz_B_fila0_col1}
    B[1,0]={matriz_B_fila1_col0}  B[1,1]={matriz_B_fila1_col1}
""")


## PASO 2: los 8 productos (2 por cada celda de C)

### Celda C[0, 0]: fila 0 de A  contra  columna 0 de B
C_fila0_col0_parte1 = matriz_A_fila0_col0 * matriz_B_fila0_col0  # A[0,0] * B[0,0]
C_fila0_col0_parte2 = matriz_A_fila0_col1 * matriz_B_fila1_col0  # A[0,1] * B[1,0]

### Celda C[0, 1]: fila 0 de A  contra  columna 1 de B
C_fila0_col1_parte1 = matriz_A_fila0_col0 * matriz_B_fila0_col1  # A[0,0] * B[0,1]
C_fila0_col1_parte2 = matriz_A_fila0_col1 * matriz_B_fila1_col1  # A[0,1] * B[1,1]

### Celda C[1, 0]: fila 1 de A  contra  columna 0 de B
C_fila1_col0_parte1 = matriz_A_fila1_col0 * matriz_B_fila0_col0  # A[1,0] * B[0,0]
C_fila1_col0_parte2 = matriz_A_fila1_col1 * matriz_B_fila1_col0  # A[1,1] * B[1,0]

### Celda C[1, 1]: fila 1 de A  contra  columna 1 de B
C_fila1_col1_parte1 = matriz_A_fila1_col0 * matriz_B_fila0_col1  # A[1,0] * B[0,1]
C_fila1_col1_parte2 = matriz_A_fila1_col1 * matriz_B_fila1_col1  # A[1,1] * B[1,1]


print(f"""
- PASO 2. LOS 8 PRODUCTOS (2 por cada celda de C)

    C[0,0]:  A[0,0]·B[0,0] = {C_fila0_col0_parte1:<5} A[0,1]·B[1,0] = {C_fila0_col0_parte2}
    C[0,1]:  A[0,0]·B[0,1] = {C_fila0_col1_parte1:<5} A[0,1]·B[1,1] = {C_fila0_col1_parte2}
    C[1,0]:  A[1,0]·B[0,0] = {C_fila1_col0_parte1:<5} A[1,1]·B[1,0] = {C_fila1_col0_parte2}
    C[1,1]:  A[1,0]·B[0,1] = {C_fila1_col1_parte1:<5} A[1,1]·B[1,1] = {C_fila1_col1_parte2}
""")


## PASO 3: sumar las dos partes de cada celda
C_fila0_col0 = C_fila0_col0_parte1 + C_fila0_col0_parte2
C_fila0_col1 = C_fila0_col1_parte1 + C_fila0_col1_parte2
C_fila1_col0 = C_fila1_col0_parte1 + C_fila1_col0_parte2
C_fila1_col1 = C_fila1_col1_parte1 + C_fila1_col1_parte2

print(f"""
- PASO 3. SUMAR LAS DOS PARTES DE CADA CELDA

    C[0,0] = {C_fila0_col0_parte1} + {C_fila0_col0_parte2} = {C_fila0_col0}
    C[0,1] = {C_fila0_col1_parte1} + {C_fila0_col1_parte2} = {C_fila0_col1}
    C[1,0] = {C_fila1_col0_parte1} + {C_fila1_col0_parte2} = {C_fila1_col0}
    C[1,1] = {C_fila1_col1_parte1} + {C_fila1_col1_parte2} = {C_fila1_col1}
""")


# PASO 4: montar la matriz C y la comparamos con np
C_manual = np.array([[C_fila0_col0, C_fila0_col1],
                     [C_fila1_col0, C_fila1_col1]])

print(f"""
- PASO 4. MONTAR C Y COMPARAR CON NUMPY

 - C montada a mano:
{C_manual}

 - A @ B:
{A @ B}

 - ¿Son idénticas?: {np.array_equal(C_manual, A @ B)}
""")




# 5. LA TRAMPA MENTAL: MISMA POSICIÓN (A * B) frente a POSICIONES CRUZADAS (A @ B)

misma_posicion = matriz_A_fila0_col1 * matriz_B_fila0_col1  # A[0,1] * B[0,1]  -> es A * B
posiciones_cruzadas = matriz_A_fila0_col1 * matriz_B_fila1_col0  # A[0,1] * B[1,0] -> es A @ B

print(f"""
- LA TRAMPA MENTAL: ¿con quién se empareja A[0,1]?

    Misma posición  A[0,1] * B[0,1] = {misma_posicion}   -> pertenece a A * B (elemento a elemento)
    Cruzada         A[0,1] * B[1,0] = {posiciones_cruzadas}   -> pertenece a A @ B (matricial)

    En la matricial, A[i, k] se empareja con B[k, j]:
    
        - El índice de en medio (k) es el MISMO
        - Los de fuera (i, j) son los que mandan en C
""")



# 6. LO MISMO, CON BUCLES (para cualquier tamaño)
C_bucles = np.zeros((A.shape[0], B.shape[1]), dtype=int)

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            C_bucles[i, j] += A[i, k] * B[k, j]

print(f"""
- CON BUCLES (i, j, k):
    
    - En código, para entenderlo: 
    for i in range(A.shape[0]):      # filas de A
    for j in range(B.shape[1]):      # columnas de B
        for k in range(A.shape[1]):  # recorre fila de A y columna de B a la vez
            C_bucles[i, j] += A[i, k] * B[k, j]
 
{C_bucles}

 - ¿Idéntica a A @ B?: {np.array_equal(C_bucles, A @ B)}
""")