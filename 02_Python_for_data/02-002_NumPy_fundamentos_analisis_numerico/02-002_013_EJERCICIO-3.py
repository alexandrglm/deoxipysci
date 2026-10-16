# EJERCICIO 3
heredoc = """
Ejercicio 3 --> Filtrado

Dado `valores = np.array([12, 55, 31, 80, 42, 9])`
 - Ordena ascentende
 - Selecciona solo los valores superiores o iguales a 40

Crea otro array con valores entre 1 y 20

 - Selecciona solo superiores o iguales a 40 de un array
 - Selecciona solo los pares del nuevo array
 - Haz un join del primer resultado con el segundo a un nuevo array
"""
print(heredoc)

import numpy as np

valores = np.array( [12,55,31,80,42,9 ] )

valores_ordenados = np.sort(valores)
print(valores_ordenados)


condicion_valores = valores >= 40
valores_filtrados = valores[condicion_valores]
print(valores_filtrados)

mas_valores = np.arange(1, 21, 1)
print(mas_valores)

mas_valores_pares_condicion = mas_valores % 2 == 0

mas_valores_pares = mas_valores[mas_valores_pares_condicion]
print(mas_valores_pares)


union = np.append(valores_filtrados, mas_valores_pares)

print(union)

# CORRECCION DETALLADA
"""
- np.append() devuelve un nuevo array; no modifica el original 

- Para unir arrays, también puedes utilizar np.concatenate((array1, array2)), 
que deja explícita la operación de concatenación

- También np.hstack(), aunque trabajará en filas, para matrices


"""
print("\n ----- CORRECCION DETALLADA de UNIONES--- \n")

array_np_uno = np.array([20, 30, 35, 40])
array_np_dos = np.array([100, 300, 400, 600])

print("Originales:", array_np_uno, "y", array_np_dos)

# 1. CONCATENATE
## Une los arrays de cabeza a cola en una sola línea (mantiene 1D pero más largo)
array_concatenate = np.concatenate([array_np_uno, array_np_dos])
print("\nCONCATENATE = Simple join. Alarga la línea 1D: \n   ", array_concatenate)

# 2. APPEND (¡Cuidado con la trampa!)
## Si no le dices el eje, aplasta los arrays y te devuelve un único array plano 1D gigante.
array_append = np.append(array_np_uno, array_np_dos)
print("\nAPPEND = Aplasta y linealiza (a menos que le indiques un axis): \n   ", array_append)

# 3. VSTACK (Vertical Stack)
## Apila los arrays 1D uno ENCIMA de otro. Cada uno se convierte en una FILA.
union_vstack = np.vstack([array_np_uno, array_np_dos])
print("\nVSTACK = Matriz creciendo hacia ABAJO (Apila filas verticalmente): \n   ", union_vstack)


# 4. HSTACK (Horizontal Stack)
## Para hstack necesitas arrays con forma de columna (2D con shape tipo (4,1))
array_para_hstack_uno = np.array([[20], [30], [35], [40]])
array_para_hstack_dos = np.array([[100], [300], [400], [600]])

union_hstack = np.hstack([array_para_hstack_uno, array_para_hstack_dos])
print("\nHSTACK = Matriz creciendo hacia LOS LADOS (Pega columnas horizontalmente): \n   ", union_hstack)