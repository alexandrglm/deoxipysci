import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2],
    "ventas" : [60, 105, 24, 40, 126, 135, 60]
})


# .loc[:] - Seleccionar FILAS mediante etiquetas de INDICE y nombres de columnas
print("\n- .loc[i] --> SELECCION por ETIQUETAS DEL INDICE y/o NOMBRES DE COLUMNAS")

## Fila cuyo índice es 1
print("\n .loc[1] - Fila con indice 1 :\n")
print(ventas.loc[1])



print("\n- .iloc[rangos] --> SELECCION por posiciones, INDICES, RANGOS\n   * Es MUY personalizable\n   * Dentro del rango trabajamos [ FILAS, COLUMNAS]\n   * Ej: [2:3, 2:4] = Filas 3 a 4, Columnas 2 a 4\n   * [:, [0, 3, 1]] = Todas las filas, Columnas ordenadas al gusto PRIMERA - CUARTA - TERCERA")

## Segunda fila por posición
print("\n .iloc[1] - Segunda fila por posición :\n")
print(ventas.iloc[1])

## Filas por posición y columnas por posición
print("\n .iloc[0:2, 0:2] - Filas por posición y columnas por posición :\n")
print(ventas.iloc[0:2, 0:2])

print("\n .iloc[:, [0, 3, 1]] - Todas las filas, y columnas ordenadas por preferncia :\n")
print(ventas.iloc[:, [0, 3, 1]])


# set_index
print("\n\n- Ajustando los indices, .set_index()\n")

ventas_indizadas = ventas.set_index("producto")

print(ventas_indizadas)

literalmente = """
          precio  unidades  ventas
producto                          
A             20         3      60
B             15         7     105
C             12         2      24
D             10         4      40
E             14         9     126
F             27         5     135
G             30         2      60
"""
# print(literalmente)


print("\n")
print(ventas_indizadas.loc["B"])
print("\n")
print(ventas_indizadas.iloc[1])


# Crear el dataframe con el index personalizado directamente
print("\n\n- Para crear un DataFrame con el index personalizado ... :\n")
indice_perso = """
    ventas_indizadas = pd.DataFrame({
        "precio": [20, 15, 12, 10, 14, 27, 30],
        "unidades": [3, 7, 2, 4, 9, 5, 2],
        "ventas": [60, 105, 24, 40, 126, 135, 60]
    }, index=["A", "B", "C", "D", "E", "F", "G"])

"""

sintax_indice_perso = """
    dataframe_index_perso = pd.DataFrame(
        {
            "clave 1" : [valor1, valor2, valor3, ...],
            "clave 2" : [valor1, valor2, valor3, ...],
            ...
        
        }, index=["Fila Indice 1", "Fila Indice 2, ...]
    )

"""

print(sintax_indice_perso)
print(indice_perso)
