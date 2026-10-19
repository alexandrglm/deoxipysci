# 03-002: Vectores

## 2.1. ¿Qué es un vector?

Un vector es un **objeto matemático** que, en este bloque, representaremos mediante una **secuencia ordenada de componentes numéricos**.  

Por ejemplo:  

$$
\mathbf{v} = (3, 5, 2)
$$

Este vector tiene tres componentes:  

- **Primer componente:** $3$
- **Segundo componente:** $5$
- **Tercer componente:** $2$

> [!IMPORTANT]
> **El orden importa:** $(3,5,2)$ y $(5,3,2)$ son vectores **diferentes**.

Un vector puede representar distintos tipos de información, según el contexto:  

- Las coordenadas de un punto en el espacio.
- Los precios de tres productos.
- Las mediciones de temperatura de tres sensores.
- Las características numéricas de una observación en un conjunto de datos.


Un vector tridimensional puede representarse geométricamente como **una flecha desde el origen hasta un punto**. Los componentes determinan su posición.  
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


## 2.4. Norma o longitud de un vector

La **norma** de un vector es una medida de su **magnitud**.

- En el caso más habitual que utilizaremos aquí, la **norma euclídea, o L2**, representa la **longitud geométrica** del vector.

Consideremos:

$$
\mathbf{v} = (3, 4)
$$

Podemos interpretar este vector como:

- Un desplazamiento de **3 unidades** en un eje.
- Otro desplazamiento de **4 unidades** en el otro eje.

Su longitud se calcula aplicando el **teorema de Pitágoras**.  

![Vector 2D y su norma como hipotenusa](./03-002_002_math-2d-vectors.png)

> [!IMPORTANT]
> La norma euclídea corresponde a la **hipotenusa** del triángulo formado por las componentes del vector.

> [!TIP]
> **Referencias de interés**
>
> 1. [swdevnotes.com](https://swdevnotes.com/python/2020/math-2d-vectors/)
> 2. [Math for Programmers](https://www.manning.com/books/math-for-programmers)

***

### Fórmula

Para un vector bidimensional:  

$$
\|\mathbf{v}\|_2 = \sqrt{v_1^2 + v_2^2}
$$

Por tanto, si un eje era $3$ y otro eje era $4$:  

$$
\begin{aligned}
\|\mathbf{v}\|_2 &= \sqrt{3^2 + 4^2} \\
&= \sqrt{9 + 16} \\
&= \sqrt{25} \\
&= \boxed{5}
\end{aligned}
$$

Para un vector con $n$ componentes, la fórmula se generaliza:  

$$
\|\mathbf{v}\|_2 = \sqrt{\sum_{i=1}^{n} v_i^2}
$$

- Es decir: **elevamos** cada componente al cuadrado, **sumamos** los resultados y **calculamos la raíz cuadrada**.  

***

### Calcular la norma con NumPy

La forma habitual es utilizar `numpy.linalg.norm(VECTOR)`.

```python
vector = np.array([3, 4])
norma = np.linalg.norm(vector)

print(norma)  # 5.0
```

> [!NOTE]
> `np.linalg.norm()` admite varios tipos de norma. Si no especificamos el parámetro `ord`, para un vector utiliza por defecto la **norma euclídea**, también denominada **norma L2**.

---

### Otras normas que conviene conocer

Consideremos el vector $\mathbf{v} = (3, -4)$.

| Norma             | Fórmula                       | Resultado | ¿Cuándo se usa?                                              |
| ----------------- | ----------------------------- | --------- | ------------------------------------------------------------ |
| **L1**            | Suma de los valores absolutos | $7$       | Distancia por cuadrícula; modelos que buscan ceros (Lasso)   |
| **L2 o euclídea** | Raíz de la suma de cuadrados  | $5$       | Distancia en línea recta; la opción por defecto (KNN, Ridge) |
| **L∞**            | Máximo valor absoluto         | $4$       | Peor caso; tolerancias ("ninguna componente supera X")       |

> [!NOTE]
> Aquí solo las presentamos. Más adelante las trabajaremos a fondo, con sus aplicaciones.

En NumPy:

```python
vector = np.array([3, -4])

print(np.linalg.norm(vector, ord=1))       # 7.0
print(np.linalg.norm(vector, ord=2))       # 5.0
print(np.linalg.norm(vector))              # 5.0 (sin ord: L2 por defecto)
print(np.linalg.norm(vector, ord=np.inf))  # 4.0
```

- **L1:** suma distancias absolutas. Imagina moverte por calles en cuadrícula: solo puedes ir en horizontal y vertical.
- **L2:** mide la longitud euclídea, la "línea recta" de siempre.
- **L∞:** toma la mayor magnitud absoluta. Solo importa la componente más grande.

> [!WARNING]
> Para la norma L∞ se usa `ord=np.inf`, **no** un número ni un texto.

> [!TIP]
> **El infinito en Python:** `np.inf` es un `float` estándar, no un tipo propio de NumPy. NumPy solo expone el valor.
>
> ```python
> print(type(np.inf))      # <class 'float'>
> print(10**100 < np.inf)  # True
> print(-np.inf)           # -inf
> ```
>
> Es mayor que cualquier número finito, y por eso encaja con "el máximo".

> [!NOTE]
> En aprendizaje automático, estas normas aparecen en la medición de distancias, la normalización de datos y la regularización de modelos. Por ahora, lo importante es **entender qué calcula cada una**, no memorizar todas sus aplicaciones.

---

> [!WARNING]
> Pendiente desde aquí: el siguiente punto debería ser **2.5. PRODUCTOS ESCALARES**.