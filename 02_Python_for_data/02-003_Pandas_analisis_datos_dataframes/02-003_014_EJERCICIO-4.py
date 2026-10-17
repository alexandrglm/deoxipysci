# EJERCICIO 4
"""
### Ejercicio 4: `groupby()`

Utiliza este conjunto de datos:

```python
datos = pd.DataFrame({
    "categoria": ["Hardware", "Software", "Hardware",
                  "Software", "Hardware"],
    "importe": [100, 200, 150, 300, 50]
})
```

Agrupa por categoría 
- calcula el importe total, la media y el número de registros de cada categoría.
"""
import pandas as pd

datos = pd.DataFrame({
    "categoria": ["Hardware", "Software", "Hardware", "Software", "Hardware"],
    "importe": [100, 200, 150, 300, 50]
})

datos_group_sum = datos.groupby("categoria").sum()
datos_group_mean = datos.groupby("categoria").mean()
datos_group_count = datos.groupby("categoria").count()

print(datos_group_sum)
print(datos_group_mean)
print(datos_group_count)
