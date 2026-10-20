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
> Se indica siempre **primero las filas y después las columnas**:  
>   - Una matriz $2 \times 3$ no es lo mismo que una $3 \times 2$.

Cada elemento se identifica con dos índices, $a_{ij}$: la fila $i$ y la columna $j$. Por ejemplo, $a_{23} = 60$.  

***

### 3.1.1. Estructura y atributos en NumPy

```python
A = np.array(
    [
        [10, 20, 30],
        [40, 50, 60]
    ]
)

print(type(A))  # <class 'numpy.ndarray'>
print(A.dtype)  # int64

print(A.shape)  # (2, 3)
print(A.ndim)   # 2

print(A.size)   # 6
print(A.count_nonzero(A))   # 6


```
| Atributo | Qué indica                                      | Valor en `A`            |
| -------- | ----------------------------------------------- | ----------------------- |
| `type()` | Tipo del **objeto** completo (sigue siendo un Array)| `numpy.ndarray`         |
| `.dtype`  | Tipo de dato **de todos los elementos**         | `int64`                 |
| `.shape`  | Forma: `(filas, columnas)`                      | `(2, 3)`                |
| `.ndim`   | Número de **ejes** del array                    | `2`                     |
| `.size`   | Número total de elementos                       | `6`                     |
| `np.count_nonzero()` | Número total de elementos reales, no nulos ni vacíos | `6`                     |


> [!NOTE]
> Recuerda la advertencia de los vectores: NumPy usa "dimensión" para hablar de los **ejes** del array.   
> Una matriz tiene **dos ejes**:  
>   - El eje `0` recorre las **filas**
>   - El eje `1` recorre las **columnas**


#### Objeto, array y elemento: tres niveles distintos

No es lo mismo el tipo del contenedor que el de lo que contiene:

```python
print(type(A))        # <class 'numpy.ndarray'>   -> la matriz entera
print(A[0].dtype)     # int64                     -> una fila (otro array)
print(type(A[0][1]))  # <class 'numpy.int64'>     -> un elemento (escalar de NumPy)
```

- `A` y cada una de sus filas son **arrays** (`ndarray`).
- Un elemento suelto es un **escalar de NumPy**, no un `int` de Python.

#### 3.1.1.1.   ¿Qué pasa si mezclamos tipos?

Un array de NumPy guarda **un único `dtype` para todos sus elementos**. Si mezclas tipos, NumPy tiene que elegir uno que sirva para todos:  

```python
mezcla_texto = np.array([[10, "20", 30], [40, 50, 60]])
print(mezcla_texto.dtype)  # <U21  (todo pasa a ser texto)

mezcla = np.array([[10, "20", 30], [40, np.inf, None]])
print(mezcla.dtype)        # object
print(type(mezcla[0][1]))  # <class 'str'>
print(type(mezcla[1][2]))  # <class 'NoneType'>
```

- Con números y texto, **todo se convierte en texto** (`<U...`).
- Con `None` de por medio, el `dtype` pasa a **`object`**: cada elemento conserva su tipo original de Python.

> [!WARNING]
> Una matriz `object` **deja de ser una matriz numérica**. Se pierde la velocidad de NumPy y las operaciones matemáticas dejan de ser fiables. En una matriz matemática, todos los elementos deben ser **numéricos**.


***

### 3.1.2. Acceso a filas, columnas y elementos

Ya sabíamos que NumPy era zero-based, utiliza índices que **empiezan en cero**, y eso sigue sin cambiar con las matrices.  

Así se ve la matriz $A$ con sus índices de Python:  

|            | **columna 0** | **columna 1** | **columna 2** |
| ---------- | ------------- | ------------- | ------------- |
| **fila 0** | `10`          | `20`          | `30`          |
| **fila 1** | `40`          | `50`          | `60`          |

```python
print(A[0, 0])  # 10: primera fila, primera columna
print(A[1, 2])  # 60: segunda fila, tercera columna
print(A[0])     # [10 20 30]: primera fila
print(A[:, 1])  # [20 50]: segunda columna
```

