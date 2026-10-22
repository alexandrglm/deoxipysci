# 03-003:   Matrices

***

## 3.3.   Traspuesta de una matriz (Trasposición de series)

La **traspuesta** de una matriz **intercambia sus filas por columnas**.  

- **Intercambia sus ejes, no toca las componentes de ninguna manera**
- Se representa como $A^T$

Por ejemplo, si tenemos una matriz de 2 filas y 3 columnas:

$$
A =
\begin{pmatrix}
\boxed{1} & \boxed{2} & \boxed{3} \\
\mathbf{4} & \mathbf{5} & \mathbf{6}
\end{pmatrix}
$$

Su traspuesta será:  

$$
A^T =
\begin{pmatrix}
\boxed{1} & \mathbf{4} \\
\boxed{2} & \mathbf{5} \\
\boxed{3} & \mathbf{6}
\end{pmatrix}
$$


```text
A (2×3)                    Aᵀ (3×2)

[1  2  3]  ← fila 0        [1  4]
[4  5  6]  ← fila 1   ──▶  [2  5]
                           [3  6]
                            ↑   ↑
                       col 0   col 1
```


- La **fila 0** de $A$ `[1, 2, 3]` pasa a ser la **columna 0** de $A^T$  
- La **fila 1** de $A$ `[4, 5, 6]` pasa a ser la **columna 1** de $A^T$  

Elemento a elemento, componente a componente, **los dos índices se intercambian**:  

$$
(A^T)_{ij} = a_{ji}
\qquad
\begin{cases}
i = \text{fila} \\
j = \text{columna}
\end{cases}
$$

Por ejemplo, el elemento de la fila 0 y columna 2 de $A$ (un `3`) acaba en la fila 2 y columna 0 de $A^T$.

$$
A =
\begin{pmatrix}
\boxed{1} & \boxed{2} & \boxed{3} \\
4 & 5 & 6
\end{pmatrix}
\qquad\Longrightarrow\qquad
A^T =
\begin{pmatrix}
\boxed{1} & 4 \\
\boxed{2} & 5 \\
\boxed{3} & 6
\end{pmatrix}
$$

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
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

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
> Aunque, contraintuitivamente, parece que la propiedad de diagonal principal no vaya a cumplirse en matrices que NO son ~~simétricas~~ cuadradas, en realidad:    
>   1. **Siempre va a existir una diagonal principal en cualquier tipo de matriz** sean o no ~~simétricas~~  
>   2. En consecencia, **siempre va a poder comprobarse la diagonal en la traspuesta frente a su original**  

> [!TIP]
> Para no confundir términos, una matriz cuadrada y una matriz simétrica **no son lo mismo**:  
>   - Una matriz cuadrada es aquella de tipo $(n , n)$, mismo número componentes en filas que columnas, independienteme del valor de estas  
>   - Una matriz simétrica es aquella que es idéntica a su traspuesta, $(A = A^T)$ y que, por ende, es cuadrada  


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
> La regla es: $(A^T)_{ij} = A_{ji}$  
>  
>   - Los elementos de la diagonal principal **no se desplazan**: mantienen sus posiciones y valores
>   - Los elementos fuera de la diagonal **intercambian sus posiciones de forma simétrica**:
>       * Por ejemplo, el $4$ que estaba en `A[1, 0]` pasa a `A.T[0, 1]`
>       * Y el $2$ que estaba en `A[0, 1]` pasa a `A.T[1, 0]`

---



### 3.3.2    Traspuesta en NumPy

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
>   - Únicamente **intercambia los ejes** de filas y columnas

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
> `matriz.T` / `np.transpose(matriz)` **NO crean una copia en memoria**:  
>   - Solo hace una **vista "preliminar"** de los mismos datos con los ejes intercambiados  
>   - No duplican los datos. Solo devuelven una **vista (*view*)**  
>   - Es decir, el mismo bloque de datos original pero "visto desde otro ángulo" con los ejes intercambiados ( lo que, en mgrandes modelos de datos, ahorra muchísima memoria)  
>   
>  Como comparten memoria, **si modificas un valor en `matriz.T`, se modifica automáticamente en la matriz inicial.**   
> 
>  **Para romper esa conexión, obtener una copia independiente en nueva variable, se utiliza el método .copy()**:  
>   - `matriz.T.copy()`  
>   - `np.transpose(matriz).copy()` 


#### 3.3.2.3    Refresh de Vector a Matriz - .reshape(x, y)

> [!WARNING]
> En un **array de un solo eje** (un vector 1D como `[1, 2, 3]`), `.T` **no hará nada**:  
>   * Porque un array 1D **solo tiene una dimensión (un eje)**.  

No hay "filas" ni "columnas", solo una secuencia plana de números. Trasponer una línea recta la deja exactamente igual. Su forma sigue siendo `(3,)`.  

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
> `.reshape()`, como `.T`,  también funciona en modo Vista ... **siempre que no haya otra opción que crear un nuevo objeto!**:  

> [!TIP]
> La regla para entender como funcionará un `.reshape()`:  
>   1. **Te da la nueva matriz en modo Vista... siempre que se pueda**
>   2. **Te hace una copia de la matriz si no queda otra**
  

* 1. **Por defecto (La mayoría de las veces es una VISTA):**  
    - Si el array está ordenado de forma contigua en la memoria (como un array recién creado), `.reshape()` **no duplica los datos**. Te devuelve una **vista** con otra forma, lo que significa que **comparte memoria** y modificar un valor puede afectar al original.  

* 2. **La trampa (A veces se convierte en una COPIA):**   
    - Si el array original no es contiguo en memoria (por ejemplo, porque viene de hacerle un corte o una trasposición previa no contigua), NumPy **necesita copiar los datos a un nuevo espacio de memoria** para poder darle la nueva forma y ... en ese caso, `.reshape()` devuelve una **copia independiente**.  

* 3. **Ante la duda, `np.shares_memory()`:**  
    - NumPy tiene una función propia llamada **`np.shares_memory()`** para salir de dudas al instante.

* 4. **... y ante la necesidad, `.copy()`:**  
    - Si es necesario hacer que el `.reshape()` sea un objeto totalmente independiente en memoria y no vaya a alterar el original bajo ninguna circunstancia, volvemos a usar el conocido legacy `.copy()`.

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
print(np.shares_memory(a, A_reshape_independiente)) # False -> Nuevo objeto copiado
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

1.  **Cambiar la orientación de los datos:** 
    - Pasar de datos organizados por filas a organizados por columnas, y al revés.

2.  **Hacer compatibles las formas** en una multiplicación matricial

3.  **En álgebra lineal y ML:** 
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

