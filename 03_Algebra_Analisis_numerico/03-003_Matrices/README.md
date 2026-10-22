# 03-003: Matrices

***

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

Cada elemento se identifica con dos índices, $a_{ij}$:  
    - La fila $i$
    - La columna $j$
    
- Por ejemplo:     $a_{23} = 60$.  

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
| `type()` | Tipo del **objeto** completo (sigue siendo un Array)| `numpy.ndarray`      |
| `.dtype`  | Tipo de dato **de todos los elementos**         | `int64`                 |
| `.shape`  | Forma: `(filas, columnas)`                      | `(2, 3)`                |
| `.ndim`   | Número de **ejes** del array                    | `2`                     |
| `.size`   | Número total de elementos                       | `6`                     |

| Métodos útiles | Qué indica                                      | Valor en `A`            |
| -------- | ----------------------------------------------- | ----------------------- |
| `np.count_nonzero()` | Número total de elementos reales, no nulos ni vacíos | `6`                     |
| `np.array_equal(MATRIZ, [ [], []....[] ] )` | Método para comparar una matriz contra otra, o la construcción de sus series | `True` |

> [!NOTE]
> Recuerda la advertencia de los vectores:  
>   - NumPy usa "dimensión" para hablar de los **ejes** del array.   
>  
> Una matriz tiene **dos ejes**:  
>   - El eje `0` recorre las **filas**
>   - El eje `1` recorre las **columnas**



#### 3.1.1.2.   Objeto, array y elemento: tres niveles distintos

No es lo mismo el tipo del contenedor, que el de lo que contiene:  

```python
print(type(A))        # <class 'numpy.ndarray'>   -> la matriz entera
print(A[0].dtype)     # int64                     -> una fila (otro array)
print(type(A[0][1]))  # <class 'numpy.int64'>     -> un elemento (escalar de NumPy)
```

- `A` y cada una de sus filas son **arrays** (`ndarray`).
- Un elemento suelto es un **escalar de NumPy**, no un `int` de Python.



#### 3.1.1.2.   ¿Qué pasa si mezclamos tipos?

Un array de NumPy guarda **un único `dtype` para todos sus elementos**.  
  
Si mezclas tipos, NumPy tiene que elegir uno que sirva para todos:  

```python
mezcla_texto = np.array([[10, "20", 30], [40, 50, 60]])
print(mezcla_texto.dtype)  # <U21  (todo pasa a ser texto)

mezcla = np.array([[10, "20", 30], [40, np.inf, None]])
print(mezcla.dtype)        # object
print(type(mezcla[0][1]))  # <class 'str'>
print(type(mezcla[1][2]))  # <class 'NoneType'>
```

- Con números y texto, **todo se convierte en texto** (`<U...`).

- Con `None` de por medio, el `dtype` pasa a **`object`**:
    * Cada elemento conserva su tipo original de Python.

> [!WARNING]
> Una matriz `object` **deja de ser una matriz numérica**. Se pierde la velocidad de NumPy y las operaciones matemáticas dejan de ser fiables.  
> En una matriz matemática, todos los elementos deben ser **numéricos**.



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

- En `A[fila, columna]`, la coma separa los índices de ambos ejes.  
    - El símbolo `:` indica que se seleccionan **todas las posiciones** de ese eje.

> [!WARNING]
> Los índices matemáticos empiezan en $1$ y los de Python en $0$:  
>   - El elemento $a_{23}$ de la matemática es `A[1, 2]` en NumPy.




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
> Las extracciones de una matriz **cambian de forma**:  
>   - El resultado ya no es una matriz, sino un array con menos ejes:  
>       * Sigue siendo un `numpy.ndarray`, pero con distinto `shape` y `ndim`.  


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
> Para `A + B` y `A - B`, ambas matrices deben tener la **misma forma**.  
> Más adelante veremos que NumPy también admite algunas combinaciones de formas distintas (*broadcasting*).



#### 3.2.1.2    Producto de Hadamard:   Multiplicación elemento a elemento (A * B)

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

> [!NOTE]
> Las aplicaciones habituales del producto de Hadamard son:  
>  
>   - **Estadística y Machine Learning** 
>       * Regresión ponderada, métodos del núcleo (kernel) y en la aplicación de restricciones por elementos a estructuras de co-varianza
>  
>   - -**Procesamiento de datos** 
>       * Funciona como una multiplicación directa y sencilla para enmascarar o escalar matrices de manera individual

***

### 3.2.2.  Producto Escalar, Multiplicación Escalar, multiplicar una matriz por un escalar

Un escalar multiplica **cada elemento**:  



$$
3A = \begin{pmatrix}
3 \cdot 1 & 3 \cdot 2 \\
3 \cdot 3 & 3 \cdot 4
\end{pmatrix} = \begin{pmatrix}
3 & 6 \\
9 & 12
\end{pmatrix}
$$


```python
print(A * 3)
# [[ 3  6]
#  [ 9 12]]
```

Sin mayor complicación, el escalar es multiplicado por cada componente de cada serie.  

---


### 3.2.3.  Multiplicación matricial

Merece una unidad aparte, no una mención rápida ...


> [!WARNING]
> Al igual que en la multiplicación matricial con vectores unidimensionales, es necesaria cierta condición de forma en el caso de las matrices:  
>  
>  - **MISMO NUMERO DE COLUMNAS EN UNA MATRIZ, QUE DE FILAS EN OTRA**

Ya hemos usado `@` con matrices pequeñas. Ahora vemos **cómo funciona por dentro** para el caso general.  

> [!NOTE]
> En este apartado, $A$ y $B$ **se van redefineniendo por cada ejemplo**:  
>  
>   - 3.2.3.4 son matrices $2 \times 2$
>   - Desde 3.2.3.5, $A$ es $3 \times 2$ y $B$ es $2 \times 3$


#### 3.2.3.1. La idea mental: Una tabla de productos escalares

La multiplicación matricial **no es una operación nueva**:   es una **tabla de productos escalares**.  


> Cada celda del resultado es el **producto escalar** entre una **fila de** $A$ y una **columna de** $B$.

- Antes:    `a @ b` entre dos vectores era **UN SOLO** producto escalar y daba **UN SOLO** número.
- Ahora:    `A @ B` hace **muchos** productos escalares y los organiza en una **rejilla**.





#### 3.2.3.2. Condición de forma

Un producto escalar solo existe entre vectores de la **misma longitud**:  
    
- **Una FILA de** $A$ **tiene tantas componentes como COLUMNAS tiene** $A$
- **Una COLUMNA de** $B$ **tiene tantas componentes como FILAS tiene** $B$
    
Para que cada pareja fila-columna se pueda multiplicar, **esos dos números deben coincidir**.  

> [!WARNING]
> **Condición de forma:**  
>   
> - El número de **columnas de $A$** debe ser igual al número de **filas de $B$**.


Si $A$ tiene forma $(m, n)$ y $B$ tiene forma $(n, p)$, el resultado $C$ tiene forma $(m, p)$:  

```text
  (m, n)  @  (n, p)  =  (m, p)
      └───────┘
   deben coincidir
```



#### 3.2.3.3.   La fórmula

$$
C = AB
\qquad
c_{ij} = \sum_{k=1}^{n} a_{ik} \, b_{kj}
= a_{i1} b_{1j} + a_{i2} b_{2j} + \cdots + a_{in} b_{nj}
$$

Es decir, $c_{ij}$ es el producto escalar de la **fila $i$** de $A$ con la **columna $j$** de $B$.  

> [!WARNING]
> Los índices matemáticos ($i$, $j$, $k$) empiezan en $1$, y los de Python en $0$. En el código y en los ejemplos usamos **índices de Python**.

En NumPy, para una celda concreta (con `A`, `B`, `i` y `j` ya definidos):

```python
# Producto escalar de la fila i de A con la columna j de B
C_ij = A[i, :] @ B[:, j]

# Equivalente, escrito como la suma de la fórmula
C_ij = sum( A[i, k] * B[k, j] for k in range(A.shape[1]) )
```

##### 3.2.3.3.1.    Caso $n = 2$ (índices de Python)

Cuando $A$ tiene 2 columnas y $B$ tiene 2 filas, cada celda tiene **dos productos**:  

$$
C[i, j] = A[i, 0] \cdot B[0, j] + A[i, 1] \cdot B[1, j]
$$

- Los dos productos de una celda comparten la **misma $i$** (fila de $A$) y la **misma $j$** (columna de $B$).  
- Lo único que cambia entre ellos es el **índice del medio**, `0` y `1`.  

***

#### 3.2.3.4. El Esquema de Falk: ver qué se multiplica con qué

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


#### 3.2.3.5.   Ejemplo ampliado: $3 \times 2$ por $2 \times 3$

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

- $C$ será $3 \times 3$, son **9 celdas**: 
    - El $2$ de en medio **desaparece**
    - Quedan las **filas de $A$** ($m = 3$) por las **columnas de $B$** ($p = 3$)

- Cada celda es un producto escalar de **2 elementos** (porque $n = 2$)

```text
  (3, 2)  @  (2, 3)  =  (3, 3)
      └───────┘
   coinciden (n = 2)
```
  
