# 03-003: Matrices

***

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
\begin{aligned}
C &= AB \\[4pt]
c_{ij} &= \sum_{k=1}^{n} a_{ik} \, b_{kj} \\[4pt]
&= a_{i1} b_{1j} + a_{i2} b_{2j} + \cdots + a_{in} b_{nj}
\end{aligned}
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

Cuando $A$ tiene 2 columnas y $B$ tiene 2 filas, la fórmula general se particulariza a **dos producto** (dos productos por celda):  

$$
\begin{aligned}
c_{ij} &= \sum_{k=1}^{n} a_{ik} \, b_{kj} \\
C[i, j] &= A[i, 0] \cdot B[0, j] + A[i, 1] \cdot B[1, j]
\end{aligned}
$$

- Los dos productos de una celda comparten la **misma $i$** (fila de $A$) y la **misma $j$** (columna de $B$).
- Lo único que cambia entre ellos es el **índice del medio**, `0` y `1` (que en la fórmula general es $k$).

> [!TIP]
> En notación de índices de Python, $C[i, j] = c_{ij}$, con índices desde $0$. Es la misma fórmula de arriba, escrita con corchetes en vez de subíndices.


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

$$
(m, \underbrace{n}_{2}) \ @ \ (\underbrace{n}_{2}, p) \ = \ (m, p)
\qquad\Longrightarrow\qquad
(3, \underbrace{2}) \ @ \ (\underbrace{2}, 3) \ = \ (3, 3)
$$

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
C[1, 2] =
\underbrace{(3, 4)}_{\text{fila 1 de } A}
\cdot
\underbrace{(30, 60)}_{\text{columna 2 de } B}
= 3 \cdot 30 + 4 \cdot 60 = 90 + 240 = \boxed{330}
$$

![Esquema de Falk para C[1, 2] = 3*30 + 4*60 = 330](./img/03-003_multiplicacion.png)


##### 3.2.3.5.1  Las nueve celdas

$$
C = AB =
\begin{pmatrix}
90 & 120 & 150 \\
190 & 260 & 330 \\
290 & 400 & 510
\end{pmatrix}
$$


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
> **El orden importa.**  
> Con las mismas matrices, `B @ A` sí es posible, pero es **otra operación** y da una matriz de **forma distinta**:

```python
print((A @ B).shape)  # (3, 3)
print((B @ A).shape)  # (2, 2)

print(B @ A)

"""
[[220 280]
 [490 640]]
"""
```

- En general, la multiplicación matricial **no es conmutativa**: 
    * `A @ B` y `B @ A` pueden dar resultados distintos, o incluso uno de ellos no existir.

> [!TIP]
> Comprueba siempre las formas con `.shape` antes de multiplicar. Es la forma más rápida de encontrar un error de compatibilidad.
