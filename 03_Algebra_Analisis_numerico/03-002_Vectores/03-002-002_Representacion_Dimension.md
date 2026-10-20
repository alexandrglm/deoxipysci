# 03-002:   Vectores

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

### 2.2.1.  Índices y componentes

Las componentes se identifican por su **posición**. En matemáticas se usa $v_1, v_2, v_3$ (recuerda que Python es zero-index, **los índices empiezan en cero**).

Para el vector $(3,5,2)$:

| Componente matemático | Valor | Índice Python |
| --------------------- | ----- | ------------- |
| $v_1$                 | 3     | `0`           |
| $v_2$                 | 5     | `1`           |
| $v_3$                 | 2     | `2`           |

### 2.2.2   Representación en Python y NumPy

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
