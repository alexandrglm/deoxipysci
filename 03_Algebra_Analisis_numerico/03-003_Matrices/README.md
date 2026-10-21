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

> [!WARNING]
> Para la generación de una matriz en NumPy, seguimos usando:
>    
>   - `np.array([ [], []..... [] ])`
>   -  Tenemos el método `np.asarray()` para crear varias series que generen una matriz directamente
>   -  También, el método `np.asmatrix()` puede servir, pero está deprecado, dejará de existir en algún momento y se recomienda usar cualquiera de los anteriores


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

print(np.array_equal([A], [ [10, 20, 30], [40, 50, 60] ]))
```


| Atributo | Qué indica                                      | Valor en `A`            |
| -------- | ----------------------------------------------- | ----------------------- |
| `type()` | Tipo del **objeto** completo (sigue siendo un Array)| `numpy.ndarray`         |
| `.dtype`  | Tipo de dato **de todos los elementos**         | `int64`                 |
| `.shape`  | Forma: `(filas, columnas)`                      | `(2, 3)`                |
| `.ndim`   | Número de **ejes** del array                    | `2`                     |
| `.size`   | Número total de elementos                       | `6`                     |
| `np.count_nonzero()` | Número total de elementos reales, no nulos ni vacíos | `6`                     |
| `np.array_equal(MATRIZ, [ [], []....[] ] )` | Método para comparar una matriz contra otra, o la construcción de sus series | *(no procede)* |

> [!NOTE]
> Recuerda la advertencia de los vectores: NumPy usa "dimensión" para hablar de los **ejes** del array.   
> Una matriz tiene **dos ejes**:  
>   - El eje `0` recorre las **filas**
>   - El eje `1` recorre las **columnas**


#### 3.1.1.2.   Objeto, array y elemento: tres niveles distintos

No es lo mismo el tipo del contenedor que el de lo que contiene:

```python
print(type(A))        # <class 'numpy.ndarray'>   -> la matriz entera
print(A[0].dtype)     # int64                     -> una fila (otro array)
print(type(A[0][1]))  # <class 'numpy.int64'>     -> un elemento (escalar de NumPy)
```

- `A` y cada una de sus filas son **arrays** (`ndarray`).
- Un elemento suelto es un **escalar de NumPy**, no un `int` de Python.

#### 3.1.1.2.   ¿Qué pasa si mezclamos tipos?

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

#### 3.2.1.2    Multiplicación elemento a elemento (A * B), Producto de Hadamard

> [!WARNING]
> `A * B` multiplica las posiciones correspondientes. **No es multiplicación matricial.**
  
Matemáticamente, `A * B` es el **producto elemento a elemento**, también llamado **producto de Hadamard**:  

$$
A \odot B = \begin{pmatrix}
1 \cdot 10 & 2 \cdot 20 \\
3 \cdot 30 & 4 \cdot 40
\end{pmatrix} = \begin{pmatrix}
10 & 40 \\
90 & 160
\end{pmatrix}
$$

> [!TIP]
> Las aplicaciones habituales del producto de Hadamard son:  
>  
>   - **Estadística y Machine Learning** 
>       * Regresión ponderada, métodos del núcleo (kernel) y en la aplicación de restricciones por elementos a estructuras de co-varianza
>  
>   - -**Procesamiento de datos** 
>       * Funciona como una multiplicación directa y sencilla para enmascarar o escalar matrices de manera individual

***

### 3.2.2.  Multiplicación Escalar, multiplicar una matriz por un escalar

Un escalar multiplica **cada elemento**:  

```python
print(A * 3)
# [[ 3  6]
#  [ 9 12]]
```

$$
3A = \begin{pmatrix}
3 \cdot 1 & 3 \cdot 2 \\
3 \cdot 3 & 3 \cdot 4
\end{pmatrix} = \begin{pmatrix}
3 & 6 \\
9 & 12
\end{pmatrix}
$$

---


### 3.2.3.  Multiplicación matricial

Merece una unidad aparte, no una mención rápida ...


> [!WARNING]
> Al igual que en la multiplicación matricial con vectores unidimensionales, es necesaria cierta condición de forma en el caso de las matrices:
>  - **MISMO NUMERO DE COLUMNAS EN UNA MATRIZ, QUE DE FILAS EN OTRA**

Ya hemos usado `@` con matrices pequeñas. Ahora vemos **cómo funciona por dentro** para el caso general.  

> [!NOTE]
> En este apartado, $A$ y $B$ son **matrices nuevas**, distintas de las del apartado anterior.

***

#### 3.2.3.1. La idea: una tabla de productos escalares

La multiplicación matricial **no es una operación nueva**:   es una **tabla de productos escalares**.  


> Cada celda del resultado es el **producto escalar** entre una **fila** de $A$ y una **columna** de $B$.

- Antes: `a @ b` entre dos vectores era **un** producto escalar y daba **un** número.
- Ahora: `A @ B` hace **muchos** productos escalares y los organiza en una **rejilla**.


***


#### 3.2.3.2. Condición de forma

Un producto escalar solo existe entre vectores de la **misma longitud**:  
    
    - Una fila de $A$ tiene tantos elementos como **columnas** tiene $A$
    - Una columna de $B$ tiene tantos elementos como **filas** tiene $B$
    
Para que cada pareja fila-columna se pueda multiplicar, **esos dos números deben coincidir**.  

> [!WARNING]
> **Condición de forma:** el número de **columnas de $A$** debe ser igual al número de **filas de $B$**.


Si $A$ tiene forma $(m, n)$ y $B$ tiene forma $(n, p)$, el resultado $C$ tiene forma $(m, p)$:  

```text
  (m, n)  @  (n, p)  =  (m, p)
      └───────┘
   deben coincidir
