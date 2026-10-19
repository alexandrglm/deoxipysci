# 03-003: Matrices

## 3.1. ¿Qué es una matriz?

Una **matriz** es una estructura rectangular de valores organizados en **filas** y **columnas**.

Por ejemplo, la siguiente matriz tiene **2 filas** y **3 columnas**:

$$
A =
\begin{pmatrix}
10 & 20 & 30 \\
40 & 50 & 60
\end{pmatrix}
$$

Se dice que $A$ es una matriz de tamaño $2 \times 3$ (filas por columnas), y se escribe $A \in \mathbb{R}^{2 \times 3}$.

> [!IMPORTANT]
> Se indica siempre **primero las filas y después las columnas**: una matriz $2 \times 3$ no es lo mismo que una $3 \times 2$.

Cada elemento se identifica con dos índices, $a_{ij}$: la fila $i$ y la columna $j$. Por ejemplo, $a_{23} = 60$.

---

### 3.1.1. Estructura y atributos en NumPy

```python
A = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(A.shape)  # (2, 3)
print(A.ndim)   # 2
print(A.size)   # 6
```

- **`shape`**: forma de la matriz, `(filas, columnas)`. Aquí, `(2, 3)`.
- **`ndim`**: número de **ejes** del array. Aquí, `2`.
- **`size`**: número total de elementos. Aquí, `6`.

> [!NOTE]
> Recuerda la advertencia de los vectores: NumPy usa "dimensión" para hablar de los **ejes** del array. Una matriz tiene **dos ejes**: el eje `0` recorre las **filas** y el eje `1` recorre las **columnas**.

---

### 3.1.2. Acceso a filas, columnas y elementos

NumPy utiliza índices que **empiezan en cero**. Así se ve la matriz $A$ con sus índices de Python:

|             | **columna 0** | **columna 1** | **columna 2** |
| ----------- | ------------- | ------------- | ------------- |
| **fila 0**  | `10`          | `20`          | `30`          |
| **fila 1**  | `40`          | `50`          | `60`          |

```python
print(A[0, 0])  # 10: primera fila, primera columna
print(A[1, 2])  # 60: segunda fila, tercera columna
print(A[0])     # [10 20 30]: primera fila
print(A[:, 1])  # [20 50]: segunda columna
```

En `A[fila, columna]`, la coma separa los índices de ambos ejes. El símbolo `:` indica que se seleccionan **todas las posiciones** de ese eje.

> [!WARNING]
> Los índices matemáticos empiezan en $1$ y los de Python en $0$: el elemento $a_{23}$ de la matemática es `A[1, 2]` en NumPy.

> [!NOTE]
> `A[:, 1]` devuelve `[20 50]`, que es un **array de un solo eje** con `shape` `(2,)`. Aunque sea una columna de la matriz, NumPy **no la mantiene como columna** (`(2, 1)`).