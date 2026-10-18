import pandas as pd
import math

datos = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108],
        "categoria": [ "Hardware", "Software", "Hardware", "Software", "Hardware", "Software", "Hardware", "Software"],
        "region": ["Norte", "Sur", "Norte", "Este", "Sur", "Norte", "Este", "Sur"],
        "precio": [120, 80, 150, 100, 90, 200, 110, 80],
        "unidades": [2, 5, 1, 3, 4, 2, 3, 6]
    }
)


heredoc = """
1. Muestra el DataFrame y consulta sus dimensiones.
2. Obtén los nombres de las columnas y los tipos de datos.
3. Utiliza `info()` y `describe()` para inspeccionar la información disponible.
4. Comprueba si existen valores nulos y registros duplicados. (ESTO NO SE HA EXPLICADO EN LA TEORIA)
5. Comprueba si la columna `id` contiene identificadores duplicados.
"""
print(heredoc)

print(datos)
print(datos.ndim)

print(datos.dtypes)

print(datos.info())
print(datos.describe())


# 4. NaN, Null, duplicados
"NO SE HA EXPLICADO EN LA TEORIA !!!!"

print(datos.isna().sum())
print(datos.isnull().sum())

print(datos.duplicated().sum())


# 5.
print(datos["id"].duplicated().sum())
print(datos["id"].is_unique)

print(datos["categoria"].duplicated().sum())
print(datos["categoria"].duplicated())

print(datos["region"].duplicated().sum())
print(datos["region"].duplicated())


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
print(region_categoria_agg_varios_indices)import numpy as np
import pandas as pd
import math

heredoc = """
### Ejercicio 5 --> NumPy y análisis numérico

Objetivo: aplicar NumPy a los datos numéricos extraídos del DataFrame.

1. Convierte la columna `importe` en un array de NumPy.
2. Calcula su media, desviación estándar, mínimo y máximo.
3. Selecciona mediante indexación booleana los importes superiores a la media.
4. Calcula qué porcentaje del importe total representa cada operación.
5. Comprueba si los resultados de suma y media coinciden con los obtenidos mediante pandas, teniendo en cuenta las convenciones utilizadas para calcular la desviación estándar.

> [!NOTE] Comparación entre bibliotecas
>
> NumPy y pandas ofrecen operaciones similares, pero sus estructuras y algunas convenciones difieren. En particular, revisa el parámetro `ddof` de la desviación estándar: el valor predeterminado de NumPy no coincide con el de pandas.
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

# 1. Convierte la columna `importe` en un array de NumPy.
importe_array = np.array(datos["importe"])

print(importe_array)
print(type(importe_array))

# 2. Calcula su media, desviación estándar, mínimo y máximo.
mean = importe_array.mean()
std = importe_array.std()
min = importe_array.min()
max = importe_array.max()
sum = importe_array.sum()

print(mean)
print(std)
print(min)
print(max)
print(sum)

# 3. Selecciona mediante indexación booleana los importes superiores a la media.

importes_mayor_mean = importe_array > mean
print(importes_mayor_mean)

# 4. Calcula qué porcentaje del importe total representa cada operación.

importe_array_compound_modo_1 = importe_array / importe_array.sum()  * 100
print(importe_array_compound_modo_1)
print(importe_array_compound_modo_1.sum())

# 5. Comprueba si los resultados de suma y media coinciden con los obtenidos mediante pandas, teniendo en cuenta las convenciones utilizadas para calcular la desviación estándar.
datos_importe_check = datos["importe"].describe()

def comprueba_datos(valor_uno, valor_dos):
    
    test = valor_uno == valor_dos
    return test

datos_importe_sum = datos["importe"].sum()
datos_importe_mean = datos["importe"].mean()

print(datos_importe_check)
print(comprueba_datos(datos_importe_sum, sum))
print(comprueba_datos(datos_importe_mean, mean))


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
