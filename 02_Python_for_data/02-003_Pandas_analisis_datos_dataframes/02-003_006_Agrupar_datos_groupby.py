import pandas as pd 

ventas_productos_repetidos = pd.DataFrame({
    "producto" : ["A", "B", "A", "C", "B", "A"],
    "precio" : [20, 15, 20, 12, 15, 20],
    "unidades" : [3, 7, 2, 2, 4, 1]
})

print(ventas_productos_repetidos)

ventas_productos_repetidos["ventas"] = ventas_productos_repetidos["precio"] * ventas_productos_repetidos["unidades"]

print(ventas_productos_repetidos)


# groupby()[].method()
facturacion = ventas_productos_repetidos.groupby("producto")["ventas"].sum()

print(facturacion)

# groupby() para ETL, aunar filas repetidas
ventas_consolidadas = ventas_productos_repetidos.groupby(
    [ "producto", "precio" ],
    as_index=False
).sum()

print(ventas_consolidadas)


# .groubby().agg(), varias metricas a la vez, en un nuevo Datafrase

resumen_varias_metricas = ventas_productos_repetidos.groupby("producto").agg(

    unidades_totales = ("unidades", "sum"),
    facturacion = ("ventas", "sum"),
    precio_medio = ("precio", "mean"),
    numero_ventas = ("unidades", "count")
)

print(resumen_varias_metricas)