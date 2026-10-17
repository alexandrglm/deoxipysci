# EJERCICIO 1
"""

### Ejercicio 1: Crear y explorar un DataFrame

Crea un DataFrame con estas columnas y datos:

```python
producto = ["A", "B", "C", "D"]
precio = [20, 15, 12, 10]
unidades = [3, 7, 2, 4]
```

Muestra sus dimensiones, columnas, tipos y las primeras filas.
"""

import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D"],
    "precio" : [20, 15, 12, 10],
    "unidades" : [3, 7, 2, 4]
})

print(ventas)

print("\n - Shape: ", ventas.shape)
print("\n - Dimensiones: ", ventas.ndim)
print("\n - ¿Qué tipos contiene?:\n", ventas.dtypes)

print("\n - Todo acerca de sus columnas:")
print(ventas.columns)

print("\n - Primeras CINCO filas (tiene 4, tanto head() como tail() mostrarían lo mismo):")
print(ventas.head())

print("\n - Distintas métricas con describe()")
print(ventas.describe())

print("\n - Usando el metodo .info():")
print(ventas.info())

