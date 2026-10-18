import pandas as pd
import numpy as np
import math

heredoc = """
### Ejercicio 6 --> Preparación de resultados para ETL

Objetivo: generar resultados que puedan consumirse en otro sistema.

1. Construye una tabla resumen con la facturación por región.
2. Ordena esa tabla por facturación descendente.
3. Comprueba que la suma de las facturaciones regionales coincide con el total global, dado que cada operación pertenece a una sola región.
4. Exporta el resumen a un CSV sin guardar el índice como una columna adicional.
5. Explica qué parte del proceso corresponde a extracción, transformación y carga en este ejercicio, y qué cambiaría si los datos de origen procedieran de un fichero CSV.
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

# 1. Construye una tabla resumen con la facturación por región.

facturacion_por_region = datos.iloc[:, [2, 5]].groupby("region", as_index=False).sum()
print(facturacion_por_region)

# 2. Ordena esa tabla por facturación descendente.
facturacion_por_region_descending = facturacion_por_region.sort_values(by="importe", ascending=False)
facturacion_por_region_descending_complex = datos.iloc[:, [2, 5]].groupby("region", as_index=True).sum().sort_values(by="importe", ascending=False)
print(facturacion_por_region_descending)
print(facturacion_por_region_descending_complex)


print("\n")
# 3. Comprueba que la suma de las facturaciones regionales coincide con el total global, dado que cada operación pertenece a una sola región.
facturacion_total = datos["importe"].sum()

total_regiones = datos.iloc[:, [2, 5]].groupby("region", as_index=False).sum()

sum_total_regiones = total_regiones["importe"].sum()
def igualdades(valor_uno, valor_dos):
    resultado = valor_uno == valor_dos
    return print(f'{resultado}')

print(facturacion_total)
print(total_regiones)
print(sum_total_regiones)
print("\n")
igualdades(facturacion_total, sum_total_regiones)


print("\n")
# 4. Exporta el resumen a un CSV sin guardar el índice como una columna adicional.

export_df_total_regiones_a_csv = total_regiones.to_csv("./total_regiones_ejercicio_6.csv", index=False)


# 5. Explica qué parte del proceso corresponde a extracción, transformación y carga en este ejercicio, y qué cambiaría si los datos de origen procedieran de un fichero CSV.
heredoc_5 = """
-Extracción de datos, cuando sacamos del DataFrame (de una tabla bidimensional), una de sus colimnas, un array,
para trabajar con el, comparar sus datos. Podríamos haberlos modificado.
También al hacer una tabla resumen, de todos los datos, al resumen de ventas por región, eligiendo qué columnas mostrar y cuales no. Implica extraer y transformar esos datos.
La carga de datos no aplica al 100% a este ejercicio, cuando pensamos en carga pensamos en cargar y usar esos datos, por ejemplo, para visualizaciones.
En este ejercicio podría haber sido las comparaciones de valores concretos, como comparar la media o sumas entre los métodos de Pandas y los de NumPy.

"""