> [!NOTE]
> Aquí, $m$ y $p$ valen ambos $3$ por mera casualidad:  
>   - $m$ viene de las filas de $A$  
>   - $p$ de las columnas de $B$   
>   
> Con otras formas se distinguirían mejor las tres letras. Por ejemplo, $(2, 3) @ (3, 4) = (2, 4)$, sería:  
>   - $m = 2$
>   - $n = 3$
>   - $p = 4$.
  

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

##### 3.2.3.5.1  Las nueve celdas

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

Ahora, comprobamos con NumPy el ejemplo ampliado:  
-   $A$ de $3 \times 2$
-   $B$ de $2 \times 3$

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
> En general, la multiplicación matricial **no es conmutativa**: 
>   - `A @ B` y `B @ A` pueden dar resultados distintos, o incluso uno de ellos no existir.

> [!TIP]
> Comprueba siempre las formas con `.shape` antes de multiplicar. Es la forma más rápida de encontrar un error de compatibilidad.


---


# 03-003:   Matrices

***

## 3.3.   Transpuesta de una matriz (Transposición de series)

La **traspuesta** de una matriz **intercambia sus filas por columnas**.  

- **Intercambia sus ejes, no toca las componentes de ninguna manera**
- Se representa como $A^T$

Por ejemplo, si tenemos una matriz de 2 filas y 3 columnas:

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{pmatrix}
$$

Su traspuesta seŕa:  

$$
A^T =
\begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6
\end{pmatrix}
$$

```text
A (2×3)                 Aᵀ (3×2)

[1  2  3]  ← fila 0     [1  4]
[4  5  6]  ← fila 1     [2  5]
                        [3  6]
                         ↑   ↑
                    col 0   col 1
```

- La **fila 0** de $A$ `[1, 2, 3]` pasa a ser la **columna 0** de $A^T$  
- La **fila 1** de $A$ `[4, 5, 6]` pasa a ser la **columna 1** de $A^T$  

Elemento a elemento, componente a componente, **los dos índices se intercambian**:  

$$
(A^T)_{ij} = a_{ji}
$$

Por ejemplo, el elemento de la fila 0 y columna 2 de $A$ (un `3`) acaba en la fila 2 y columna 0 de $A^T$.

> [!NOTE]
> Si $A$ tiene forma $(m, n)$, entonces $A^T$ tiene forma $(n, m)$:  
>   - Es decir, la forma cambia de `(2, 3)` a `(3, 2)`
>   - Cambia sus ejes, no sus valores
>   - Repito, no se modifican sus componentes, solo intercambia los ejes

---

#### 3.3.1.     Propiedades básicas de la trasposición de matrices

| Propiedad              | Fórmula                      |
| ---------------------- | ---------------------------- |
| Doble traspuesta      | $(A^T)^T = A$                |
| Suma                   | $(A + B)^T = A^T + B^T$      |
| Multiplicar por escalar | $(kA)^T = k A^T$            |
| Producto de matrices   | $(AB)^T = B^T A^T$           |

> [!WARNING]
> **La trampa del producto traspuesto:**    
>   - En una multiplicación de matrices, **el orden se invierte obligatoriamente**:  
>       * $(AB)^T = B^T A^T$  ( **NUNCA** es $A^T B^T$ )  


##### 3.3.1.1.    ¿Por qué se invierte el orden? (El análisis de dimensiones)

Las matemáticas y las formas de las matrices no permiten otra combinación. Vamos a comprobarlo paso a paso:  

1. **Partimos de las dimensiones originales:**  
   * Si la matriz $A$ es de forma $(m, n)$ ...  
   * ... Y la matriz $B$ es de forma $(n, p)$  

2. **¿Qué forma tiene el resultado traspuesto?**  
   * El producto normal $(AB)$ da como resultado una matriz de forma $(m, p)$ ...  
   * ... Por tanto, su traspuesta $(AB)^T$ invierte esas dimensiones y pasa a ser de forma **$(p, m)$**  

3. **Probamos los dos caminos posibles:**  

   * **El orden correcto ( $B^T A^T$ ):**   
        - $B^T$ es $(p, n)$ y $A^T$ es $(n, m)$  
        - Al multiplicarlas:   
            - $(p, n) @ (n, m) = (p, m)$   
            - **Las formas encajan a la perfección y dan el tamaño esperado**    

   * **El orden incorrecto ( $A^T B^T$ ):**  
        - $A^T$ es $(n, m)$ y $B^T$ es $(p, n)$  
        - Al intentar multiplicarlas:  
            - $(n, m) @ (p, n)$  
            - **Las dimensiones internas no coinciden** (y Python lanzará un `ValueError`)  

```python
B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

## Validamos empíricamente que la propiedad matemática
print(np.array_equal( (A @ B).T, B.T @ A.T) )  # True
```

##### 3.3.1.2.  La diagonal principal de una matriz y la traspuesta, `np.diag()`

La diagonal principal de una matriz, se considera:  
    - **La que comienza en [0, 0]** y termina en [n, n]  
    - Visualmente "de arriba a la izquierda, hasta el final "visual" de dicha diagonal 

En la traspuesta de matrices, **una propiedad impresionante** radica en que **la diagonal principal nunca se modificará**.  

> [!IMPORTANT]
> Aunque, contraintuitivamente, parece que la propiedad de diagonal principal no vaya a cumplirse en matrices que NO son simétricas, en realidad:    
>   1. **siempre va a existir una diagonal principal en cualquier tipo de matriz** sean o no simétricas  
>   2. En consecencia, **siempre va a poder comprobarse la diagonal en la traspuesta frente a su original**  


Consideremos la siguiente matriz:  

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$

- **La diagonal principal está formada por los componentes CUYOS INDICES de FILA y COLUMNA coinciden**:  
    
    - `A[0,0]`, `A[1,1]` y `A[2,2]`  

- DIAGONAL PRINCIPAL dada la matriz:   $1$, $5$, $9$  

- Si trasponemos la misma matriz:  

$$
A^T =
\begin{pmatrix}
1 & 4 & 7 \\
2 & 5 & 8 \\
3 & 6 & 9
\end{pmatrix}
$$

- DIAGONAL PRINCIPAL de la traspuesta SIGUE SIENDO:   $1$, $5$, $9$  

> [!IMPORTANT]
> La regla es:    $(A^T)\_{ij}=A\_{ji}$  
>   - Los elementos de la diagonal principal no se desplazan, **mantienen sus posiciones y valores**
>   - Los elementos que están fuera de la diagonal intercambian sus posiciones de manera simétricas:
>       * Por ejemplo, el $6$ que estaba en `A[1,0]` pasa a `A.T[0,1]`
>   - 

---


### 3.3.2    Transpuesta en NumPy

En NumPy utilizamos `matriz.T` (atributo, como atajo) o `np.transpose(matriz)` (como método), siendo y haciendo exáctamewnte lo mismo:  

```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.shape)    # (2, 3)
print(A.T)
# [[1 4]
#  [2 5]
#  [3 6]]
print(A.T.shape)  # (3, 2)

print(A[0, 2])    # 3
print(A.T[2, 0])  # 3: los índices se intercambian
```


> [!IMPORTANT]
> Una vez más, la traspuesta **no invierte los valores ni los ordena al revés**:  
>  
>   - Unicamente **intercambia los ejes** de filas y columnas

#### 3.3.2.1    Comprobación de la Diagonal Principal, `np.diag()`

Tal y como describimos en las propiedades de la traspuesta de las matrices, podemos hacer una comprobación de su diagonal principal con el método `np.diag(matriz)`:


```python
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

A_traspuesta = A.T.copy()

print(np.diag(A))
print(np.diag(A_traspuesta))
# Ambas devuelven [1, 5, 9] idénticas
```


#### 3.3.2.2      Vista de la traspuesta VS Copia de la traspuesta

> [!WARNING]
> `matriz.T` / `np.transpose(matriz) **NO crean una copia en memoria**:  
>   - Solo hace una **vista preliminar** de los mismos datos con los ejes intercambiados  
>   - No duplican los datos. Solo devuelven una **vista (*view*)**  
>   - Es decir, el mismo bloque de datos original pero "visto desde otro ángulo" con los ejes intercambiados ( lo que, en modelos de datos gigantes ahorra muchísima memoria)  
>   
>  Como comparten memoria, **si modificas un valor en `matriz.T`, se modifica automáticamente en la matriz inicial.**   
> 
>  **Para romper esa conexión, obtener una copia independiente en nueva variable, se utiliza el legacy .copy():  
>   - `matriz.T.copy()`  
>   - `np.transpose(matriz).copy()` 


#### 3.3.2.3    Refresh de Vector a Matriz - .reshape(x, y)

> [!WARNING]
> En un **array de un solo eje** (un vector 1D como `[1, 2, 3]`), `.T` **no hará nada**:  
>   * Porque un array 1D **solo tiene una dimensión (un eje)**.  

No hay "filas" ni "columnas", solo una secuencia plana de números. Transponer una línea recta la deja exactamente igual. Su forma sigue siendo `(3,)`.  

Para convertir un vector plano en una matriz real (de columna o de fila), necesitamos **obligatoriamente añadirle un segundo eje** usando `.reshape(x, y)`.  


```python
v = np.array([1, 2, 3])

