import pandas as pd
import numpy as np
import math

heredoc = """
### Ejercicio 4 --> Agrupación y agregación

Objetivo: obtener indicadores por categoría y región.

1. Agrupa por `categoria` y calcula la facturación total.
2. Agrupa por `region` y calcula el importe medio.
3. Agrupa por `categoria` y calcula simultáneamente:
   - Unidades totales.
   - Facturación total.
   - Importe medio por operación.
   - Número de registros.
4. Repite el análisis agrupando por `region` y `categoria`.
5. Presenta al menos uno de los resultados como un DataFrame con las columnas de agrupación visibles, en lugar de utilizarlas como índice.

> [!INFO] Relación con Power BI y SQL
>
> Estas operaciones se relacionan con las agregaciones de una tabla visual o una matriz de Power BI y con `GROUP BY` en SQL. La elección de las dimensiones y las métricas determina qué resumen obtienes.
>
> Puedes resolver el tercer apartado con `.agg()`. Antes de elegir una función, piensa en qué métrica necesitas y qué columna debe utilizarse para calcularla.
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


# 1
print("\n---------\n")
agrupado_ventas_totales_modo_1_basico = datos.groupby("categoria").sum("importe")

agrupado_ventas_totales_modo_2 = datos.groupby(
    ["categoria"]
).sum("importe")


print(agrupado_ventas_totales_modo_1_basico)
print(agrupado_ventas_totales_modo_2)

# 2
print("\n---------\n")
agg_region = datos.groupby("region", as_index=False).mean("importe")

print(agg_region)

# 3
print("\n---------\n")
categoria_agg_varios = datos.groupby("categoria").agg(
    unidades_totales = ("unidades", "sum"),
    facturacion_total = ("importe", "sum"),
    media_operacion = ("importe", "mean"),
    numero_operaciones = ("unidades", "sum"),
    numero_registros = ("id", "count")
)
print(categoria_agg_varios)

# 4
print("\n---------\n")
region_categoria_agg_varios = datos.groupby(["region", "categoria"]).agg(
    unidades_totales = ("unidades", "sum"),
    facturacion_total = ("importe", "sum"),
    media_operacion = ("importe", "mean"),
    numero_operaciones = ("unidades", "sum"),
    numero_registros = ("id", "count")
)
print("\n---------\n")
print(region_categoria_agg_varios)

# 5
print("\n---------\n")
region_categoria_agg_varios_indices = datos.groupby(["region", "categoria"], as_index=False).agg(
    unidades_totales = ("unidades", "sum"),
    facturacion_total = ("importe", "sum"),
    media_operacion = ("importe", "mean"),
    numero_operaciones = ("unidades", "sum"),
    numero_registros = ("id", "count")
)
print(region_categoria_agg_varios_indices)