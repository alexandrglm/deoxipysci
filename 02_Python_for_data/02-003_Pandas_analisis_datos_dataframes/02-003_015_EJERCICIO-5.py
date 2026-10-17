# EJERCICIO 5

"""
### Ejercicio 5: Mini análisis

Con el DataFrame del ejercicio 1, 
calcula la facturación total, 
el importe medio, 
el producto con mayor importe 
y ordena la tabla por importe descendente.
"""
import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D"],
    "precio" : [20, 15, 12, 10],
    "unidades" : [3, 7, 2, 4]
})

facturacion_total = (ventas["precio"] * ventas["unidades"]).sum()
print(facturacion_total)

precio_medio = ventas["precio"].mean()
print(precio_medio)

producto_mayor_importe = ventas["precio"].max()

ventas_descending = ventas.sort_values(by="producto", ascending=False)
print(ventas_descending)

ventas_descending_sort_index = ventas.sort_index(ascending=False)
print(ventas_descending_sort_index)