print(v.shape)                   # (3,)    <- Vector plano (1 solo eje)
print(v.T.shape)                 # (3,)    <- .T no hace nada en 1D

## Forzamos una estructura de 2D (Matriz Columna):
print(v.reshape(3, 1).shape)     # (3, 1)  <- 3 filas, 1 columna

## Forzamos una estructura de 2D (Matriz Fila):
print(v.reshape(1, 3).shape)     # (1, 3)  <- 1 fila, 3 columnas
```

#### 3.3.2.4    `.reshape(x, y)` - `.copy()` - `np.shares_memory(A, B)`

> [!IMPORTANT]
> `.reshape()`, como '.T',  también funciona en modo Vista ... **siempre que no haya otra opción que crear un nuevo objeto!**:_  

> [!TIP]
> La regla para entender como funcionará un `.reshape()`:  
>   1. **Te da la nueva matriz en modo Vista... siempre que se pueda**
>   2. **Te hace una copia de la matriz si no queda otra**
  

* 1. **Por defecto (La mayoría de las veces es una VISTA):**  
    - Si el array está ordenado de forma contigua en la memoria (como un array recién creado), `.reshape()` **no duplica los datos**. Te devuelve una **vista** con otra forma, lo que significa que **comparte memoria** y modificar un valor puede afectar al original.  

* 2. **La trampa (A veces se convierte en una COPIA):**   
    - Si el array original no es contiguo en memoria (por ejemplo, porque viene de hacerle un corte o una trasposición previa no contigua), NumPy **necesita copiar los datos a un nuevo espacio de memoria** para poder darle la nueva form y ... en ese caso, `.reshape()` devuelve una **copia independiente**.  

* 3. **Ante la duda, `np.shares_memory()`:**  
    - NumPy tiene una función propia llamada **`np.shares_memory()`** para salir de dudas al instante.

* 4. **... y ante la necesidad, `.copy()`:**  
    - Si es necesario hacer que el `.reshape()` sea n objeto totalmente independiente en memoria y no vaya a alterar el original bajo ninguna circunstancia, volvemos a usar el conocido legacy `.copy()`.

```python
a = np.array([1, 2, 3, 4, 5, 6])

# SHARES MEMORY np.shares_memoryu(A, B)

## Hacemos un reshape
A_reshape = a.reshape(3, 2)

## Comprobamos si comparten memoria
print(np.shares_memory(a, A_reshape))  # True? Entonces es una VISTA

## Si modificamos un valor en el reshaped:
A_reshape[0, 0] = 99

print(a)  
# [99,  2,  3,  4,  5,  6]  ... Es decir, se ha modificado el original


# COPY ANTE LA DUDA
A_reshape_independiente = a.reshape(3, 2).copy()
```


##### 3.3.2.4.1.    Ajuste Perfecto Automático, con "Comodín" "-1", `.reshape(-1, 1)`

> [!NOTE]
> **El comodín `-1` en `.reshape(-1, 1)`:**  
>   - En lugar de escribir el número exacto de filas a mano, puedes usar `-1`
>   - Esto le dice a NumPy: 
>   *"Calcula tú automáticamente cuántas filas hacen falta para que encajen todos los elementos, pero déjame exactamente 1 columna"*.
>  
> En ML, es la forma más adecuada para **convertir arrays planos en columnas compatibles con modelos**.  

```python
v = np.array([1, 2, 3])

## El comodín `-1` calcula automáticamente:
print(v.reshape(-1, 1))  

# Transforma v en una columna perfecta
# [[1]
#  [2]
#  [3]]

print(v.reshape(-1, 1).T.shape)  # (1, 3) ... Si a la columna reshapeada le aplicas .T, pasa a ser fila

```

##### 3.3.2.4.2.    ¿Por qué necesito comprender y usar `.reshape()?

* 1.    **Cambiar la orientación de los datos:** 
    - Pasar de datos organizados por filas a organizados por columnas, y al revés.

* 2.    **Hacer compatibles las formas** en una multiplicación matricial

* 3.    **En álgebra lineal y ML:** 
    - Transformar representaciones matriciales

    
Un ejemplo claro para compatibilizar las formas a la hora de multiplicación matricial:  

* Con $A$ de forma $(2, 3)$, `A @ A` no se puede calcular ...
* Pero `A @ A.T` sí

```python
print(A.shape, A.T.shape)  # (2, 3) (3, 2)
# A @ A                    # ValueError: (2, 3) @ (2, 3) ( el 3 y el 2 no coinciden)

print(A @ A.T)
# [[14 32]
#  [32 77]]

print((A @ A.T).shape)     # (2, 2)

```

Las formas encajan porque `A.T` tiene `3` filas, igual que las `3` columnas de `A`: $(2, 3) @ (3, 2) = (2, 2)$.

---

## 3.4.     Determinante de una matriz

EL **determinante de una matriz es un valor escalar**, (un único número), calculado **a partir de una matriz cuadrada**.  

 - Se representa como $\det(A)$ o $|A|$.

> [!NOTE]
> La notación $|A|$ **no es un valor absoluto ni una norma**:  
>   - El determinante **puede ser negativo, cero, positivo**...  


El determinante condensa en un solo número información muy importante sobre la matriz:

-   Si la matriz **tiene, o no, inversa**
-   Cuánto **escala áreas o volúmenes** la transformación que representa
-   Si sus filas o columnas son **redundantes (dependientes entre sí mismas)**


***

### 3.4.1.1 ¿Por qué necesito comprender, resolver y usar la determinante de una matriz?  

* 1. **Saber si una matriz tiene inversa**
    - $A$ es invertible $\iff \det(A) \neq 0$ (ver 3.4.6)
    - Si $\det(A) = 0$, la matriz es **singular** y no existe $A^{-1}$

* 2. **Resolver sistemas de ecuaciones lineales**
    - $A\mathbf{x} = \mathbf{b}$ tiene **solución única** $\iff \det(A) \neq 0$ (ver 3.4.6)
    - Si $\det(A) = 0$, el sistema es **singular**: o no tiene solución, o tiene infinitas

* 3. **Geometría**
    - $|\det(A)|$ es el **factor de escala** de áreas (en $2 \times 2$) o volúmenes (en $3 \times 3$) que aplica la transformación (ver 3.4.3)
    - El **signo** indica si la transformación **invierte la orientación** (positivo: la conserva; negativo: la invierte)
    - $\det(A) = 0$ significa que la transformación **aplasta/colpasa** el espacio a una dimensión menor

* 4. **Detectar redundancia**
    - $\det(A) = 0$ $\iff$ las filas (o columnas) son **linealmente dependientes** entre sí (ver 3.4.6)
    - Es decir, si hay información repetida o derivable de las demás

* 5. **En álgebra lineal y ML**
    - Si las columnas de una matriz de datos $X$ son dependientes (variables redundantes), entonces $\det(X^T X) = 0$
    - En la práctica, para detectar redundancia se usan medidas más fiables que el determinante, como el **rango** (ver 3.4.7.7)


***


### 3.4.2.  Condición de Determinante: LA MATRIZ DEBE SER CUADRADA

> [!IMPORTANT]
> El determinante **solo está definido para matrices cuadradas**:  
>   - Aquella que tienen el **mismo número de filas que de columnas**, es decir, de forma $(n, n)$  

| Matriz       | Forma    | ¿Tiene determinante? |
| ------------ | -------- | -------------------- |
| $2 \times 2$ | `(2, 2)` | Sí                   |
| $3 \times 3$ | `(3, 3)` | Sí                   |
| $2 \times 3$ | `(2, 3)` | **No**               |
| $3 \times 1$ | `(3, 1)` | **No**               |

***




#### 3.4.2.1.    Determinante de una matriz $2 \times 2$

##### 3.4.2.1.1.  Fórmula

Para una matriz de $2 \times 2$:

$$
A =
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
$$

Su determinante es:

$$
\det(A) = ad - bc
$$

Es decir, **el producto de la diagonal principal menos el producto de la diagonal secundaria**:

```text
  [ a, b ]  ↘  diagonal principal:   a * d   (se suma)
  [ c, d ]  ↙  diagonal secundaria:  b * c   (se resta)
```

> [!NOTE]
> La **diagonal principal** es la que ya conoces de la traspuesta:  
>   - Empieza en `[0, 0]`  
>  
> La **diagonal secundaria** es la que adquieres ahora:  
>   - Inverda a la diagonal primaria  
>   - Empieza en `[0, -1]`  

##### 3.4.2.1.2.    Ejemplo

$$
A =
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
$$

$$
\det(A) = (1 \cdot 4) - (2 \cdot 3) = 4 - 6 = \boxed{-2}
$$

> [!NOTE]
> Para una matriz $1 \times 1$, el determinante no tiene más opción que ser su único elemento:  
>   - $\det\big((a)\big) = a$

***

### 3.4.3. Interpretación geométrica - Visualización mental a través de la geometría

Cada columna de una matriz $2 \times 2$ es un **vector**:  
    - Llamémoslas $\mathbf{u}$ y $\mathbf{v}$.
    - Estos dos vectores... **ESTÁN FORMANDO UN PARALELOGRAMO!**