En `A[fila, columna]`, la coma separa los índices de ambos ejes. El símbolo `:` indica que se seleccionan **todas las posiciones** de ese eje.

> [!WARNING]
> Los índices matemáticos empiezan en $1$ y los de Python en $0$: el elemento $a_{23}$ de la matemática es `A[1, 2]` en NumPy.


#### 3.1.2.1.   `[fila, columna]` vs `[fila][columna]`

También existe la sintaxis anidada, que **para un elemento individual dará el mismo resultado**:

```python
print(A[1, 2])  # 60
print(A[1][2])  # 60
```

La diferencia es que `A[1][2]` son **dos pasos**:  
    1. Primero `A[1]` extrae la fila (un array 1D)
    2. Después `[2]` toma un elemento de esa fila. 
    
En cambio, `A[1, 2]` es **una sola operación** sobre la matriz.  

> [!WARNING]
> Ambas sintaxis coinciden **solo para un elemento**. Para filas o columnas completas **no hacen lo mismo**.


#### 3.1.2.2.   La trampa de las columnas: `A[:][1]`

```python
print(A[:, 1])  # [20 50]    -> segunda COLUMNA (lo que buscabas)
print(A[:][1])  # [40 50 60] -> segunda FILA (¡no es la columna!)
```

- `A[:]` devuelve **toda la matriz** (una vista, no una columna), y el segundo `[1]` toma la **fila 1** de ese resultado.

> [!IMPORTANT]
> Para acceder a filas, columnas y elementos en NumPy, **usa siempre `[fila, columna]`**.  
> **Evita encadenar `[][]` salvo que sepas exactamente por qué** lo haces (como crear un nuevo array con ciertos valores, **sacar un valor concreto jugando con "coordenadas"**, etc)  


#### 3.1.2.3.   Una columna extraída no se mantiene como columna

Al extraer una columna con `A[:, 1]`, NumPy **colapsa** el resultado a un array de **un solo eje**.  

Para conservar la forma de columna $(2 \times 1)$, pasa el índice **dentro de una lista**:  

```python
columna_colapsada = A[:, 1]
columna_preservada = A[:, [1]]

print(columna_colapsada)   # [20 50]
print(columna_preservada)
# [[20]
#  [50]]

print(columna_preservada.shape)  # (2, 1)
print(columna_preservada.ndim)   # 2
```

Matemáticamente, son objetos distintos:  

$$
\begin{pmatrix} 20 & 50 \end{pmatrix}
\ \text{o simplemente}\ (20, 50)
\qquad \text{frente a} \qquad
\begin{pmatrix} 20 \\ 50 \end{pmatrix}
$$

- El primero es un vector de dos componentes (`shape` `(2,)`)  
- El segundo es una **matriz de tamaño $2 \times 1$** (`shape` `(2, 1)`)  


#### 3.1.2.4.   Para tener claro qué devuelve cada expresión ...

| Expresión   | Resultado       | `shape`  | `ndim` | ¿Qué es?                       |
| ----------- | --------------- | -------- | ------ | ------------------------------ |
| `A`         | la matriz       | `(2, 3)` | `2`    | Matriz                         |
| `A[1]`      | `[40 50 60]`    | `(3,)`   | `1`    | Una **fila** (array 1D)        |
| `A[:, 1]`   | `[20 50]`       | `(2,)`   | `1`    | Una **columna colapsada** (1D) |
| `A[:][1]`   | `[40 50 60]`    | `(3,)`   | `1`    | Una **fila** (no la columna)   |
| `A[:, [1]]` | `[[20] [50]]`   | `(2, 1)` | `2`    | Una **columna preservada** (2D) |

> [!TIP]
> Cuando necesites que una columna siga siendo una columna, usa `A[:, [1]]`.  
>   
> También vale seleccionar rangos, `A[:, 1:2]`, que selecciona un rango de una sola columna y mantiene los dos ejes.  

> [!NOTE]
> Las extracciones de una matriz **cambian de forma**: el resultado ya no es una matriz, sino un array con menos ejes:  
>   - Sigue siendo un `numpy.ndarray`, pero con distinto `shape` y `ndim`.