```


#### 3.2.3.3. La fórmula

$$
C = AB
\qquad
c_{ij} = \sum_{k=1}^{n} a_{ik} \, b_{kj}
= a_{i1} b_{1j} + a_{i2} b_{2j} + \cdots + a_{in} b_{nj}
$$

Es decir, $c_{ij}$ es el producto escalar de la **fila $i$** de $A$ con la **columna $j$** de $B$. En NumPy:  

Entonces, **la regla para cualquier celda** es:   

$$
C_{ij} = A[i, 0] 
\cdot 
B[0, j] + A[i, 1] 
\cdot 
B[1, j]
$$

- Los dos productos de una celda comparten la misma i (fila de A) y la misma j (columna de B)

- Lo único que cambia entre ellos es el índice del medio, 0 y 1


> [!WARNING]
> Los índices matemáticos ($i$, $j$) empiezan en $1$, y los de Python en $0$. Aquí usamos **índices de Python** en los ejemplos.

```python
C[i, j] = A[i, :] @ B[:, j]
```

***

#### 3.2.3.4. El esquema de Falk: ver qué se multiplica con qué

La fórmula es correcta, pero cuesta visualizar mentalmente **qué fila se junta con qué columna**.  

> [!IMPORTANT]
> El **Esquema de Falk** resuelve eso:  
>   
>  - Es una forma de **colocar las matrices en el papel** para que cada celda del resultado quede a la vista de sus dos vectores.



##### 3.2.3.4.1.    Ejemplo mínimo: $2 \times 2$ por $2 \times 2$

Empezamos con el caso más pequeño, con números **todos distintos** para no confundir qué viene de dónde:  

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
5 & 6 \\
7 & 8
\end{pmatrix}
$$

##### 3.2.3.4.2.    Cómo se construye, paso a paso

1. **$B$ arriba a la derecha**
2. **$A$ abajo a la izquierda**
3. **$C$ en el cruce**: debajo de $B$ y a la derecha de $A$. Su forma se lee del dibujo: las **filas de $A$** por las **columnas de $B$**
4. **Cada celda de $C$** se calcula con **su fila de $A$** (hacia la izquierda) y **su columna de $B$** (hacia arriba)

![Esquema de Falk construido en cuatro pasos para C[0, 1] = 1*6 + 2*8 = 22](./img/03-003_falk_construccion.png)

- **ROJO:** la fila de $A$ que interviene y su fila en $C$
- **NARANJA:** la columna de $B$ que interviene y su columna en $C$
- **VERDE:** la celda de $C$, en el **cruce** de ambas

El mismo resultado, en consola:  

```text
A (2×2)          B (2×2)
                  col 0  col 1
                    5   [  6  ]
                    7   [  8  ]
───────────────┼───────────────
[  1  ][  2  ] │   19   « 22  »  ← fila 0
   3      4    │   43     50     ← fila 1
                 C (2×2)

[ ] fila 0 de A y columna 1 de B   « » celda C[0, 1]
```

> [!TIP]
> Para saber qué calcula una celda de $C$, **sigue su fila hacia la izquierda** (hasta $A$) y **su columna hacia arriba** (hasta $B$). Esos dos vectores son los que se multiplican.



##### 3.2.3.4.3.    Las cuatro celdas

$$
(1, 2) \cdot (6, 8) = 1 \cdot 6 + 2 \cdot 8 = \boxed{22}
\qquad \text{(celda } C[0, 1] \text{, la del dibujo)}
$$

| Celda     | Fila de $A$ | Columna de $B$ | Cálculo                   | Resultado |
| --------- | ----------- | -------------- | ------------------------- | --------- |
| `C[0, 0]` | `[1, 2]`    | `[5, 7]`       | $1 \cdot 5 + 2 \cdot 7$   | $19$      |
| `C[0, 1]` | `[1, 2]`    | `[6, 8]`       | $1 \cdot 6 + 2 \cdot 8$   | $22$      |
| `C[1, 0]` | `[3, 4]`    | `[5, 7]`       | $3 \cdot 5 + 4 \cdot 7$   | $43$      |
| `C[1, 1]` | `[3, 4]`    | `[6, 8]`       | $3 \cdot 6 + 4 \cdot 8$   | $50$      |

$$
C = AB =
\begin{pmatrix}
19 & 22 \\
43 & 50
\end{pmatrix}
$$

> [!IMPORTANT]
> Cada celda es **un producto escalar de dos vectores**. El esquema de Falk no calcula nada nuevo:   
>  
>   - Solo **coloca las matrices para que se vea cuáles son esos dos vectores**


***


#### 3.2.3.5. Ejemplo ampliado: $3 \times 2$ por $2 \times 3$

Ahora, el mismo método con formas **distintas**, donde se ve que $C$ no tiene por qué parecerse a $A$ ni a $B$:  

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
5 & 6
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
10 & 20 & 30 \\
40 & 50 & 60
\end{pmatrix}
$$

- $A$ es $3 \times 2$ y $B$ es $2 \times 3$: las columnas de $A$ ($2$) coinciden con las filas de $B$ ($2$)
- $C$ será $3 \times 3$: **9 celdas**
- Cada celda es un producto escalar de **2 elementos** (porque $n = 2$)


Una celda en detalle, `C[1, 2]`: la **fila 1 de $A$** con la **columna 2 de $B$**:  

$$
\underbrace{(3, \; 4)}_{\text{fila 1 de } A}
\cdot
\underbrace{(30, \; 60)}_{\text{columna 2 de } B}
= 3 \cdot 30 + 4 \cdot 60 = 90 + 240 = \boxed{330}
$$

![Esquema de Falk para C[1, 2] = 3*30 + 4*60 = 330](./img/03-003_multiplicacion.png)

```text
A (3×2)          B (2×3)
                  col 0  col 1  col 2
                   10     20   [ 30  ]
                   40     50   [ 60  ]