> [!IMPORTANT]
> El valor absoluto del determinante, $|\det(A)|$, es el **área del paralelogramo** formado por las columnas de $A$

Y el **signo** indica el sentido de giro de $\mathbf{u}$ a $\mathbf{v}$:

| $\det(A)$  | Significado                                              |
| ---------- | -------------------------------------------------------- |
| Positivo   | De $\mathbf{u}$ ... a $\mathbf{v}$, gira en sentido **antihorario** |
| Negativo   | De $\mathbf{u}$ ... a $\mathbf{v}$,  gira en sentido **horario**     |
| Cero       | Los vectores quedan **alineados**, el área es $0$        |

![Paralelogramos formados por las columnas de A: determinante positivo, negativo y cero](./img/03-004_determinante.png)

- **Caso 1:**   *determinante positivo*
    - $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$  
    - Con $\mathbf{u} = (2, 0)$ y $\mathbf{v} = (1, 3)$  
    - Su determinante es $2 \cdot 3 - 1 \cdot 0 = 6$   
    - **Area $6$ y giro antihorario**  

- **Caso 2:** *determinante negativo (mismas columnas, intercambiadas)* 
    - $A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$  
    - El paralelogramo es el mismo (área $6$), pero el giro es horarip  
    - Por lo que su determinante es $\det(A) = -6$  

- **Caso 3:**   *determinante cero*
    - $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$  
    - La segunda columna es el **doble** de la primera, así que los vectores están alineados  
    - Su determinante será $\det(A) = 1 \cdot 4 - 2 \cdot 2 = 0$  

> [!TIP]
> Una forma útil de visualizaro mentalmente:  
>    
>   - La matriz $A$ **transforma** el cuadrado unidad (de área $1$) en el paralelogramo de sus columnas.  
>   - Por eso $|\det(A)|$ es el **factor por el que la transformación multiplica las áreas**.  
>  
>   - En $3 \times 3$, el mismo razonamiento se aplica a **volúmenes**.

***




### 3.4.4. Determinante de una matriz $3 \times 3$ (REGLA DE SARRUS)

> [!WARNING]
> La regla de Sarrus **solo funciona para matrices $3 \times 3$**. No se puede extender a $4 \times 4$ ni a tamaños mayores.  

#### 3.4.4.1. Regla de Sarrus

Si estamos hablando de las regla de SArrus, estamos hablando de una matriz de $3 \times 3$:  

$$
A =
\begin{pmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{pmatrix}
$$

1.  Se **repiten las dos primeras columnas a la derecha** a la derecha
2.  Se **suman las tres diagonales descendentes**
3.  Se **restan las tres ascendentes**

```text
  [a  b  c]  a  b       ↘ se suman:  a*e*i,  b*f*g,  c*d*h
  [d  e  f]  d  e       ↙ se restan: c*e*g,  a*f*h,  b*d*i
  [g  h  i]  g  h
```

$$
\det(A) = aei + bfg + cdh - ceg - afh - bdi
$$

Ejemplo:

$$
A =
\begin{pmatrix}
2 & 0 & 1 \\
1 & 3 & 2 \\
1 & 1 & 4
\end{pmatrix}
$$

| Diagonales que se suman       | Producto                       | Diagonales que se restan      | Producto                       |
| ----------------------------- | ------------------------------ | ----------------------------- | ------------------------------ |
| $a \cdot e \cdot i$           | $2 \cdot 3 \cdot 4 = 24$       | $c \cdot e \cdot g$           | $1 \cdot 3 \cdot 1 = 3$        |
| $b \cdot f \cdot g$           | $0 \cdot 2 \cdot 1 = 0$        | $a \cdot f \cdot h$           | $2 \cdot 2 \cdot 1 = 4$        |
| $c \cdot d \cdot h$           | $1 \cdot 1 \cdot 1 = 1$        | $b \cdot d \cdot i$           | $0 \cdot 1 \cdot 4 = 0$        |
| **Total**                     | $25$                           | **Total**                     | $7$                            |

$$
\det(A) = 25 - 7 = \boxed{18}
$$

***


## 3.4.4.2. Desarrollo por cofactores (Laplace), para $n \times n$

El método de Sarrus solo sirve para $3 \times 3$. Para cualquier $n \times n$ existe un método **general y recursivo**:

1. Reducir el determinante $n \times n$ ...
2. ... a varios determinantes de $(n-1) \times (n-1)$ ...
3. ... hasta llegar al $2 \times 2$ !


Antes de la fórmula conviene definir algunos términos:

- **MENOR COMPLEMENTARIO / MENOR** $M_{ij}$
    -   El determinante resultante al **tachar la fila $i$ y la columna $j$**

- **COFACTOR / ADJUNTO** $C_{ij} = (-1)^{i+j}\,M_{ij}$
    -   El menor con el **factor de signo** ya aplicado

- **FACTOR DE SIGNO / SIGNO DEL COFACTOR** $(-1)^{i+j}$
    - Depende **solo de la posición $(i,j)$**, no del valor. 

Para visualizar mentalmente la alplicación del factor de signo al menor, podemos verlo  **como un tablero de ajedrez**:

```text
posición (i, j)
signo = (-1) ^ (i + j) 

     (j)
(i) [ +  -  +  - ]    fila 0:  +  -  +  -
    [ -  +  -  + ]    fila 1:  -  +  -  +
    [ +  -  +  - ]    fila 2:  +  -  +  -
    [ -  +  -  + ]    fila 3:  -  +  -  +

```

### 3.4.4.2.1.  Fórmula (desarrollo por la fila $i$)

$$
\det(A) = \sum_{j=0}^{n-1} a_{ij}\,C_{ij} = \sum_{j=0}^{n-1} (-1)^{i+j}\,a_{ij}\,M_{ij}
$$

Es decir, **cada elemento de la fila elegida multiplica a su cofactor, y se suman todos**.  

### 3.4.4.2.2. Caso $3 \times 3$ y ejemplo


Para $n=3$, desarrollando por la primera fila ($i=0$):  

$$
\det(A) = a_{00}M_{00} - a_{01}M_{01} + a_{02}M_{02}
$$

Cada $M_{0j}$ es un determinante $2 \times 2$. Con la matriz del ejemplo:  

$$
A = \begin{bmatrix} 
2 & 0 & 1 \\  
1 & 3 & 2 \\  
1 & 1 & 4 \end{bmatrix}
$$


Para visualizarlo mentalmente haremos las reducciones paso a paso visual:

1.  Dada la matriz:
```text
[2   0   1]
[1   3   2]
[1   1   4]
```

2. Generamos las matrices para tachar:  
    
    - Generamos $M_{00}$, $M_{01}$, $M_{02}$  
    
    - SIEMPRE FILA 0 TACHADA para todas $M_{0j}$  
        - Para $M_{00}$, $j_0$ tacha la primera columna  
        - Para $M_{01}$, $j_1$ tacha la segunda columna  
        - Para $M_{02}$, $j_2$ tacha la tercera columna  

```text
   j = 0              j = 1              j = 2
 [X  X  X]          [X  X  X]          [X  X  X]
 [X  3  2]          [1  X  2]          [1  3  X]
 [X  1  4]          [1  X  4]          [1  1  X]
```


3. Una vez tachadas, ya tenemos reducidas a $2 \times 2$ cada matriz:  
```text
M_00 =  [3 2]         
        [1 4]
                 
M_01 =  [1 2]
        [1 4]

M_02 =  [1 3]
        [1 1]
```

4. Aplicamos $\sum_{j=0}^{n-1} (-1)^{i+j}\,a_{ij}\,M_{ij}$ a cada matriz:
```text
M_00    =       [3 2]
                [1 4]
        =   3 * 4  -  2 * 1
        =   10                     

M_01    =       [1 2]
                [1 4]
        =   1 * 4  -  2 * 1
        =   2 

M_02    =       [1 3]
                [1 1]
        =   1 * 1  - 3 * 1
        =   -2
```

Sustituyendo en la fórmula (con los signos $+,-,+$ de la fila 0):  

$$
\det(A) = 2\cdot(10) - 0\cdot(2) + 1\cdot(-2) \\
= 20 - 0 - 2 \\ 
= \boxed{18}
$$

> [!TIP]
> Se puede desarrollar por **cualquier fila o columna**, pero conviene elegir la que tenga **más ceros**:  
>   - **Cada cero anula su término entero** (aquí, el $0$ de la primera fila elimina el segundo término)




### 3.4.4.2.3.  Casos grandes, $5 \times 5$:   Estrategia de "crear ceros"

Para $n \ge 4$ el desarrollo directo por cofactores **no es rentable**: 

- Un $5 \times 5$ genera cinco menores $4 \times 4$ ... 
- ... Cada uno de ellos genera cuatro $3 \times 3$ ...
- ... Cada uno de estos, a su vez, generan tres $2 \times 2$ ...
- ... y así sucesivamente, explotando en cálculos.


Es decir, el número de términos crece como $n!$, exponencialmente.

Para casos gigantes, a forma habitual de trabajar es:

1. **Usar operaciones elementales entre filas para crear ceros en una fila o columna determinada**
2. Y, después, desarrollar por esa línea.


> [!NOTE]
> Las operaciones elementales entre filas **no cambian el determinante** salvo que se intercambien filas (donde, en consecuencia, cambiaría el signo).  
>  
> En particular, sumar a una fila un múltiplo de otra **deja el determinante igual**.

Dada la siguiente $5 \times 5$:  

$$
A = \begin{pmatrix}
1 & 2 & 0 & 0 & 3 \\
0 & 1 & 4 & 0 & 0 \\
2 & 0 & 1 & 5 & 0 \\
0 & 3 & 0 & 1 & 2 \\
1 & 0 & 0 & 0 & 1
\end{pmatrix}
$$


1.  **CREAR CEROS EN LA PRIMERA COLUMNA**   
- Decidimos usar las la fila 1:  
    - Tiene un $1$ en la posición $(1,1)$)
    - Anulamos los valores que no sean ceros:
        - El $2$ de la fila 3, y el $1$ de la fila 5:    
            - $F_3 \leftarrow F_3 - 2F_1$ (anula el $2$ de $(3,1)$)  
            - $F_5 \leftarrow F_5 - F_1$ (anula el $1$ de $(5,1)$)  

