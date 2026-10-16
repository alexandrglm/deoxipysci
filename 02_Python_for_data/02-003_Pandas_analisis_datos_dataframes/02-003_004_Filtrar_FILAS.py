import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2],
    "ventas" : [60, 105, 24, 40, 126, 135, 60]
})

ventas_indizadas = pd.DataFrame({
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2],
    "ventas" : [60, 105, 24, 40, 126, 135, 60]
}, index=["A", "B", "C", "D", "E", "F", "G"])


# filtros simples
precio_mayor_15 = ventas[ ventas["precio"] > 15 ]
print(precio_mayor_15)


# Filtros combinados

## Precios mayores a 15 de artículo con 4 o más unidades
precio_mayor_15_4_unidades = ventas[
    ( ventas["precio"] > 15 )
    &
    ( ventas["unidades"] >= 4 )
]

print(precio_mayor_15_4_unidades)


# Filtrar por valores de una columna

# .isin( ["x", "y", ...] )
print("\n\n- .isin( [] ) - Valores EXACTOS que le indiques:")
print( ventas[ ventas["producto"].isin( ["A", "G", "B"] ) ] )

# .between(x,y)
print("\n- .between( [] ) - Valores que están ENTRE un intervalo, INCLUYENDO AMBOS EXTREMOS:")
print( ventas[ ventas["precio"].between( 12, 20)] )
