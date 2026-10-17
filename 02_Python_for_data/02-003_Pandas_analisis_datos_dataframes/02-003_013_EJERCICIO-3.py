# EJERCICIO 3
"""
### Ejercicio 3: Filtros

Obtén las filas con un importe superior a 50 € y, 
por separado, las que tengan un precio de al menos 12 € y 3 o más unidades.

Aparte, extrae una selección de:
- La fila del producto C
- Filas 3 por posición
- Filas 3 y 4 y Columnas Producto e Importe

Recoge la columa producto y usála como índice

Crea un nuevo DataFrame columna con indice personalizado, de la A a la G, y esto datos
    "precio" : [20, 15, 12, 10, 7, 3, 100]
    "unidades" : [3, 7, 2, 4, 15, 9, 3]

"""
import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D"],
    "precio" : [20, 15, 12, 10],
    "unidades" : [3, 7, 2, 4]
})
ventas["importe"] = ventas["precio"] * ventas["unidades"]
print(ventas)

# importe > 50
ventas_importe_50 = ventas[ ventas["importe"] > 50 ]
print(ventas_importe_50)

# precio >=12 & unidades >= 3
ventas_precio_12_unidades_3 = ventas[ 
    (ventas["precio"] >= 12) & (ventas["unidades"] >= 3)
]
print(ventas_precio_12_unidades_3)


# loc, iloc
ventas_fila_producto_c = ventas.loc[2]
print(ventas_fila_producto_c)

ventas_filas_posicion_3 = ventas.iloc[2]
print(ventas_filas_posicion_3)

ventas_posicion_3_4_columnas_precio_importe = ventas.iloc[2:4, [1,3]]
print("\n -----")
print(ventas_posicion_3_4_columnas_precio_importe)


# pasar producto a indice
ventas_set_index_producto = ventas.set_index("producto")
print(ventas_set_index_producto)

# index="producto"
ventas_indizadas_creado = pd.DataFrame({
    "precio" : [20, 15, 12, 10, 7, 3, 100],
    "unidades" : [3, 7, 2, 4, 15, 9, 3]
}, index=["A", "B", "C", "D", "E", "F", "G"])

print(ventas_indizadas_creado)