$$
A' = \begin{pmatrix}
1 & 2 & 0 & 0 & 3 \\
0 & 1 & 4 & 0 & 0 \\
0 & -4 & 1 & 5 & -6 \\
0 & 3 & 0 & 1 & 2 \\
0 & -2 & 0 & 0 & -2
\end{pmatrix}
$$



2. **DESARROLLAR POR LA PRIMERA COLUMNA** 

- Solo queda el término $a_{11}=1$, con signo $(-1)^{1+1}=+$:

$$
\det(A) = 1 \cdot \det\begin{pmatrix}
1 & 4 & 0 & 0 \\
-4 & 1 & 5 & -6 \\
3 & 0 & 1 & 2 \\
-2 & 0 & 0 & -2
\end{pmatrix}
$$



3.  **CREAR CEROS en la PRIMERA COLUMNA DEL $(n-1) \times (n-1)$ inmediatamente inferior**  
- En este caso, en columna del $4 \times 4$.
- Usamos la fila 1 ($1$ en $(1,1)$) para anular el $-4$ y el $3$:

    - $F_2 \leftarrow F_2 + 4F_1$
    - $F_3 \leftarrow F_3 - 3F_1$

$$
\det = \det\begin{pmatrix}
1 & 4 & 0 & 0 \\
0 & 17 & 5 & -6 \\
0 & -12 & 1 & 2 \\
-2 & 0 & 0 & -2
\end{pmatrix}
$$

4. **SEGUIR DESARROLLANDO a $n-1$**
- Ya hay dos ceros en la primera columna, pero el $-2$ de la fila 4 sigue ahí, por lo que podemos... :
    - O bien desarrollar por la primera columna (dos términos)
    - O bien crear un cero más con $F_4 \leftarrow F_4 + 2F_1$:

$$
\det = \det\begin{pmatrix}
1 & 4 & 0 & 0 \\
0 & 17 & 5 & -6 \\
0 & -12 & 1 & 2 \\
0 & 8 & 0 & -2
\end{pmatrix}
= 1 \cdot \det\begin{pmatrix}
17 & 5 & -6 \\
-12 & 1 & 2 \\
8 & 0 & -2
\end{pmatrix}
$$

5.  **LLEGAMOS a $3 \times 3$, Sarrus o cofactores**
- Este $3 \times 3$ ya se resuelve directamente:

$$
\begin{aligned}
\det\begin{pmatrix}
17 & 5 & -6 \\
-12 & 1 & 2 \\
8 & 0 & -2
\end{pmatrix}
&= 17\cdot1\cdot(-2) + 5\cdot2\cdot8 + (-6)\cdot(-12)\cdot0 \\
&\quad - (-6)\cdot1\cdot8 - 17\cdot2\cdot0 - 5\cdot(-12)\cdot(-2) \\
&= -34 + 80 + 0 - (-48) - 0 - 120 \\
&= -34 + 80 + 48 - 120 \\
&= \boxed{-26}
\end{aligned}
$$

$$
\begin{aligned}
\det(A) = \boxed{-26}
\end{aligned}
$$


> [!NOTE]
> **El patrón es claro:** en cada paso elegimos la fila/columna con más ceros y creamos más ceros con operaciones entre filas. Así, el número de términos que hay que arrastrar se mantiene pequeño.
>
> En este ejemplo concreto, el desarrollo directo del $5 \times 5$ habría requerido:     
>   1. Evaluar 5 menores $4 \times 4$ ...    
>   2. Cada uno de estos, evaluar 4 menores $3 \times 3$ cada uno de estos ...  
>   3. 3 menores $2 \times 2$...  
>   Y así sucesiva y recursivamente, lo que no es nada rentable en términos de cálculo.    
>   En total, **cientos de determinantes** frente a los **6 pasos** que acabamos de dar.  



### 3.4.4.2.4. Estrategia práctica

Para $n\ge4$ **no conviene desarrollar directamente por cofactores**: el coste crece como $n!$.  

El procedimiento habitual es:

1. **Crear ceros** con operaciones elementales entre filas (sumar múltiplos de otra fila no cambia el determinante; intercambiar filas cambia el signo).
2. **Desarrollar por la fila o columna con más ceros**, reduciendo el orden en 1.
3. **Repetir** hasta llegar a $3 \times 3$ (Sarrus) o $2 \times 2$ (fórmula directa).

> [!NOTE]
> Para un $4 \times 4$ o mayor, el método **más eficiente** no es Laplace sino la **ELIMINACIÓN GAUSSIANA** (descomposición Lower-Upper, matrices triangulares), de orden $n^3$.  
> 
> Laplace se estudia porque es la **definición recursiva** del determinante y porque permite demostrar propiedades; en cálculo numérico se usa Descomposición LU, en el caso de las matrices triangulares que viene a continuación.  


***


#### 3.4.4.3. El fascinante mundo de las MATRICES TRIANGULARES

Una **matriz triangular** es aquella en la que todos los elementos a un lado de una de las diagonales son **cero**.  
    - Los elementos no nulos forman un "triángulo" al otro lado de la diagonal.

Hay **dos familias**, según la diagonal sobre la que se construye el triángulo:  

1. **Triangular Principal (o simplemente triangular)**  
    - El triángulo se construye sobre la **diagonal principal**

2. **Triangular Secundaria (o Antidiagonal)**
    - El triángulo se construye sobre la **diagonal secundaria**


Y, dentro de cada familia, **dos subtipos**, según hacia dónde mire el triángulo:

| Familia | Subtipo | Dónde están los ceros | Nombre habitual |
|---|---|---|---|
| Principal | Superior | **Por debajo** de la diagonal principal | Triangular superior ($U$) |
| Principal | Inferior | **Por encima** de la diagonal principal | Triangular inferior ($L$) |
| Secundaria | Superior | **Por debajo** de la diagonal secundaria | Triangular secundaria superior |
| Secundaria | Inferior | **Por encima** de la diagonal secundaria | Triangular secundaria inferior |

> [!NOTE]
> La nomenclatura "superior/inferior" es habitual, y refiere a **dónde queda el triángulo de datos no nulos**, no a la ubicación de los ceros.  




  
##### 3.4.4.3.1. Triangulares principales (sobre la diagonal principal)

1.  **Triangular superior ($U$):**      *ceros por debajo de la diagonal principal, datos arriba*          

$$
U = \begin{pmatrix}
\mathbf{2} & 1 & 3 \\
0 & \mathbf{4} & 1 \\
0 & 0 & \mathbf{5}
\end{pmatrix}
\quad\Longrightarrow\quad
\det(U) = 2 \cdot 4 \cdot 5 = \boxed{40}
$$

2.  **Triangular inferior ($L$):**      *ceros por encima de la diagonal principal, datos abajo*      

$$
L = \begin{pmatrix}
\mathbf{5} & 0 & 0 \\
2 & \mathbf{8} & 0 \\
1 & 9 & \mathbf{3}
\end{pmatrix}
\quad\Longrightarrow\quad
\det(L) = 5 \cdot 8 \cdot 3 = \boxed{120}
$$

> [!TIP]
> **FUNDAMENTAL PARA TRIANGULAR PRINCIPAL**:  
>   
>   - Más adelante, al desarrollar por Laplace, casi todos los términos colapsan, y el determinante de **cualquier matriz triangular principal** (superior o inferior) es simplemente el **producto de los elementos de su diagonal principal**. Memorízalo.  






##### 3.4.4.3.2. Triangulares secundarias (sobre la diagonal secundaria)

La **diagonal secundaria** (o antidiagonal) va de la esquina superior derecha a la inferior izquierda.  
Y, sobre ella se construyen los otros dos subtipos:  


3.  **Triangular secundaria superior:**     *ceros por debajo de la diagonal secundaria, datos arriba*  

$$
U_s = \begin{pmatrix}
0 & 0 & \mathbf{3} \\
0 & \mathbf{4} & 2 \\
\mathbf{5} & 6 & 1
\end{pmatrix}
$$


