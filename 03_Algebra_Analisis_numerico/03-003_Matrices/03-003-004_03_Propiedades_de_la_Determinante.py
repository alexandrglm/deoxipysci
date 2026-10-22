import numpy as np

A = np.array([ [1, 2], [3, 4] ])
B = np.array([ [2, 0], [1, 3] ])

# PROPIEDAD    Traspuesta  
## det(A ^ T) == det(A)
determinante_traspuesta_A = np.linalg.det(A.T)
determinante_A = np.linalg.det(A)
determinante_B = np.linalg.det(B)


print(determinante_A)
print(determinante_traspuesta_A)
print(np.isclose(determinante_A, determinante_traspuesta_A))




# PROPIEDAD Producto de matrices 
## det(AB) = det(A) * det(B)
determinante_AB = determinante_A * determinante_B
determinante_A_at_B_directo = np.linalg.det(A @ B)


print(determinante_AB)
print(determinante_A_at_B_directo)

print(np.isclose(determinante_AB, determinante_A_at_B_directo))
print(np.isclose(determinante_AB, (determinante_A * determinante_B)))
print(np.isclose(determinante_A_at_B_directo, (determinante_A * determinante_B)))



# PROPIEDAD Multiplicar por un escalar (matriz $n \times n$)
## det(kA) = k^n * det(A), con n = 2
producto_determinante_A_escalar_3 = np.linalg.det(3 * A)
producto_determinante_A_escalar_3_al_cubo = 3 ** 2 * determinante_A

print(producto_determinante_A_escalar_3)
print(producto_determinante_A_escalar_3_al_cubo)
print(np.isclose(producto_determinante_A_escalar_3, producto_determinante_A_escalar_3_al_cubo))


# PROPIEDAD Intercambiar filas cambia el signo
A_filas_intercambiadas = A[::-1]
A_filas_intercambiadas_determinante = np.linalg.det(A[::-1])

A_negativa = -A
A_negativa_determinante = np.linalg.det(A_negativa)

print(A_filas_intercambiadas_determinante)
print(A_negativa_determinante)
print(np.isclose(A_filas_intercambiadas_determinante, A_negativa_determinante))


# PROPIEDAD     La suma NO se cumple
A_suma_B = A + B

determinante_A_SUMA_B = np.linalg.det(A_suma_B)
determinante_A_MAS_determinante_B = np.linalg.det(A) + np.linalg.det(B)

print(determinante_A_SUMA_B)
print(determinante_A_MAS_determinante_B)
print(np.isclose(determinante_A_SUMA_B, determinante_A_MAS_determinante_B))




# PROPIEDAD DE LAS MATRICES TRIANGULARES
## Triangulas principal superior
U = np.array([ [2, 1, 3], [0, 4, 1], [0, 0, 5] ])


diagonal_principal_U = np.diag(U)
producto_diagonal_principal_U = np.prod(diagonal_principal_U)

determinante_U = np.linalg.det(U)

print(U)
print(diagonal_principal_U)
print(producto_diagonal_principal_U)
print(determinante_U)
print(np.isclose(determinante_U, producto_diagonal_principal_U))


