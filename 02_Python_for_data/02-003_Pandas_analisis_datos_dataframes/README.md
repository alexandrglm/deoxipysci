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
- 1. Tipo:  <class 'pandas.core.frame.DataFrame'>

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
> `info()`  **SIN print(), imprime** un resumen y **usando PRINT, devuelve `None`**; no es un método que debas usar esperando obtener un DataFrame.

---

## 3.2. Seleccionar columnas

### Una sola columna:

```python
precios = ventas["precio"]

print(precios)
print(type(precios))
```

El resultado es una **`Series`**, una estructura **unidimensional** de pandas.

- 1. Tipo:  <class 'pandas.core.series.Series'>

### Varias columnas

```python
seleccion = ventas[["producto", "unidades"]]

print(seleccion)
print(type(seleccion))
```

Ahora el resultado vuelve a ser otro **`DataFrame`**.
- 1. Tipo:  <class 'pandas.core.frame.DataFrame'>

> [!IMPORTANT]
> Esta distinción importa:  
>  
> - `ventas["precio"]` devuelve una **`Series`**.  
>       <class 'pandas.core.series.Series'>    
>
> - `ventas[["precio"]]` devuelve un **`DataFrame`** con una columna.  
>       <class 'pandas.core.frame.DataFrame'>  


### Crear columnas

Para crear una nueva columna, por ejemplo, vectorizando operaciones:

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

## 3.3. Seleccionar filas con `.loc[:]` e `.iloc[:]`

Estos dos métodos son importantes:

- **`loc`**: selecciona mediante **etiquetas** del índice y **nombres de columnas**.
- **`iloc`**: selecciona mediante **posiciones enteras**, directamente con indices, rangos. Es muy muy personalizable.

```python
# Fila cuyo índice es 1
print(ventas.loc[1])

# Segunda fila por posición
print(ventas.iloc[1])

# Filas por posición y columnas por posición
print(ventas.iloc[0:2, 0:2])
```

### Ajustando los índices, `.set_index()`

> [!IMPORTANT]
> **`.set_index()`** coge una columna existente, **la saca de las columnas de datos** y la mueve al lateral izquierdo para convertirla en el **Índice oficial** (las etiquetas de las filas), reemplazando a los números automáticos (`0`, `1`, `2`, `3`...).

> [!NOTE]  
> **A efectos de ETL / Modelado de Datos:**  
>  
> Hacer un `.set_index()` equivale estrictamente a **definir una Clave Primaria (Primary Key)** o un identificador único en una tabla de base de datos o modelo analítico.  
>  
> Pasas de un modelo secuencial (donde los datos se localizan por su número de línea físico) a un modelo relacional o de búsqueda por clave de negocio (buscar por el ID o nombre del producto, como harías con un `VLOOKUP` o un `JOIN`).

Si el índice es el habitual (`0`, `1`, `2`, `3`, ...), usar `.loc` y `.iloc` puede parecer que hace lo mismo. Sin embargo, al cambiar el índice por una columna de negocio, la diferencia se vuelve vital.

Por ejemplo:

```python
ventas_indizadas = ventas.set_index("producto")

print(ventas_indizadas.loc["B"])
print(ventas_indizadas.iloc[1])

```

* En el primer caso (`.loc["B"]`) buscas la **etiqueta de texto** exacta (`"B"`), usando tu nueva clave primaria.
* En el segundo caso (`.iloc[1]`) buscas estrictamente la **segunda posición** física de la fila en la tabla.

Al coincidir que la `"B"` está en la segunda línea, ambos devuelven **mismos datos**, pero con lógicas de búsqueda totalmente diferentes.

#### Crear un DataFrame con índices personalizados desde cero

Si desde el principio quieres construir la tabla ya indizada (sin tener que crear una columna extra y aplicar `.set_index()` después), puedes pasarle el parámetro `index=` directamente a `pd.DataFrame()`:  

```python
ventas_indizadas = pd.DataFrame({
    "precio": [20, 15, 12, 10, 14, 27, 30],
    "unidades": [3, 7, 2, 4, 9, 5, 2],
    "ventas": [60, 105, 24, 40, 126, 135, 60]
}, index=["A", "B", "C", "D", "E", "F", "G"])
```
De esta forma, las letras (o lo que estimes) actúan como la clave primaria de la estructura desde el primer momento, dejando las columnas de datos limpias a la derecha.  
---

## 3.4. Filtrar filas

- Supongamos que queremos encontrar los precios cuyo importe sea superior a 15 €:

```python
ventas_mayores_15 = ventas[ventas["importe"] > 15]

print(ventas_mayores_15)
```

Resultado: los productos **A**, **F** y **G**.  

- Podemos combinar condiciones:

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
> En pandas, **no utilices `and` u `or`** directamente para combinar comparaciones vectorizadas de Series. Emplea SIEMPRE su símbolos`&` y `|`, con **paréntesis alrededor de cada comparación**.  
>  
> Sintáxis:     
>   filtrado = dataframe[ ( dataframe["COLUMNA"] CONDICION )   EVALUADOR   ( dataframe["COLUMNA"] CONDICION ) ]      



### Filtrar por valores de una columna

```python
print(ventas[ ventas["producto"].isin(["A", "C"])])
print(ventas[ventas["precio"].between(12, 20)])

```

#### 1. `.isin( [ "x", "y", ... ] )` - Pertenencia a un conjunto (Filtro por lista)

Comprueba elemento a elemento si el valor de la celda se encuentra dentro de una **lista cerrada de opciones**.  