4.  **Triangular secundaria inferior:**     *ceros por encima de la diagonal secundaria, datos abajo*  

$$
L_s = \begin{pmatrix}
1 & 2 & \mathbf{3} \\
4 & \mathbf{5} & 0 \\
\mathbf{6} & 0 & 0
\end{pmatrix}
$$

> [!IMPORTANT]
> **FUNDAMENTAL PARA TRIANGULAR SECUNDARIA**  
>  
>   - El determinante es el **producto de los elementos de la diagonal secundaria**, multiplicado por un signo $(\pm 1)$ que depende del tamaño $n \times n$.  
>   
>   - El signo aparece porque, para llevar la matriz a forma triangular principal, hay que **permutar filas** (o columnas), y cada permutación cambia el signo del determinante.
>
>   - En concreto, el signo es $(-1)^{\lfloor n/2 \rfloor}$:
>   
>       - $n = 2$: signo $(-1)^1 = -1$
>       - $n = 3$: signo $(-1)^1 = -1$
>       - $n = 4$: signo $(-1)^2 = +1$
>       - $n = 5$: signo $(-1)^2 = +1$



##### 3.4.4.3.3. **Comprobación con los ejemplos $3 \times 3$ anteriores** (producto de la diagonal secundaria, con signo $-1$ para $n=3$)

1. Para $U_s$:  
    - La diagonal secundaria es $(3, 4, 5)$
    - Producto $3 \cdot 4 \cdot 5 = 60$  
    - Con signo $(-1)^{\lfloor 3/2 \rfloor} = (-1)^1 = -1$  
        * $$\det(U_s) = -60$$

3. Para $L_s$:  
    - La diagonal secundaria es $(3, 5, 6)$
    - Producto $3 \cdot 5 \cdot 6 = 90$
    - Con el mismo signo
        * $$\det(L_s) = -90$$

> [!NOTE]
> **¿Por qué el signo depende solo de la permutación de $n$?** 
>   
>   - Una vez más... porque, para llevar una triangular secundaria a triangular principal, hay que invertir el orden de las filas (o de las columnas)  
>   - Invertir $n$ elementos requiere $\lfloor n/2 \rfloor$ intercambios, y cada intercambio multiplica el determinante por $-1$. De ahí $(-1)^{\lfloor n/2 \rfloor}$  


##### 3.4.4.3.4.    Visualizar mentalmente las diagonales

```text
Datos = 💵  Cero = 0️⃣   

                DIAGONAL PRINCIPAL = ⭐       DIAGONAL SECUNDARIA = ☄️

SUPERIOR            [⭐ 💵 💵]                     [0️⃣ 0️⃣ ☄️]
(datos arriba,      [0️⃣ ⭐ 💵]                     [0️⃣ ☄️ 💵]
 ceros abajo)       [0️⃣ 0️⃣ ⭐]                     [☄️ 💵 💵]

Determinante =  Producto Diagonal Principal     Determinante =  Producto Diagonal Secundaria


INFERIOR            [⭐ 0️⃣ 0️⃣]                     [💵 💵 ☄️]
(datos abajo,       [💵 ⭐ 0️⃣]                     [💵 ☄️ 0️⃣]
 ceros arriba)      [💵 💵 ⭐]                     [☄️ 0️⃣ 0️⃣]

Determinante = Producto diagonal Principal      Determinante =  Producto Diagonal Secundaria
```


***

### 3.4.5. Propiedades básicas de la determinante de una matriz

| Propiedad                                   | Fórmula                                    |
| ------------------------------------------- | ------------------------------------------ |
| Matriz identidad                            | $\det(I) = 1$                              |
| Traspuesta                                  | $\det(A^T) = \det(A)$                      |
| Producto de matrices                        | $\det(AB) = \det(A) \cdot \det(B)$         |
| Multiplicar por un escalar (matriz $n \times n$) | $\det(kA) = k^n \cdot \det(A)$        |
| Intercambiar dos filas (o dos columnas)     | El determinante **cambia de signo**        |
| Fila (o columna) de ceros                   | $\det(A) = 0$                              |
| Dos filas (o columnas) iguales o proporcionales | $\det(A) = 0$                          |
| Las sumas det(A + B) y det(A) + det(B) no cumplen | Distintas determinantes              |
| Matriz triangular principal (superior o inferior) | **Producto de su diagonal principal** |
| Matriz triangular secundaria (superior o inferior) | **Producto de su diagonal secundaria**, con signo $(\pm 1)$ según $n$ |

> [!WARNING]
> **La trampa del escalar:**  
>   - $\det(kA) = k^n \det(A)$, no $k \cdot \det(A)$  
    - Multiplicar una matriz $2 \times 2$ por $3$ multiplica su determinante por $3^2 = 9$, porque se escalan **las dos columnas** y, con ellas, el área en las dos direcciones  

> [!WARNING]
> Además, **la suma NO se comporta igual:**  
>   - En general, $\det(A + B) \neq \det(A) + \det(B)$
>   - El determinante **puede respetar el producto, pero NO LO SUMA**


---

### 3.4.6.  Matriz Singular, *¿Qué significa que el determinante sea cero?*


Un determinante cero indica que **las filas (o columnas) son dependientes**:  

-   Alguna se puede obtener combinando las demás  
-   Geométricamente, el paralelogramo (o el volumen en $3 \times 3$) **se aplasta/colapsa**. y su área se vuelve cero
-   **NO tiene inversa**

| $\det(A)$            | La matriz es ..                    | Consecuencia                                      |
| -------------------- | ---------------------------------- | ------------------------------------------------- |
| **Distinto de cero** | **Regular** (invertible)           | **Tiene inversa**                                 |
| **Igual a cero**     | **Singular** (no invertible)       | **No tiene inversa**                              |



Un caso clásico:

$$
S =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$

La tercera fila se obtiene a partir de las otras dos:  
    - $2 \cdot (4, 5, 6) - (1, 2, 3) = (7, 8, 9)$
    - Por tanto, $\det(S) = 0$ ... la matriz es **singular**

> [!IMPORTANT]
> Para una matriz cuadrada $A$, un sistema $A\mathbf{x} = \mathbf{b}$ tiene **solución única** si y solo si $\det(A) \neq 0$.

---

### 3.4.7. Determinantes en NumPy

> [!IMPORTANT]
> **Nuevos métodos que añadimos a nuestra colección!**  
>   
> - `np.linalg.det(M)`: *calcula el* ***determinante*** *de una matriz cuadrada `M`*  
>       * Devuelve un `float`, aunque `M` sea de enteros (por eso el resultado es aproximado)  
>       * Lanza `LinAlgError` si `M` no es cuadrada  
>   
> - `np.diag(M)`: *tiene* ***dos caras*** *según lo que reciba*  
>       * Con una **matriz 2D**, **extrae** su diagonal principal como vector 1D  
>       * Con un **vector 1D**, **construye** una matriz diagonal a partir de él  
>   
> - `np.isclose(a, b)`: *compara dos números de manera fiable (no como con `==`)**  
>       * Devuelve `True` si están "suficientemente cerca"  
>       * Necesario porque los cálculos floats (casi) nunca dan el valor exacto  



#### 3.4.7.1. `np.linalg.det()`

Con NumPy utilizamos `np.linalg.det(A)`:  

```python
A = np.array([
    [1, 2],
    [3, 4]
])

determinante = np.linalg.det(A)

print(determinante)        # -2.0000000000000004
print(type(determinante))  # <class 'numpy.float64'>
```

> [!NOTE]
> Aunque la matriz sea de enteros, **el resultado SIEMPRE es un `float`**, y por tanto **aproximado**.  
> Por ello, hay distintos métodos para recabar o compara determinantes, trabajando en floats, con escalas muy amplias, etc.



#### 3.4.7.2.   `np.isclose()`,  comparando resultados en coma flotante: 

NumPy, que trabaja con números en **coma flotante**, puede dar determinantes con pequeños errores de redondeo. Por eso, como vimos en vectores y al comienzo de matrices, **NUNCA se hace una comparación directa `==`**.  

Para ello, `np.isclose(valor, objetivo)` "alisa" los coma-flotantes para hacer las comparaciones de la forma adecuada:  

```python
print(determinante == -2)            # False
print(np.isclose(determinante, -2))  # True
```

Lo mismo ocurre al comprobar si un determinante es **prácticamente cero**:

```python
S = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

d = np.linalg.det(S)

print(d)                 # 6.66133814775094e-16
print(np.isclose(d, 0))  # True
```

