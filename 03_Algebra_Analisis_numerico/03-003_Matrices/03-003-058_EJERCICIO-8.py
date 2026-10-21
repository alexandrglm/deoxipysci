# ERJECICIO 8
import numpy as np

print("""
# Ejercicio 8. Transpuesta II

Crea una matriz cuadrada de 3x3
    - Calcula su transpuesta
    - Comprueba qué ocurre con los elementos de la diagonal principal
""")

vector_0, vector_1, vector_2 = np.zeros(3, dtype=int), np.arange(6, 9), np.array([3, 4, 5])

print(vector_0)
print(vector_1)
print(vector_2)

matriz = np.array([ vector_0, vector_1, vector_2 ])
matriz_as_matrix_deprecado_pero_util = np.asmatrix([ vector_0, vector_1, vector_2])

print(matriz)
print(matriz_as_matrix_deprecado_pero_util)

matriz_transpuesta_atajo = matriz.T
matriz_transpuesta_metodo = np.transpose(matriz)

comprueba_shared_atajo = np.shares_memory(matriz, matriz_transpuesta_atajo)
comprueba_shared_metodo = np.shares_memory(matriz, matriz_transpuesta_metodo)
print(comprueba_shared_atajo)
print(comprueba_shared_metodo)

matriz_transpuesta_atajo_copy = matriz.T.copy()
matriz_transpuesta_metodo_copy = np.transpose(matriz).copy()

comprueba_shared_atajo_copy = np.shares_memory(matriz, matriz_transpuesta_atajo_copy)
comprueba_shared_metodo_copy = np.shares_memory(matriz, matriz_transpuesta_metodo_copy)

print(comprueba_shared_atajo_copy)
print(comprueba_shared_metodo_copy)


print(f"""
- MATRIZ ORIGINAL:
{matriz}

- MATRIZ TRANSPUESTA:
{matriz_transpuesta_metodo_copy}


- "Comprueba qué ocurre con los elementos de la diagonal principal"

La diagonal principal es la que empieza en [0, 0] (y solo sirve para series de mismos numero de componetes en la matriz).
Una de las propiedades de estas matrices con igual número de posiciones en cada serie es que, al transponerla, NUNCA cambia su diagonal principal.
Podemos verlo con np.diag()

{np.diag(matriz)}

{np.diag(matriz_transpuesta_atajo_copy)}

""")

matriz_no_simetrica = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90], [100, 110, 120]])
no_simetrica_transpuesta = matriz_no_simetrica.T.copy()

print(matriz_no_simetrica)
print(np.diag(matriz_no_simetrica))

print(no_simetrica_transpuesta)
print(np.diag(no_simetrica_transpuesta))
