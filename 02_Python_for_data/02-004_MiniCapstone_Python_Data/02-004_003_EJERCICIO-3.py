
import pandas as pd
import numpy as np
import math

heredoc = """
### Ejercicio 3 --> Filtrado y selección

Objetivo: seleccionar registros según criterios de negocio.

1. Obtén las operaciones cuyo importe sea superior a 250.
2. Selecciona las operaciones de la región Norte.
3. Selecciona las operaciones de Hardware con al menos dos unidades.
4. Combina una condición de región con una condición numérica.
5. Devuelve únicamente las columnas `id`, `categoria` e `importe` de las operaciones que cumplan una condición.
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
importe_250 = datos[ datos["importe"] > 250 ]
print(importe_250)

# 2
operaciones_norte = datos[ datos["region"] == "Norte" ]
print(operaciones_norte)

# 3
hardware_con_dos = datos[ (datos["categoria"] == "Hardware") & (datos["unidades"] >= 2) ]
print(hardware_con_dos)

# 4
combina_region_numerica = datos[ (datos["region"] == "Sur") & (datos["precio"] > 80)  ]
print(combina_region_numerica)

# 5

pre_combina_condicion_orden = datos.iloc[:, [0, 1, 5]]
combina_condicion_orden = pre_combina_condicion_orden[pre_combina_condicion_orden["importe"] > 200]

modo_directo = (datos[datos["importe"] > 200 ]).iloc[:, [0, 1, 5]]

condicion = "Hardware"
modo_loc_primero_filtro_luego_selecciono = datos.loc[ datos["categoria"] == condicion, ["id", "categoria", "importe"] ]

columnas_objetivo = ["id", "categoria", "importe"]
modo_loc_primero_selecciono_luego_filtro = datos[columnas_objetivo][datos["categoria"] == condicion]

modo_query = datos.query("categoria == 'Hardware' ")[columnas_objetivo]


print(combina_condicion_orden)
print(modo_directo)
print(modo_loc_primero_filtro_luego_selecciono)
print(modo_loc_primero_selecciono_luego_filtro)
print(modo_query)