> [!TIP]
> Existen varios enfoques para portar los valores en notación ciéntifica (que ocurrirá siempre con las matrizes singulares, determinantes cero) a valores visualmente asimilados:  
>   1. El primero, adaptarse a usar notación científica. Un `6.66133814775094e-16` ya te está hablando de la tolerancia, diciendo que tiene muuuuchos ceros por delante en los decimales (`0.00000000000000000066133814...`, $10^{-16}$ ), viendo que **APARENTEMENTE es una singular, determinante cero** (aparentemente ...).  
>   2. Redondear con `round(determinante, decimales)`
>   3. Configurar NumPy nada más importarlo para que muestre los componentes de arrays tal y como tú le indiques, `np.set_printoptions(suppress=True, precision=4)` ... y, después, mostrando la determinante dentro de un array, `np.array( np.linalg(matriz) )`
>   4. Interpolar string siempre que NO necesites usar el valor numérico después,  `f"{determinante:.xf}"` (usando x como decimales deseados)
>  
> **Lo más adecuado es adaptarse a la notación científica; a efectos de la determinante de una matriz no es primordial extraer el valor exacto si sabes que es singular - cero - cerana a cero** (o sí, como veremos más adelante, usamos otros métodos para determinar la singularidad, o no, de una matriz).  


> [!WARNING]
> Por el mismo motivo, conviene entender que Python puede darte el mismo valor matemático usando tipos distintos:  
>   - `float`: $\det(A)$ y $\det(A^T)$ son iguales, pero NumPy puede darlos con **diferencias en las últimas cifras**  
>   - `np.isclose()` nos sirve de ayuda  

```python
print(np.linalg.det(A))    # -2.0000000000000004
print(np.linalg.det(A.T))  # -2.0
print(np.linalg.det(A) == np.linalg.det(A.T))             # False
print(np.isclose(np.linalg.det(A), np.linalg.det(A.T)))   # True
```



#### 3.4.7.3.   Comprobación manual, deconstrucción paso a paso

**Matriz $2 \times 2$**, con la fórmula $ad - bc$:  

```python
a, b = A[0]
c, d = A[1]

det_manual = a * d - b * c

print(det_manual)                                   # -2 (entero exacto)
print(np.isclose(det_manual, np.linalg.det(A)))     # True
```

**Matriz $3 \times 3$**, con la regla de Sarrus:  

```python
P = np.array([
    [2, 0, 1],
    [1, 3, 2],
    [1, 1, 4]
])

a, b, c = P[0]
d, e, f = P[1]
g, h, i = P[2]

positivos = a * e * i + b * f * g + c * d * h  # 25
negativos = c * e * g + a * f * h + b * d * i  # 7

det_sarrus = positivos - negativos

print(det_sarrus)                # 18
print(np.linalg.det(P))          # 17.999999999999996
print(np.isclose(det_sarrus, np.linalg.det(P)))  # True

# Para visualizar en Python la fórmula matemática exacta real, aunque sea dar un paso más
aei = a * e * i
bfg = b * f *g
cdh = c * d * h

ceg = c * e * g
afh = a * f * h
bdi = b * d * i

positivos_negativos_en_serie_es_la_determinante_literal = aei + bfg + cdh - ceg - afh - bdi

print(positivos_negativos_en_serie_es_la_determinante_literal)
print(np.isclose(positivos_negativos_en_serie_es_la_determinante_literal, determinante_sarrus))
```

> [!NOTE]
> El cálculo manual con enteros da **exactamente** `-2` y `18`; NumPy da valores **aproximados**. Ambos son correctos: la diferencia es solo de redondeo.



#### 3.4.7.4.   `LinAlgError`:  Si la matriz no es cuadrada

NumPy lanza un error:

```python
M = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(M.shape)  # (2, 3)
# np.linalg.det(M)  # LinAlgError: Last 2 dimensions of the array must be square
```

> [!TIP]
> Antes de calcular, comprueba que la matriz es cuadrada: `M.shape[0] == M.shape[1]`.  
> Añade una condición-salvaguarda para este caso en aquellos programas que no quieres que se detengan por este motivo.



#### 3.4.7.5. Verificando las propiedades

```python
A = np.array([ 
    [1, 2],
    [3, 4] 
])

B = np.array([
    [2, 0],
    [1, 3]
])

# det(A^T) = det(A)
print(np.isclose(np.linalg.det(A.T), np.linalg.det(A)))                       # True

# det(AB) = det(A) * det(B)
print(np.isclose(np.linalg.det(A @ B), np.linalg.det(A) * np.linalg.det(B)))  # True

# det(kA) = k^n · det(A), con n = 2
print(np.isclose(np.linalg.det(3 * A), 3**2 * np.linalg.det(A)))              # True

# Intercambiar filas cambia el signo
print(np.isclose(np.linalg.det(A[::-1]), -np.linalg.det(A)))                  # True

# La suma NO se cumple
print(np.isclose(np.linalg.det(A + B), np.linalg.det(A) + np.linalg.det(B)))  # False
```



Y la propiedad de la matriz triangular principal superior, con `np.diag()` y `np.prod()`:

```python
U = np.array([
    [2, 1, 3],
    [0, 4, 1],
    [0, 0, 5]
])

print(np.prod(np.diag(U)))  # 40
print(np.linalg.det(U))     # 39.99999999999998 (≈ 40)
```

##### 3.4.7.5.1. Un apunte al fascinante mundo de las matrices triangulares

> [!IMPORTANT]
> **Nuevo método que añadimos a nuestra colección!**:       `np.fliplr(M)`  (y `np.flipud(M)`)
>
>   - Invierte el orden de las **columnas** de `M` (espejo horizontal)  
>   - Es la forma de poder "girar" la matriz para que la **diagonal secundaria** pase a ser como diagonal principal, y así poder extraerla con `np.diag`  
>       * Para el flip up-down, **invertir las filas** (espejo vertical) está `np.flipud(M)`-
>       * Muy útil para trabajar con triangulares secundarias, como veremos a continuación.

- `np.diag(M)` extrae la **diagonal principal** de `M` 
    - Para una **triangular principal** (superior o inferior), `np.prod(np.diag(M))` da directamente su determinante (sin signos ni permutaciones) 

- Para una **triangular secundaria**, `np.diag` **NO** da la diagonal relevante (da la principal, que está mezclada con ceros y datos)  
    - Hay que **girar** la matriz primero con `np.fliplr(M)`, y entonces `np.diag(np.fliplr(M))` sí devuelve la diagonal secundaria  
    - El determinante es `np.prod(np.diag(np.fliplr(M)))`, multiplicado por el signo $(-1)^{\lfloor n/2 \rfloor}$ (el que vimos en 3.4.4.3.2)  



Ejemplo con las dos triangulares secundarias de 3.4.4.3.2:

```python
U_s = np.array([
    [0, 0, 3],
    [0, 4, 2],
    [5, 6, 1]
])

L_s = np.array([
    [1, 2, 3],
    [4, 5, 0],
    [6, 0, 0]
])

# np.diag directo da la diagonal PRINCIPAL
print(np.diag(U_s))              # [0 4 1]   <- mezcla de ceros y datos
print(np.diag(L_s))              # [1 5 0]   <- mezcla de ceros y datos

# Girando con np.fliplr(), la diagonal secundaria pasa a ser la principal
print(np.diag( np.fliplr(U_s) ))   # [3 4 5]   <- diagonal secundaria de U_s
print(np.diag (np.fliplr(L_s) ))   # [3 5 6]   <- diagonal secundaria de L_s


# Determinante = producto de la diagonal secundaria * signo (-1)^(n//2), con n = 3
signo = (-1) ** (3 // 2)         # -1
print(signo * np.prod( np.diag( np.fliplr(U_s) ) ))   # -60
print(signo * np.prod( np.diag( np.fliplr(L_s) ) ))   # -90


# Comprobación con np.linalg.det()
print(np.linalg.det(U_s))        # -59.99999999999999  (≈ -60)
print(np.linalg.det(L_s))        # -90.0
```

- **La descomposición LU** (que trabajaremos más adelante) factoriza una matriz como $A = LU$, con $L$ triangular inferior y $U$ triangular superior:  
    - Por la propiedad del producto, $\det(A) = \det(L)\det(U)$, y cada uno es el producto de su diagonal  
    - De ahí que LU sea $O(n^3)$ (no hay que desarrollar cofactores, solo multiplicar diagonales)  


***





#### 3.4.7.6.   Laplace - Implementación manual por cofactores

> [!IMPORTANT]
> **Otro nuevo método desbloqueado!**:    `np.delete(matriz, posicion, axis=eje)`  
>  
> Compatibilísima con `np.vstack()` / `np.hstack()` (las que añaden una serie vertical (fila) u horizontal (columna)  voluntad).

```python
M = np.array([[10, 2, 3], [4, 5, 6]])
print(M)

# AÑADE UNA SERIE VERTICAL (fila), tres componentes
M = np.vstack( ( M, np.ones(3, dtype=int) ) )
print(M)

# AÑADE OTRA SERIE VERTICAL (fila), tres componentes
M = np.vstack( ( M, np.zeros(3, dtype=int) ) )
print(M)

"""
[[10  2  3]
 [ 4  5  6]
 [ 1  1  1]
 [ 0  0  0]]
"""

# ELIMINA, del EJE 0 (filas) la serie 3 (cuarta)
M = np.delete(M, -1, axis=0)
print(M)
"""
[[10  2  3]
 [ 4  5  6]
 [ 1  1  1]]
"""

# ELIMINA, del EJE 0 (filas) la serie 2 (tercera)
M = np.delete(M, 2, axis=0)
print(M)
"""
[[10  2  3]
 [ 4  5  6]]
"""
```


