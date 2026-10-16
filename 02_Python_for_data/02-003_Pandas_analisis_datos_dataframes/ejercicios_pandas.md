
### Ejercicio 1: Crear y explorar un DataFrame

Crea un DataFrame con estas columnas y datos:

```python
producto = ["A", "B", "C", "D"]
precio = [20, 15, 12, 10]
unidades = [3, 7, 2, 4]
```

Muestra sus dimensiones, columnas, tipos y las primeras filas.

### Ejercicio 2: Columnas

Añade la columna `importe` y muestra solamente las columnas `producto` e `importe`.

### Ejercicio 3: Filtros

Obtén las filas con un importe superior a 50 € y, por separado, las que tengan un precio de al menos 12 € y 3 o más unidades.

### Ejercicio 4: `groupby()`

Utiliza este conjunto de datos:

```python
datos = pd.DataFrame({
    "categoria": ["Hardware", "Software", "Hardware",
                  "Software", "Hardware"],
    "importe": [100, 200, 150, 300, 50]
})
```

Agrupa por categoría y calcula el importe total, la media y el número de registros de cada categoría.

### Ejercicio 5: Mini análisis

Con el DataFrame del ejercicio 1, calcula la facturación total, el importe medio, el producto con mayor importe y ordena la tabla por importe descendente.

---
