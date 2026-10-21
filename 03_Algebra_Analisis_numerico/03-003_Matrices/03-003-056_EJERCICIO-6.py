import numpy as np

print(""" 
# Ejercicio 6. Multiplicación matricial

Calcula `A @ B`
Comprueba el resultado manualmente para la primera fila
Explica por qué el resultado tiene forma `(2, 2)`
""")

A, B = np.asarray([[1, 2],[3, 4]]), np.asarray([[5, 6], [7, 8]])

producto_escalar = A @ B
producto_escalar_modo_dot = np.dot(A, B)
print(producto_escalar == producto_escalar_modo_dot)
print(producto_escalar)

C = producto_escalar

heredoc_explica = f"""
- Dadas estas matrices:

 A = [1, 2]     B = [5, 6]
     [3, 4]         [7, 8]


- Dado el resultado de su multiplicación matricial:

        C = [19, 22]
            [43, 50]

- Comprobamos manualmente la primera fila:
    {C[0,0]}, {C[0, 1]}

{C[0, 0] == ( A[0, 0] * B[0, 0] ) + ( A[0, 1] * B[1, 0] ) }
{C[0, 1] ==  (A[0, 0] * B[0, 1]) + ( A[0, 1] * B[1, 1])  }
"""
print(heredoc_explica)


C = producto_escalar

# PRIMERA FILA de C
# Productos sueltos (cada uno mezcla un valor de A con uno de B)

## Fila 0 de A contra columna 0 de B, para C[0, 0]
producto_escalar_A00_B00 = A[0, 0] * B[0,0]
producto_escalar_A01_B10 = A[0, 1] * B[1, 0]

## Fila 0 de A contra columna 1 de B, para C[0, 1]
producto_escalar_A00_B01 = A[0, 0] * B[0, 1]
producto_escalar_A01_B11 = A[0, 1] * B[1, 1]

# SEGUNDA FILA de C
## Fila 1 de A contra columna 0 de B, para C[1, 0]
producto_escalar_A10_B00 = A[1, 0] * B[0, 0]
producto_escalar_A11_B10 = A[1, 1] * B[1, 0]

## Fila 1 de A contra columna 1 de B, para C[1, 1]
producto_escalar_A10_B01 = A[1, 0] * B[0, 1]
producto_escalar_A11_B11 = A[1, 1] * B[1, 1]


# MONTANDO LA MATRIZ C por FILAS
# Cada celda es la SUMA de sus dos productos
## PRIMERA FILA DE C
producto_escalar_C00 = producto_escalar_A00_B00 + producto_escalar_A01_B10
producto_escalar_C01 = producto_escalar_A00_B01 + producto_escalar_A01_B11

## SEGUNDA FILA de C
producto_escalar_C10 = producto_escalar_A10_B00 + producto_escalar_A11_B10 
producto_escalar_C11 = producto_escalar_A10_B01 + producto_escalar_A11_B11



# COMPROBACION de PRIMERA FILA de C
print(C[0, 0] == producto_escalar_C00)
print(C[0, 1] == producto_escalar_C01)

# O la fila completa de una vez
print(np.array_equal(C[0], [producto_escalar_C00, producto_escalar_C01]))


# COMPROBACION de SEGUNDA FILA de C
print( C[1, 0] == producto_escalar_C10 )
print( C[1, 1] == producto_escalar_C11 )
print(np.array_equal( C[1], [producto_escalar_C10, producto_escalar_C11] ))