Ahora, para el desarrollo manual por cofactores, recursivos, vamos a hacerlo con su propia clase y método.  

- Traducimos la fórmula $\det(A)=\sum_j (-1)^{0+j} a_{0j} M_{0j}$ (desarrollo por la **primera fila**) a una función **recursiva**:
    * Un caso general que llama a la misma función con matrices más pequeñas
    * Dos casos base donde la recursión se detiene




```python
class DeterminanteManual:
    """Calcula el determinante por desarrollo de cofactores (primera fila)"""

    @staticmethod
    def calcular(matriz):
        
        matriz = np.asarray(matriz)

        condicion_dim = matriz.ndim != 2
        condicion_cuadrada = matriz.shape[0] != matriz.shape[1]

        if condicion_dim:
            print("No es viable la matriz NO es bidimensional!")
            return False
        if condicion_cuadrada:
            print("No es viable, la matriz NO es cuadrada!")
            return False


        n = matriz.shape[0]

        if n == 1:
            return matriz[0, 0]
        
        if n == 2:
            return ( matriz[0, 0] * matriz[1, 1] ) - ( matriz[0, 1] * matriz[1, 0] )

        total = 0

        for j in range(n):
            
            menor = np.delete(np.delete(matriz, 0, axis=0), j, axis=1)  # tacha fila 0 y columna j
            signo = (-1) ** j                                      # signos alternos
            
            total += signo * matriz[0, j] * DeterminanteManual.calcular(menor)

        return total


        
# PARTE 1, usar los métodos vstack, hstack y delete citados
A = np.array([ [1, 2], [3, 4] ])
P = np.array([ [2, 0, 1], [1, 3, 2], [1, 1, 4] ])
S = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
U = np.array([ [2, 1, 3], [0, 4, 1], [0, 0, 5] ])


M = np.array([[10, 2, 3], [4, 5, 6]])

print(M)
M = np.vstack( ( M, np.ones(3, dtype=int) ) )
print(M)
M = np.vstack( ( M, np.zeros(3, dtype=int) ) )
print(M)
M = np.delete(M, 3, axis=0)
print(M)
M = np.delete(M, -1, axis=0)
print(M)




print(DeterminanteManual.calcular(A))  # -1
print(DeterminanteManual.calcular(P))  # 16
print(DeterminanteManual.calcular(S))  # -47  (exactamente, sin error de redondeo)
print(DeterminanteManual.calcular(U))  # 5
print(DeterminanteManual.calcular(M))  # La salvaguarda explítica de matriz cuadrada salta "No es viable, la matriz NO es cuadrada!"
```

> [!IMPORTANT]
> Con matrices de enteros, este cálculo es **exacto**:  
>   - Para $S$ da `0`, mientras que NumPy puede dar un valor minúsculo.  
>  
>  Pero esto **NO se usa en la práctica**: el desarrollo por cofactores crece con $n!$ operaciones, y con NumPy tenemos métodos mucho más eficiente (como la citada descomposición LU con matrices triangulaes, del orden de $n^3$).

> [!NOTE]
> Ciertas decisiones de código, se implemntan tal cual para tratar de simplificar y mejorar la visualización en terminal.



***

#### 3.4.7.7. Un determinante pequeño NO siempre significa ser matriz singular

> [!IMPORTANT]
> **Nuevos métodos que añadimos a nuestra colección:**  
>  
> - `np.isclose(a, b, rtol=, atol=)`, que ahora recibe un nuevo **poder para manejar tolerancias en comparaciones**  
>       * **Compara dos números con tolerancia** (por defecto `rtol=1e-5`, `atol=1e-8`)  
>       * Devuelve `True` si se cumple:
>         $$|a - b| \le \text{atol} + \text{rtol} \cdot |b|$$  
>       * `atol=` es la **tolerancia absoluta**, el margen en las mismas unidades que `a` y `b`  
>           - Es la que **"manda" cuando comparamos contra cero**, porque `rtol * |0| = 0` y el término relativo desaparece  
>       * `rtol=` es la **tolerancia relativa**, un margen proporcional a $|b|$  
>           -  Es la que **"manda" cuando comparamos valores grandes** que deberían coincidir, donde un `atol` fijo sería demasiado estricto  
>       * **Útiles para comparar los determinantes con tolerancias, pero para definir la singularidad en estos casos conviene usar `np.linalg.matrix_rank(M)`**  
>           - *(Como se indica anteriormente, hay muchos enfoques para trabajar con tolerancias, y la mejor manera es asumirlas, usarlas, no evitarlas!)*  
>  
> - `np.linalg.matrix_rank(M)`, para **definir la singularidad o no de una matriz** mejor que con `np.isclose()`  
>       * **Rango** de la matriz: el número de filas (o columnas) **linealmente independientes**  
>       * Si el rango es menor que $n$, la matriz es singular  
>       * Es **invariante a la escala**: no le afecta que las entradas sean muy grandes o muy pequeñas  
>  
> - `np.eye(n)`  
>       * Crea la **matriz identidad** $n \times n$ (unos en la diagonal principal, ceros fuera, la vamos a revisar posteriormente)  
>       * Útil como bloque base para construir matrices de prueba  
>       * Es la prima-hermana de `np.ones()`, `np.zeros()`, pero para diagonales **llenando de uno's**
  

    
Y, ahora, volvamos al asunto de los determinantes "tan cercanos a cero":

- Primero, volvamos a definir qué es una matriz singular:  

    - **Aquella donde alguna de sus filas (contraintuitivamente NO tiene por qué ser la última) es una COMBINACIÓN LINEAL de las demás**


> [!WARNING]
> El valor del determinante **depende de la escala de la matriz**:  
>   - Una matriz puede tener un determinante diminuto y ser perfectamente invertible!  

```python
matriz_componentes_tolerancia = 1e-5 * np.eye(3)
determinante = np.linalg.det(matriz_componentes_tolerancia)

print(matriz_componentes_tolerancia)
"""
[[1.e-05 0.e+00 0.e+00]
 [0.e+00 1.e-05 0.e+00]
 [0.e+00 0.e+00 1.e-05]]
"""
print(determinante)                    # 1.0000000000000013e-15

print(np.isclose(determinante, 0))     # True ENGAÑOSO!
print(np.isclose(determinante, 0, atol=1e-15))  # False, PORQUE LE AJUSTAMOS CORRECTAMENTE LA TOLERANCIA ABOSLUTA
print(np.linalg.matrix_rank(matriz_componentes_tolerancia))  # 3  , Por lo que es invertible ergo NO es singular
```

- `np.isclose(determinante, 0)` usa un `atol=1e-8` por defecto, que aquí es **demasiado grande**: el determinante $10^{-15}$ no cabe en ese margen por defecto y da `True` aunque la matriz sea invertible.
    - **Es una comparación engañosa**

- `atol=1e-15` (o inferior) **lo arregla**: 
    - En este caso con $1 \times 10^{-15}$... **al ser igual o estar aún más por debajo que el determinante, nos hace la comparación más correcta**  
    - Es decir, ajustar la tolerancia absoluta por encima $10^{+t}$ (o debajo para $10^{-t}$) afina para que la comparación no sea engañosa
    
- `rtol=1e-5`, aunque no estamos usando la tolerancia relativa, recordamos que este ajuste, que se basa en B, permite aumentar la afinación cuando la tolerancia absoluta es demasiado "rígida".

- `np.linalg.matrix_rank(...)`, en cambio, devuelve `3`, es decir, **es rango completo**: 
    - **La matriz SI es invertible**, nos sirve para definir la singularidad, y no hemos tocado tolerancias o escalas para ello  

> [!TIP]
> Para decidir si una matriz es singular de forma más fiable, se usa su **rango**: `np.linalg.matrix_rank(M)`  
>  
>   - Si el rango es **menor que $n$**, la matriz es singular  
>   - Le da exactamente igual qué componentes tan grandes o pequeños contenga  
>   
> El rango lo estudiaremos más adelante.



**Un poco más a fondo con `matrix_rank`**, usando las matrices que ya conocemos:

```python
A = np.array([[1, 2], [3, 4]])
P = np.array([[2, 0, 1], [1, 3, 2], [1, 1, 4]])
S = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U = np.array([[2, 1, 3], [0, 4, 1], [0, 0, 5]])

print(np.linalg.matrix_rank(A))   # 2  2 = 2,   2 filas independientes, invertible
print(np.linalg.matrix_rank(P))   # 3  3 = 3,   3 filas independientes, invertible
print(np.linalg.matrix_rank(S))   # 2  2 < 3    Es singular! (la 3ª fila es combinación de las otras)
print(np.linalg.matrix_rank(U))   # 3  3 = 2    3 filas independientes, invertible
```

- $A$ es $2 \times 2$ y su rango es $2 = n$: invertible.
- $P$ es $3 \times 3$ y su rango es $3 = n$: invertible (de hecho, $\det(P) = 18$).
- $S$ es $3 \times 3$ y su rango es $2 < 3$: **singular**, coherente con $\det(S) = 0$.
- $U$ es triangular principsl superior con diagonal no nula; su rango es $3 = n$: invertible.



---


[PENDIENTE, Ejercicios Determinante
- Después Traza ]
