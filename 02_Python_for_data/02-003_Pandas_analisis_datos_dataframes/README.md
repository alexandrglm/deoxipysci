# Bloque 3 - `pandas`: análisis de datos con DataFrames

> [!IMPORTANT]
> **NumPy** trabaja muy bien con **arrays numéricos**.  
> **pandas** añade una **estructura tabular** con nombres de columnas, índices, datos de distintos tipos, filtros y agrupaciones.  

## Objetivo

- Crear e inspeccionar un `DataFrame`.
- Diferenciar `Series` y `DataFrame`.
- Seleccionar columnas y filas.
- Crear columnas calculadas mediante **operaciones vectorizadas**.
- Filtrar con condiciones simples y combinadas.
- Ordenar y calcular estadísticas.
- Agrupar por categorías y obtener agregaciones con `groupby()`.

El siguiente bloque será: **mini proyecto de análisis de ventas**, integrando Python, NumPy y pandas sobre el mismo conjunto de datos.

---

## 3.1. ¿Qué es un `DataFrame`?

Un `DataFrame` es una **tabla bidimensional con filas y columnas etiquetadas**. Puedes imaginarlo como una hoja de cálculo, pero manipulable mediante Python.

Vamos a reutilizar el ejemplo ventas:

```python
import pandas as pd

ventas = pd.DataFrame({
    "producto": ["A", "B", "C", "D"],
    "precio": [20, 15, 12, 10],
    "unidades": [3, 7, 2, 4]
})

print(ventas)
```

Resultado:

```text
  producto  precio  unidades
0        A      20         3
1        B      15         7
2        C      12         2
3        D      10         4
```

El **índice** de la izquierda (`0`, `1`, `2`, `3`) identifica las filas. **No es una columna ordinaria**, aunque puede convertirse en una.

Comprueba las propiedades:

```python
print(type(ventas))
print(ventas.shape)
print(ventas.columns)
print(ventas.dtypes)
print(ventas.info())
print(ventas.describe())
```

Debes conocer estas herramientas:

| Propiedad o método | Para qué sirve                                   |
| ------------------ | ------------------------------------------------ |
| `shape`            | Dimensiones de la tabla: filas y columnas.       |
| `columns`          | Nombres de las columnas.                         |
| `dtypes`           | Tipo de datos de cada columna.                   |
| `info()`           | Resumen de columnas, tipos y valores no nulos.   |
| `describe()`       | Estadísticas descriptivas de columnas numéricas. |
| `head()`           | Muestra las primeras filas.                      |
| `tail()`           | Muestra las últimas filas.                       |

> [!NOTE]
> `info()` **imprime** un resumen y **devuelve `None`**; no es un método que debas usar esperando obtener un DataFrame.

---

## 3.2. Seleccionar columnas

Una sola columna:

```python
precios = ventas["precio"]

print(precios)
print(type(precios))
```

El resultado es una **`Series`**, una estructura unidimensional de pandas.

Varias columnas:

```python
seleccion = ventas[["producto", "unidades"]]

print(seleccion)
print(type(seleccion))
```

Ahora el resultado es otro **`DataFrame`**.

> [!IMPORTANT]
> Esta distinción importa:
>
> - `ventas["precio"]` devuelve una **`Series`**.
> - `ventas[["precio"]]` devuelve un **`DataFrame`** con una columna.

Para crear una nueva columna:

```python
ventas["importe"] = ventas["precio"] * ventas["unidades"]

print(ventas)
```

Resultado:

```text
  producto  precio  unidades  importe
0        A      20         3       60
1        B      15         7      105
2        C      12         2       24
3        D      10         4       40
```

Fíjate en que la operación es **vectorizada**: no necesitamos recorrer las filas mediante un `for`.

---

## 3.3. Seleccionar filas con `loc` e `iloc`

Estos dos métodos son importantes:

- **`loc`**: selecciona mediante **etiquetas** del índice y nombres de columnas.
- **`iloc`**: selecciona mediante **posiciones enteras**.

