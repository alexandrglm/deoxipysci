import pandas as pd
import math
import numpy as np

heredoc = """
Objetivo: crear variables derivadas sin recorrer las filas manualmente.

1. Añade una columna `importe`, calculada a partir de `precio` y `unidades`.
2. Calcula el importe total de todas las operaciones.
3. Calcula el importe medio, el máximo y el mínimo.
4. Obtén la fila correspondiente a la operación con mayor importe.
5. Ordena las operaciones por importe, de mayor a menor.
"""

datos = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108],
        "categoria": [ "Hardware", "Software", "Hardware", "Software", "Hardware", "Software", "Hardware", "Software"],
        "region": ["Norte", "Sur", "Norte", "Este", "Sur", "Norte", "Este", "Sur"],
        "precio": [120, 80, 150, 100, 90, 200, 110, 80],
        "unidades": [2, 5, 1, 3, 4, 2, 3, 6]
    }
)

datos["importe"] = datos["precio"] * datos["unidades"]

facturacion_total = sum(datos["importe"])

datos_describe = datos["importe"].describe()
datos_importe_mean = datos["importe"].mean()
datos_importe_max = datos["importe"].max()
datos_importe_min = datos["importe"].min()

datos_importe_agg = datos.groupby("importe").agg(
    importe_mean = ("importe", "mean"),
    importe_max = ("importe", "max"),
    importe_min = ("importe", "min")

)

filtro_mayor_venta_fila_simple = datos["importe"].max()
filtro_mayor_venta_fila_entera = datos[datos["importe"] > 410 ]

filtro_mayor_venta_loc_idxmax = datos.loc[datos["importe"].idxmax()]
filtro_mayor_venta_comparacion_directa = datos[ datos["importe"] == datos["importe"].max() ]

datos_sort_descending = datos.sort_values(by="importe", ascending=False)

print(datos)
print(facturacion_total)

print(datos_describe)
print(datos_importe_mean)
print(datos_importe_max)
print(datos_importe_min)
print("\n NOTA DE ESTUDIO, agg no es el mejor método para una sola columna, lo pongo solo para recordar su sintaxis\n", datos_importe_agg)

print("\n 4. Fila importe con mayor valor\n  - Hasta aquí, ninguno de estos dos métodos son la forma correcta de hacerlo:")
print(filtro_mayor_venta_fila_simple)
print(filtro_mayor_venta_fila_entera)
print("\n  - A) Con .loc[ DataFrame[COLUMNA].idxmax() ]\n    Funcionará porque importes son numéricos. Devuelve un Series")
print(filtro_mayor_venta_loc_idxmax)
print('\n  - B) Comparando con .max() directamente, DataFrame[ DataFrame["COLUMNA"] == DataFrame["COLUMNA"].max() ]\n    Es la forma más legacy y directa, devuelve un DataFrame')
print(filtro_mayor_venta_comparacion_directa)


print(datos_sort_descending)