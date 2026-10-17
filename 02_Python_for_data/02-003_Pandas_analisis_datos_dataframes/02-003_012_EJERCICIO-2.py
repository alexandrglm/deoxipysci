# EJERCICIO 2
"""
### Ejercicio 2: Columnas

Añade la columna `importe` y muestra solamente las columnas `producto` e `importe`.
"""
import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D"],
    "precio" : [20, 15, 12, 10],
    "unidades" : [3, 7, 2, 4]
})

ventas_con_importes = ventas["precio"] * ventas["unidades"]

print(ventas_con_importes)

ventas["importe"] = ventas["precio"] * ventas["unidades"]

print(ventas)

ventas_filtradas = ventas[["producto", "importe"]]
print(ventas_filtradas)