```python
# Fila cuyo índice es 1
print(ventas.loc[1])

# Segunda fila por posición
print(ventas.iloc[1])

# Filas por posición y columnas por posición
print(ventas.iloc[0:2, 0:2])
```

Si el índice es el habitual (`0`, `1`, `2`, `3`), algunos resultados parecen idénticos. Sin embargo, si cambias el índice, la diferencia se vuelve importante.

Por ejemplo:

```python
ventas_indizadas = ventas.set_index("producto")

print(ventas_indizadas.loc["B"])
print(ventas_indizadas.iloc[1])
```

En el primer caso buscas la **etiqueta** `"B"`; en el segundo, la **segunda fila**.

---

## 3.4. Filtrar filas

Supongamos que queremos encontrar las ventas cuyo importe sea superior a 50 €:

```python
ventas_mayores_50 = ventas[ventas["importe"] > 50]

print(ventas_mayores_50)
```

Resultado: los productos **A** y **B**.

Podemos combinar condiciones:

```python
filtro = (
    (ventas["precio"] >= 12)
    & (ventas["unidades"] >= 3)
)

print(ventas[filtro])
```

Para combinar condiciones:

- `&` significa **AND**.
- `|` significa **OR**.
- `~` **niega** una condición.

> [!WARNING]
> En pandas, **no utilices `and` u `or`** directamente para combinar comparaciones vectorizadas de Series. Emplea `&` y `|`, con **paréntesis alrededor de cada comparación**.

### Filtrar por valores de una columna

```python
print(ventas[ventas["producto"].isin(["A", "C"])])
print(ventas[ventas["precio"].between(12, 20)])
```

- `isin()` comprueba si cada valor pertenece a una colección.
- `between()` selecciona los valores que se encuentran dentro de un intervalo, **incluyendo ambos extremos por defecto**.

---

## 3.5. Ordenar y agregar datos

Para ordenar por importe descendente:

```python
ordenadas = ventas.sort_values(
    by="importe",
    ascending=False
)

print(ordenadas)
```

Para calcular estadísticas de una columna:

```python
print(ventas["importe"].sum())   # 229
print(ventas["importe"].mean())  # 57.25
print(ventas["importe"].max())   # 105
print(ventas["importe"].min())   # 24
```

Y para obtener estadísticas de varias columnas:

```python
print(ventas[["precio", "unidades", "importe"]].mean())
```

Esto calcula la media de cada columna numérica seleccionada.

---

## 3.6. Agrupar datos con `groupby()`

> [!IMPORTANT]
> `groupby()` es **una de las herramientas más importantes de pandas**. Permite agrupar filas por una categoría y calcular estadísticas para cada grupo.

Imagina que tenemos más ventas, con productos repetidos:

```python
ventas = pd.DataFrame({
    "producto": ["A", "B", "A", "C", "B", "A"],
    "precio": [20, 15, 20, 12, 15, 20],
    "unidades": [3, 7, 2, 2, 4, 1]
})

ventas["importe"] = ventas["precio"] * ventas["unidades"]
```

Agrupar por producto y sumar los importes:

```python
facturacion = ventas.groupby("producto")["importe"].sum()

print(facturacion)
```

Resultado:

```text
producto
A    120
B    165
C     24
```

¿Por qué?

- **A**: $60+40+20=120$
- **B**: $105+60=165$
- **C**: $24$

Puedes calcular varias métricas a la vez:

```python
resumen = ventas.groupby("producto").agg(
    unidades_totales=("unidades", "sum"),
    facturacion=("importe", "sum"),
    importe_medio=("importe", "mean"),
    numero_ventas=("importe", "count")
)

print(resumen)
```

Esto es especialmente útil para informes, análisis exploratorio de datos y preparación de conjuntos de datos para modelos de aprendizaje automático.

> [!NOTE]
> Una diferencia que conviene tener clara: **`count`** cuenta valores **no nulos** en la columna seleccionada, mientras que **`size`** cuenta **filas** del grupo, aunque haya valores nulos.

---
