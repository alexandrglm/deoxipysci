## Bloque 2 - NumPy: fundamentos para el análisis numérico

> [!IMPORTANT]
> **NumPy** es una biblioteca de Python para trabajar **eficientemente** con datos numéricos, vectores, matrices y operaciones matemáticas. Es una base importante para comprender el análisis numérico y muchas herramientas de aprendizaje automático.

## Qué debes aprender de este bloque

No hace falta memorizar todas las funciones de NumPy hoy. Lo importante es que puedas:

- Crear **arrays unidimensionales** y **matrices**.
- Comprender `shape`, `ndim` y `dtype`.
- Realizar **operaciones vectorizadas**.
- Seleccionar elementos por **índices** y **condiciones**.
- Entender las dimensiones y el efecto de `axis=0` y `axis=1`.
- Aplicar estas operaciones a un pequeño conjunto de datos.

Al terminar, pasaremos al **bloque 3: pandas**, donde trabajaremos con `DataFrame`, selección de columnas, filtros, nuevas columnas y `groupby()`.

---

## 2.1. ¿Por qué necesitamos NumPy?

Ya sabes trabajar con listas de Python. La pregunta es: ¿qué aporta un array de NumPy?

```python
lista = [10, 20, 30]

print(lista * 2)
# [10, 20, 30, 10, 20, 30]
```

En una lista, multiplicar por dos **repite la lista**. En cambio:

```python
import numpy as np

array = np.array([10, 20, 30])

print(array * 2)
# [20 40 60]
```

En un array, la multiplicación por dos **se aplica a cada elemento**. Esto se llama **operación vectorizada**.

### La diferencia fundamental

**Lista Python**

```python
[10, 20, 30] * 2
# [10, 20, 30, 10, 20, 30]  -> Repite la secuencia.
```

**Array NumPy**

```python
array * 2
# [20, 40, 60]  -> Multiplica cada elemento.
```

> [!IMPORTANT]
> En análisis de datos es habitual aplicar la misma operación a cientos, miles o millones de valores. **NumPy permite hacerlo sin escribir explícitamente un bucle para cada operación.**

---

## 2.2. Crear arrays

Abre un archivo `numpy_basico.py` en VS Code y ejecuta:

```python
import numpy as np

precios = np.array([20, 15, 12, 10])

print(precios)
print(type(precios))
print(precios.dtype)
print(precios.shape)
print(precios.ndim)
```

Conceptos:

- `np.array(...)`: construye un array.
- `type(precios)`: indica que es un objeto `numpy.ndarray`.
- `dtype`: indica el **tipo de datos** almacenado.
- `shape`: indica las **dimensiones** y el tamaño de cada dimensión.
- `ndim`: indica el **número de dimensiones**.

Para este ejemplo, `shape` será `(4,)` y `ndim` será `1`: es un **vector** de cuatro elementos.

### Crear arrays de diferentes formas

```python
import numpy as np

ceros = np.zeros(4)
unos = np.ones(4)

secuencia = np.arange(0, 10, 2)
valores = np.linspace(0, 1, 5)

print(ceros)
# [0. 0. 0. 0.]

print(unos)
# [1. 1. 1. 1.]

print(secuencia)
# [0 2 4 6 8]

print(valores)
# [0.   0.25 0.5  0.75 1.  ]
```

- `np.arange(inicio, fin, paso)`: genera valores separados por un paso determinado, **sin incluir** normalmente el límite final. Devuelve **enteros** o **floats**.
- `np.linspace(inicio, fin, cantidad)`: genera una cantidad concreta de valores espaciados uniformemente, **incluyendo** los extremos por defecto. Devuelve **floats** siempre.

> [!IMPORTANT]
> NumPy suele almacenar los elementos de un array numérico con un **tipo común**, como enteros o números de coma flotante. Esto favorece la **eficiencia** de las operaciones numéricas.

---

## 2.3. Operaciones vectorizadas

Vamos a usar datos de ventas:

```python
precios = np.array([20, 15, 12, 10])
unidades = np.array([3, 7, 2, 4])
importes = precios * unidades

print(importes)         # [ 60 105  24  40]
print(importes.sum())   # 229
print(importes.mean())  # 57.25
```