---

## 3.2. Operaciones básicas con matrices

Con NumPy, muchas operaciones entre matrices se realizan **elemento a elemento**, siempre que sus **formas** (`shape`) sean compatibles.  

Usaremos estas dos matrices:

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
10 & 20 \\
30 & 40
\end{pmatrix}
$$

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [10, 20],
    [30, 40]
])
```

***

### 3.2.1.  Suma, resta y producto elemento a elemento

Cada operación se aplica a las **posiciones correspondientes**:  

```python
print(A + B)
# [[11 22]
#  [33 44]]

print(A - B)
# [[ -9 -18]
#  [-27 -36]]

print(A * B)
# [[ 10  40]
#  [ 90 160]]
```

> [!NOTE]
> Para `A + B` y `A - B`, ambas matrices deben tener la **misma forma**. Más adelante veremos que NumPy también admite algunas combinaciones de formas distintas (*broadcasting*).

> [!WARNING]
> `A * B` multiplica las posiciones correspondientes. **No es multiplicación matricial.**

  
Matemáticamente, `A * B` es el **producto elemento a elemento** (también llamado producto de Hadamard):    

$$
A \odot B =
\begin{pmatrix}
1 \cdot 10 & 2 \cdot 20 \\
3 \cdot 30 & 4 \cdot 40
\end{pmatrix}
=
\begin{pmatrix}
10 & 40 \\
90 & 160
\end{pmatrix}
$$

***

### 3.2.2.  Multiplicar una matriz por un escalar

Un escalar multiplica **cada elemento**:  

```python
print(A * 3)
# [[ 3  6]
#  [ 9 12]]
```

$$
3A =
\begin{pmatrix}
3 \cdot 1 & 3 \cdot 2 \\
3 \cdot 3 & 3 \cdot 4
\end{pmatrix}
=
\begin{pmatrix}
3 & 6 \\
9 & 12
\end{pmatrix}
$$

***

### 3.2.3.  Multiplicación matricial

Para multiplicar matrices **matemáticamente**, usamos el operador `@`:  

```python
print(A @ B)
# [[ 70 100]
#  [150 220]]
```

> [!IMPORTANT]
> `A * B` y `A @ B` son operaciones **distintas** y dan resultados distintos. La multiplicación matricial es `@`.

Cada elemento del resultado se calcula con una **fila** de $A$ y una **columna** de $B$, multiplicando y sumando (como un **producto escalar**):  

$$
(AB)_{ij} = \sum_{k} a_{ik} \, b_{kj}
$$

Para nuestro ejemplo:  

$$
AB =
\begin{pmatrix}
1 \cdot 10 + 2 \cdot 30 & 1 \cdot 20 + 2 \cdot 40 \\
3 \cdot 10 + 4 \cdot 30 & 3 \cdot 20 + 4 \cdot 40
\end{pmatrix}
=
\begin{pmatrix}
70 & 100 \\
150 & 220
\end{pmatrix}
$$

#### 3.2.3.1.   Condición de compatibilidad

Para que `A @ B` sea posible, el número de **columnas de $A$** debe coincidir con el número de **filas de $B$**.  

Si $A$ tiene forma $(m, n)$ y $B$ forma $(n, p)$, el resultado tendrá forma $(m, p)$:  

```text
  (m, n)  @  (n, p)  =  (m, p)
      └──────┘
   deben coincidir
```

```python
C = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.shape, C.shape)   # (2, 2) (2, 3)
print((A @ C).shape)      # (2, 3)   -> (2, 2) @ (2, 3): los 2 centrales coinciden
# C @ A                   # ValueError -> (2, 3) @ (2, 2): 3 y 2 no coinciden
```

> [!WARNING]
> En general, la multiplicación matricial **no es conmutativa**: `A @ B` y `B @ A` pueden dar resultados distintos. En este ejemplo coinciden solo porque $B = 10A$.

> [!TIP]
> Comprueba siempre las formas con `.shape` antes de multiplicar. Es la forma más rápida de encontrar un error de compatibilidad.