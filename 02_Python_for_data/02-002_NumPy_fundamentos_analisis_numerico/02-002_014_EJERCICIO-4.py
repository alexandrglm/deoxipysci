# EJERCICIO 4
heredoc = """
Ejercicio 4 --> Matrices y ejes

Crea esta matriz y calcula la suma de cada columna y de cada fila:

[ [2, 4, 6], [1, 3, 5] ]

 - Explica bien los axis
"""
import numpy as np

matriz = np.array( [
    [2,4,6],
    [1,3,5]
])


crea_rango_para_complicados_de_la_vida = np.arange(1,8,1)

condicion_rango_valido = crea_rango_para_complicados_de_la_vida[
    (crea_rango_para_complicados_de_la_vida >=1 ) 
    & 
    (crea_rango_para_complicados_de_la_vida < 7)
]
print(condicion_rango_valido)

condicion_impar = condicion_rango_valido[
    (condicion_rango_valido % 2 != 0)
]
print(condicion_impar)

condicion_par = condicion_rango_valido[
    (condicion_rango_valido % 2 == 0)
]
print(condicion_par)

matriz_para_complicados = np.array([condicion_par, condicion_impar])
print(matriz)
print(matriz.dtype)
print(matriz_para_complicados)
print(matriz_para_complicados.dtype)

matriz_para_complicados_vertical_stack = np.array([condicion_par, condicion_impar])
print(matriz_para_complicados_vertical_stack)
print(matriz_para_complicados_vertical_stack.dtype)


suma_eje_cero = matriz.sum(axis=0)
suma_eje_uno = matriz.sum(axis=1)

print("\n- Sumas de axis = 0 : ", suma_eje_cero)
print("    Con axis 0 le pedimos que colapse la primera posición del shape,")
print("    es decir, COLAPSA HACIA ABAJO, se come las filas, sumándolas en este caso.")

print("\n- Sumas de axis = 1 : ", suma_eje_uno)
print("    Con axis 1 le pedimos que colapse la segunda posición del shape,")
print("    es decir, COLAPSA A LOS LADOS, se come las columnas, sumándolas en este caso.")
print("\n     OJO! El ejercicio pide crear matriz con pares e impares, para que al hacer axis 1 duela a la vista ver [12 9] en vez de [9 12]")
# primer_array_temp = (crea_rango_para_complicados_de_la_vida >= 1) & (crea_rango_para_complicados_de_la_vida < 7)
# primer_array = (primer_array_temp % 2 != 0 )

# segundo_array_temp = (crea_rango_para_complicados_de_la_vida >= 2) & (crea_rango_para_complicados_de_la_vida < 7)
# segundo_array = (segundo_array_temp % 2 == 0)

# print(primer_array)
# print(segundo_array)


# CORRECCION DETALLADA
"""
La explicación de «colapsar» el eje es buena. La formulación más precisa sería:

    - axis=0: reduce el eje de las filas; queda un resultado por columna.
    - axis=1: reduce el eje de las columnas; queda un resultado por fila.

LA matriz adicional de pares e impares tiene una limitación: ambas filas deben tener la misma longitud para construir un array numérico rectangular normal. 

En el ejemplo, los números pares entre 1 y 6 son tres, y los impares también son tres, por lo que funciona. 
Si las longitudes fueran diferentes, NumPy no podría construir de esa forma un array bidimensional numérico regular.
"""