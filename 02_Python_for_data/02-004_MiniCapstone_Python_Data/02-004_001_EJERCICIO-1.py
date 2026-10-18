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