Observa que multiplicamos **dos arrays elemento a elemento**:

- El primer precio por las primeras unidades.
- El segundo por las segundas.
- Y así sucesivamente.

También podemos aplicar operaciones a todos los valores **directamente**, sin necesidad de bucles:

```python
precios_con_iva = precios * 1.21

precios_con_descuento = precios * 0.90

print(precios_con_iva)
print(precios_con_descuento)
```

- No necesitamos escribir un bucle para calcular cada resultado.
- Repito: **no necesitamos escribir un bucle para calcular cada resultado.**

> [!IMPORTANT]
> Con NumPy **NO NECESITAMOS ESCRIBIR UN BUCLE PARA CALCULAR CADA RESULTADO**.

### Operaciones y funciones frecuentes

| Operación         | Ejemplo             |
| ----------------- | ------------------- |
| Suma              | `np.sum(importes)`  |
| Media             | `np.mean(importes)` |
| Mínimo            | `np.min(importes)`  |
| Máximo            | `np.max(importes)`  |
| Desviación típica | `np.std(importes)`  |
| Raíz cuadrada     | `np.sqrt(importes)` |

> [!NOTE]
> La **desviación típica** mide la dispersión de los valores respecto de la media. Por defecto, `np.std()` utiliza `ddof=0`, es decir, calcula la desviación típica **poblacional**.
> Más adelante veremos cuándo se utiliza la versión **muestral**.

---

## 2.4. Índices y selección

En NumPy, como en las listas de Python, los índices son **zero-based**.

```python
importes = np.array([60, 105, 24, 40])

print(importes[0])
# 60

print(importes[-1])
# 40

print(importes[1:3])
# [105  24]
```

El corte `1:3` **incluye** el índice 1, pero **excluye** el índice 3.

### Filtrado mediante condiciones

Aquí aparece una de las funcionalidades más útiles de NumPy:

```python
importes = np.array([60, 105, 24, 40])
mas_de_50 = importes > 50

print(mas_de_50)
# [ True  True False False]

print(importes[mas_de_50])
# [ 60 105]
```

Podemos combinar la condición directamente:

```python
print(importes[importes > 50])
# [ 60 105]
```

Esto se denomina **indexación booleana**. La condición genera una **máscara** de valores verdaderos y falsos, que después se utiliza para seleccionar los elementos correspondientes.

También puedes combinar condiciones. Usa `&` (ampersand) para **AND** y `|` (pipe) para **OR**, colocando **cada comparación entre paréntesis**:

```python
importes = np.array([60, 105, 24, 40])

print(importes[(importes >= 40) & (importes < 100)])
# [60 40]
```

> [!NOTE]
> Como curiosidad, un ampersand no sirve para hacer joins. Al igual que en legacy, `,` sirve para evaluaciones.

---

## 2.5. Vectores y matrices: dos dimensiones

Hasta ahora hemos trabajado con arrays unidimensionales. Para analizar datos también necesitaremos **matrices**.

```python
datos = np.array([
    [20, 3],
    [15, 7],
    [12, 2],
    [10, 4]
])

print(datos.shape)
# (4, 2)

print(datos.ndim)
# 2
```

Tenemos **cuatro filas y dos columnas**. Podemos interpretar cada fila como un producto y las columnas como precio y unidades.

### Visualización de la matriz

| Producto | Precio | Unidades |
| -------- | ------ | -------- |
| A        | 20     | 3        |
| B        | 15     | 7        |
| C        | 12     | 2        |
| D        | 10     | 4        |

Los nombres de producto se omiten de la matriz numérica para mantener los datos **homogéneos**; se pueden conservar por separado.

Para seleccionar elementos, sintaxis `matriz[x, y]`:

```python
print(datos[0, 0])
# Precio del primer producto: 20

print(datos[1, 1])
# Unidades del segundo producto: 7

print(datos[:, 0])
# Todos los precios

print(datos[:, 1])
# Todas las unidades
```

La sintaxis `datos[fila, columna]` selecciona una posición. El símbolo `:` significa que queremos **todos los elementos de esa dimensión**.

