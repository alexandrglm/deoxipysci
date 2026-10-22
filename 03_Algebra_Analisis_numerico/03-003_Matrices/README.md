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

[PENDING]
- DETERMINANTE DE UNA MATRIZ