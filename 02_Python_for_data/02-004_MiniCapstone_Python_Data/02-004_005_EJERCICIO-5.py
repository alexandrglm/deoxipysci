import numpy as np
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