### Operaciones por eje: `axis`

Este concepto aparece mucho en análisis numérico y pandas.

> [!IMPORTANT]
> **REGLA MENTAL**
>
> 1. **`shape` SIEMPRE es `(filas, columnas)`**.
> 2. **`axis` SIEMPRE es la posición del `shape`** (filas = 0, columnas = 1).
>
> *¿Qué posición del shape (qué dimensión) quiero colapsar?*

- `axis=0` -> reduce el eje de las **FILAS** (posición 0 del shape).
  - Colapsa **verticalmente** (hacia abajo).
  - Sobreviven las columnas -> queda **un resultado por columna**.
- `axis=1` -> reduce el eje de las **COLUMNAS** (posición 1 del shape).
  - Colapsa **horizontalmente** (a los lados).
  - Sobreviven las filas -> queda **un resultado por fila**.

```python
datos = np.array([
    [20, 3],
    [15, 7],
    [12, 2],
    [10, 4]
])

print(datos.sum(axis=0))
# [57 16]

print(datos.sum(axis=1))
# [23 22 14 14]
```

- `axis=0`: **OPERA VERTICALMENTE - REDUCE FILAS**.
  - **Recorre la matriz HACIA ABAJO**.
  - Desaparecen filas (colapsan). Mantiene columnas.
  - Reduce las filas y calcula un resultado para cada columna.
  - En el ejemplo de ventas suma todos los precios y todas las unidades.
- `axis=1`: **OPERA HORIZONTALMENTE - REDUCE COLUMNAS**.
  - **Recorre la matriz HACIA LOS LADOS**.
  - Desaparecen (colapsan) columnas.
  - Reduce las columnas y calcula un resultado para cada fila.
  - Aquí suma precio y unidades de cada producto, algo que sirve para ilustrar el eje, aunque no sería una métrica comercial útil.

> [!WARNING]
> No podrías usar estas sumas como facturación total: para obtenerla tendrías que **multiplicar precio por unidades en cada fila** y sumar esos importes.

---

## 2.6. Operaciones de unión

**Corrección detallada de uniones**

```python
array_np_uno = np.array([20, 30, 35, 40])
array_np_dos = np.array([100, 300, 400, 600])

print("Originales:", array_np_uno, "y", array_np_dos)
```

### 1. CONCATENATE: `np.concatenate()`

- **Une los arrays de cabeza a cola en una sola línea** (mantiene 1D pero más largo).

```python
array_concatenate = np.concatenate([array_np_uno, array_np_dos])

print("\nCONCATENATE = Simple join. Alarga la línea 1D: \n   ", array_concatenate)
# [ 20  30  35  40 100 300 400 600]
```

### 2. APPEND: `np.append()`

- **Si no le dices el eje, aplasta los arrays y devuelve un único array plano 1D.**

```python
array_append = np.append(array_np_uno, array_np_dos)

print("\nAPPEND = Aplasta y linealiza (a menos que le indiques un axis): \n   ", array_append)
# [ 20  30  35  40 100 300 400 600]
```

### 3. VSTACK (Vertical Stack): `np.vstack()`

- **Apila los arrays 1D uno ENCIMA de otro. Cada uno se convierte en una FILA.**

```python
union_vstack = np.vstack([array_np_uno, array_np_dos])

print("\nVSTACK = Matriz creciendo hacia ABAJO (Apila filas verticalmente): \n   ", union_vstack)
# [[ 20  30  35  40]
#  [100 300 400 600]]
```

### 4. HSTACK (Horizontal Stack): `np.hstack()`

- **Para `hstack` necesitas arrays con forma de columna** (2D con shape tipo `(4, 1)`).

```python
array_para_hstack_uno = np.array([[20], [30], [35], [40]])
array_para_hstack_dos = np.array([[100], [300], [400], [600]])

union_hstack = np.hstack([array_para_hstack_uno, array_para_hstack_dos])

print("\nHSTACK = Matriz creciendo hacia LOS LADOS (Pega columnas horizontalmente): \n   ", union_hstack)
# [[ 20 100]
#  [ 30 300]
#  [ 35 400]
#  [ 40 600]]
```

---
