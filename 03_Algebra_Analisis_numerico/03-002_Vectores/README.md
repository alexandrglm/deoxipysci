# 03-002: Vectores

## 2.1. ¿Qué es un vector?

Un vector es un **objeto matemático** que, en este bloque, representaremos mediante una **secuencia ordenada de componentes numéricos**.  

Por ejemplo:  

$$
\mathbf{v} = (3, 5, 2)
$$

Este vector tiene tres componentes:  

- **Primera componente:** $3$
- **Segunda componente:** $5$
- **Tercera componente:** $2$

> [!IMPORTANT]
> **El orden importa:** $(3,5,2)$ y $(5,3,2)$ son vectores **diferentes**.

Un vector puede representar distintos tipos de información, según el contexto:  

- Las coordenadas de un punto en el espacio.
- Los precios de tres productos.
- Las mediciones de temperatura de tres sensores.
- Las características numéricas de una observación en un conjunto de datos.


Un vector tridimensional puede representarse geométricamente como **una flecha desde el origen hasta un punto**. Las componentes determinan su posición.  
![](./03-002-001_vector_tridimensional.jpeg)

***

### ¿Qué relación tiene con los escalares?

Un **escalar** representa un único valor; un **vector** agrupa varios componentes ordenados.

| Escalar                | Vector                                     |
| ---------------------- | ------------------------------------------ |
| $5$                    | $(3,5,2)$                                  |
| Una temperatura        | Temperaturas de varios sensores            |
| Un precio              | Precios de varios productos                |
| Un único dato numérico | Una observación con varias características |

> [!NOTE]
> Un vector **no tiene por qué** representar una posición geométrica. En análisis de datos, se usa a menudo para representar una colección ordenada de valores numéricos.  

> [!WARNING]
> Una lista de Python puede almacenar números y parecerse a un vector, pero **una lista no es automáticamente un vector matemático**.  
>  
> La estructura de datos y el objeto matemático son conceptos diferentes.  

---

## 2.2. Representación y dimensión

Podemos representar un vector como una **fila**:

$$
\mathbf{v} = (3, 5, 2)
$$

O como una **columna**:

$$
\mathbf{v} =
\begin{pmatrix}
3 \\
5 \\
2
\end{pmatrix}
$$

Ambas representaciones contienen los mismos valores, pero la **orientación puede importar** en determinadas operaciones matriciales.

La **dimensión** del vector, en este contexto, es el número de componentes que contiene:

| Vector    | Dimensión | Componentes |
| --------- | --------- | ----------- |
| $(7)$     | 1         | 1           |
| $(3,5)$   | 2         | 2           |
| $(3,5,2)$ | 3         | 3           |

> [!WARNING]
> Esta terminología puede confundir: **NumPy usa la palabra "dimensión" para los ejes de un array**, no para el número de componentes. Más adelante distinguiremos ambos significados con precisión.

***

### Índices y componentes

Las componentes se identifican por su **posición**. En matemáticas se usa $v_1, v_2, v_3$ (recuerda que Python es zero-index, **los índices empiezan en cero**).

Para el vector $(3,5,2)$:

| Componente matemático | Valor | Índice Python |
| --------------------- | ----- | ------------- |
| $v_1$                 | 3     | `0`           |
| $v_2$                 | 5     | `1`           |
| $v_3$                 | 2     | `2`           |

### Representación en Python y NumPy

```python
vector_lista = [3, 5, 2]
vector = np.array([3, 5, 2])

print(vector[0])  # 3
print(vector[1])  # 5
print(vector[2])  # 2

print(vector.shape)  # (3,)
print(vector.ndim)   # 1
print(vector.size)   # 3
```

Observa las tres propiedades:

- **`shape`**: forma del array. `(3,)` significa un eje con tres elementos.
- **`ndim`**: número de ejes. Aquí, `1`.
- **`size`**: número total de elementos. Aquí, `3`.

> [!NOTE]
> Aunque el vector matemático tiene **tres componentes**, el array NumPy `vector` tiene **un solo eje**. Por eso `shape` devuelve `(3,)` y `ndim` devuelve `1`.

> [!TIP]
> En términos de objetos: `vector` es una instancia de `np.ndarray`, y `shape`, `ndim` y `size` son **atributos** de esa instancia (se leen sin paréntesis).

---

## 2.3. Operaciones básicas con vectores

Ahora que sabemos representar un vector, podemos operar con sus componentes. Consideremos:

$$
\mathbf{u} = (2, 4, 6), \qquad \mathbf{v} = (1, 3, 5)
$$

**Suma:** se suman las componentes que ocupan la misma posición.

$$
\mathbf{u} + \mathbf{v} = (2+1,\ 4+3,\ 6+5) = (3, 7, 11)
$$

**Resta:** se restan las componentes correspondientes.

$$
\mathbf{u} - \mathbf{v} = (2-1,\ 4-3,\ 6-5) = (1, 1, 1)
$$

**Multiplicación por un escalar:** se multiplican todas las componentes por el mismo número.

$$
3\mathbf{u} = (3 \cdot 2,\ 3 \cdot 4,\ 3 \cdot 6) = (6, 12, 18)
$$

> [!IMPORTANT]
> La suma y la resta **requieren que ambos vectores tengan el mismo número de componentes**.

En NumPy:

```python
import numpy as np

u = np.array([2, 4, 6])
v = np.array([1, 3, 5])

print(u + v)  # [ 3  7 11]
print(u - v)  # [1 1 1]
print(3 * u)  # [ 6 12 18]
```

### Una diferencia importante: listas frente a arrays

En Python, el operador `+` aplicado a **listas concatena** sus elementos:

```python
[2, 4] + [1, 3]  # [2, 4, 1, 3]
```

En cambio, con **arrays NumPy suma componente a componente**:

```python
np.array([2, 4]) + np.array([1, 3])
# array([4, 7])
```

> [!WARNING]
> Mismo operador, resultado distinto: `+` **concatena** listas pero **suma** arrays. Esta diferencia será esencial al trabajar con cálculos numéricos y datos.

---