Útil cuando quieres **filtrar por múltiples valores discretos exactos** (códigos de producto, categorías, IDs de cliente) **sin tener que encadenar una infinidad de condiciones** con `or` (`|`).  

- **Equivalente en ETL / SQL -->** Equivale exactamente a la cláusula **`WHERE columna IN ('A', 'G', 'B')`**.


```python
# Selecciona las filas donde el producto sea exactamente "A", "G" o "B"
print(ventas[ ventas["producto"].isin(["A", "G", "B"]) ])

```


#### 2. `.between(x, y)` - Filtrar por intervalos numéricos o temporales

Seelecciona los valores que se encuentran **dentro de un rango continuo delimitado** por un límite inferior (`x`) y un límite superior (`y`).  

* **Por defecto es nclusivo en ambos extremos** (`inclusive="both"`), es decir, coge tanto el `12` como el `20` si están en los límites.   
    - (Nota mental: en versiones modernas de Pandas puedes ajustar esto con el parámetro `inclusive` si solo quieres que sea abierto por un lado).*
    - Ideal para rangos de precios, franjas de edad, cantidades de stock o rangos de fechas.

* **Equivalente en ETL / SQL --> ** Equivale a la cláusula **`WHERE precio BETWEEN 12 AND 20`**.  


```python
# Selecciona los productos cuyo precio esté entre 12 y 20 (ambos inclusive)
print(ventas[ ventas["precio"].between(12, 20) ])

```

---

## 3.5. Ordenar y agregar datos

### .sort_values()

Para ordenar por valores de COLUMNA, descendente, o ascendente (por defecto):  

```python
ventas_sort_values = ventas.sort_values(

    by="producto",
    ascending=False
)

print(ventas_sort_values)
```
```text
  producto  precio  unidades  ventas
6        G      30         2      60
5        F      27         5     135
4        E      14         9     126
3        D      10         4      40
2        C      12         2      24
1        B      15         7     105
0        A      20         3      60
```

### .sort_index()

Para ordenar por los índices, la forma más básica también es manejando el ascendente booleano:  

```python
ventas_sort_index = ventas.sort_index(
    ascending=False
)

print(ventas_descending)
```
```text
  producto  precio  unidades  ventas
6        G      30         2      60
5        F      27         5     135
4        E      14         9     126
3        D      10         4      40
2        C      12         2      24
1        B      15         7     105
0        A      20         3      60
```


### Operaciones algebráicas para UNA columna


Para calcular estadísticas de una columna:  

```python
ventas_ventas_sum = ventas["ventas"].sum()
ventas_ventas_mean = ventas["ventas"].mean()
ventas_ventas_max = ventas["ventas"].max()
ventas_ventas_min = ventas["ventas"].min()

print("\n - sum() de ventas por producto:  ", ventas_ventas_sum,
      "\n - mean() de ventas por producto: ", ventas_ventas_mean,
      "\n - max() de ventas por producto:  ", ventas_ventas_max,
      "\n - min() de ventas por producto:  ", ventas_ventas_min)
```
```
 - sum() de ventas por producto:   550 
 - mean() de ventas por producto:  78.57142857142857 
 - max() de ventas por producto:   135 
 - min() de ventas por producto:   24
```

### Operaciones algebráicas sobre VARIAS columnas

Con una operación algebráica sobre varias columnas, podemos obtener una Series con estadísticas.  

Por ejemplo, la media de precios de producto, media de stock y de ventas por productos a la vez:  

```python
ventas_mean_por_columnas = ventas[  ["precio", "unidades", "ventas" ] ].mean()

print(ventas_mean_por_columnas)
```

Esto calcula la media de cada columna numérica seleccionada.  

```text
precio      18.285714
unidades     4.571429
ventas      78.571429
dtype: float64
```


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


### Agrupar por valores iguales de una columna - `.groupby()`

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

* **A**:    $60+40+20=120$
* **B**:    $105+60=165$
* **C**:    $24$

#### Agrupar por múltiples columnas y mantener la tabla plana (`as_index=False`)

Si necesitas agrupar por más de una columna (por ejemplo, producto y precio) y quieres que el resultado **siga siendo un DataFrame plano** (sin que las columnas de agrupación se conviertan en índices multinivel), utilizas el parámetro **`as_index=False`**:

```python
ventas_consolidadas = ventas_productos_repetidos.groupby(
    [ "producto", "precio" ],
    as_index=False
).sum()

print(ventas_consolidadas)

```

> [!NOTE]
> **A efectos de ETL / SQL:**
> Esto equivale exactamente a un `GROUP BY columna1, columna2` en SQL. El parámetro `as_index=False` evita que las claves de agrupación suban al índice lateral, manteniendo la estructura de columnas limpia para seguir operando o exportando los datos.

---

### .agg() -  Varias metricas a la vez
Puedes calcular varias métricas a la vez usando `.agg()`:

```python
resumen = ventas.groupby("producto").agg(
    unidades_totales = ("unidades", "sum"),
    facturacion = ("ventas", "sum"),
    precio_medio = ("precio", "mean"),
    numero_ventas = ("unidades", "count")
)

print(resumen)

```
```text
          unidades_totales  facturacion  precio_medio  numero_ventas
producto                                                            
A                        6          120          20.0              3
B                       11          165          15.0              2
C                        2           24          12.0              1
```

Esto es especialmente útil para informes, análisis exploratorio de datos y preparación de conjuntos de datos para modelos de aprendizaje automático.  

> [!NOTE]
> Una diferencia que conviene tener clara: **`count`** cuenta valores **no nulos** en la columna seleccionada, mientras que **`size`** cuenta **filas** totales del grupo, aunque haya valores nulos.  


---