───────────────┼──────────────────────
   1      2    │   90     120    150    ← fila 0
[  3  ][  4  ] │   190    260  « 330 »  ← fila 1
   5      6    │   290    400    510    ← fila 2
                 C (3×3)

[ ] fila 1 de A y columna 2 de B   « » celda C[1, 2]
```

##### 3.2.3.5.1 Las nueve celdas

| Celda     | Fila de $A$ | Columna de $B$ | Cálculo                   | Resultado |
| --------- | ----------- | -------------- | ------------------------- | --------- |
| `C[0, 0]` | `[1, 2]`    | `[10, 40]`     | $1 \cdot 10 + 2 \cdot 40$ | $90$      |
| `C[0, 1]` | `[1, 2]`    | `[20, 50]`     | $1 \cdot 20 + 2 \cdot 50$ | $120$     |
| `C[0, 2]` | `[1, 2]`    | `[30, 60]`     | $1 \cdot 30 + 2 \cdot 60$ | $150$     |
| `C[1, 0]` | `[3, 4]`    | `[10, 40]`     | $3 \cdot 10 + 4 \cdot 40$ | $190$     |
| `C[1, 1]` | `[3, 4]`    | `[20, 50]`     | $3 \cdot 20 + 4 \cdot 50$ | $260$     |
| `C[1, 2]` | `[3, 4]`    | `[30, 60]`     | $3 \cdot 30 + 4 \cdot 60$ | $330$     |
| `C[2, 0]` | `[5, 6]`    | `[10, 40]`     | $5 \cdot 10 + 6 \cdot 40$ | $290$     |
| `C[2, 1]` | `[5, 6]`    | `[20, 50]`     | $5 \cdot 20 + 6 \cdot 50$ | $400$     |
| `C[2, 2]` | `[5, 6]`    | `[30, 60]`     | $5 \cdot 30 + 6 \cdot 60$ | $510$     |

$$
C = AB =
\begin{pmatrix}
90 & 120 & 150 \\
190 & 260 & 330 \\
290 & 400 & 510
\end{pmatrix}
$$

***

#### 3.2.3.6. Comprobación con NumPy

```python
A = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

B = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

C = A @ B

print(C)
# [[ 90 120 150]
#  [190 260 330]
#  [290 400 510]]

print(C.shape)            # (3, 3)
print(C[1, 2])            # 330
print(A[1, :] @ B[:, 2])  # 330: la misma celda, como producto escalar
```

> [!IMPORTANT]
> `C[1, 2]` y `A[1, :] @ B[:, 2]` dan lo mismo. **Esa es toda la multiplicación matricial:**  
>   
>   - **Una tabla de productos escalares!**

***

#### 3.2.3.7. Errores de forma y orden

Si las formas no son compatibles, NumPy lanza un `ValueError`:

```python
print(B.shape, B.shape)  # (2, 3) (2, 3)
# B @ B                  # ValueError: las columnas de B (3) no coinciden con sus filas (2)
```

> [!WARNING]
> **El orden importa.** Con las mismas matrices, `B @ A` sí es posible, pero es **otra operación** y da una matriz de **forma distinta**:
>
> ```python
> print((A @ B).shape)  # (3, 3)
> print((B @ A).shape)  # (2, 2)
> print(B @ A)
> # [[220 280]
> #  [490 640]]
> ```
>
> En general, la multiplicación matricial **no es conmutativa**: `A @ B` y `B @ A` pueden dar resultados distintos, o incluso uno de ellos no existir.

> [!TIP]
> Comprueba siempre las formas con `.shape` antes de multiplicar. Es la forma más rápida de encontrar un error de compatibilidad.


---


