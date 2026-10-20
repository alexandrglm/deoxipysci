# 03-002:   Vectores

***

## 2.5. Producto escalar de vectores

El **producto escalar** es una operación que toma **dos vectores** y devuelve **un único número** (un escalar).  

Es una operación fundamental en álgebra lineal y aparece en análisis de datos, aprendizaje automático, geometría y cálculo de similitud.  

***

### 2.5.1. Fórmula matemática

Dados dos vectores de la **misma longitud**:  

$$
\mathbf{u} = (u_1, u_2, \ldots, u_n)
$$

$$
\mathbf{v} = (v_1, v_2, \ldots, v_n)
$$

Su producto escalar se calcula **multiplicando las componentes que ocupan la misma posición** y **sumando los resultados**:  

$$
\boxed{\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^{n} u_i v_i}
$$

Por ejemplo, con $\mathbf{u} = (2, 3)$ y $\mathbf{v} = (4, 5)$:  

$$
\begin{aligned}
\mathbf{u} \cdot \mathbf{v} &= 2 \cdot 4 + 3 \cdot 5 \\
&= 8 + 15 \\
&= \boxed{23}
\end{aligned}
$$

El resultado es $23$, un **escalar**. **No es un vector**.  

> [!WARNING]
> No confundas el producto escalar con la suma de vectores:  
>   - La suma produce **otro vector**  
>   - El producto escalar produce **un número**  

***

### 2.5.2. Cómo calcularlo con NumPy

Vamos a utilizar dos vectores de ejemplo:  

```python
u = np.array([2, 3])
v = np.array([4, 5])
```

Hay **tres formas habituales de calcular el producto escalar** de vectores **unidimensionales**.  

- **Método 1:** `np.dot(u, v)`

```python
resultado = np.dot(u, v)

print(resultado)  # 23
```

Función de NumPy para calcular productos entre arrays. Para dos vectores 1D, calcula el producto escalar.  



- **Método 2:** `u @ v`, Multiplicación matricial

```python
resultado = u @ v

print(resultado)  # 23
```

El operador `@` representa la **multiplicación matricial**. Para dos vectores 1D, calcula el producto escalar.  



- **Método 3:** `np.sum(u * v)`

```python
resultado = np.sum(u * v)

print(resultado)  # 23
```

Primero multiplica las componentes **elemento a elemento** y después **suma** los productos.  

> [!WARNING]
> Los argumentos de `np.sum()` **deben tenerse muy claro**:  
>  
> - `np.sum(u, v)` **NO ES LO MISMO QUE** `np.sum(u * v)`  
>    * El segundo argumento posicional de `np.sum(u, v)` no representa el segundo vector; corresponde al parámetro `axis`, para matrices. No aplica a vectores unidimensionales -> producto escalar
>  
> - `np.sum(u, v)` **TAMPOCO ES EQUIVALENTE** a `u @ v`. 
>  
> Para calcular el oducto escalar, utiliza `np.sum(u * v)`, `np.dot(u, v)` o `u @ v`.  


***

### 2.5.3. ¿Qué hace exactamente cada operación?

Con `u = [2, 3]` y `v = [4, 5]`:

| Operación       | Resultado | Tipo de resultado |
| --------------- | --------- | ----------------- |
| `u * v`         | `[8, 15]` | Array, np.darray  |
| `np.sum(u * v)` | `23`      | Escalar de NumPy  |
| `np.dot(u, v)`  | `23`      | Escalar de NumPy  |
| `u @ v`         | `23`      | Escalar de NumPy  |

> [!WARNING]
> `u * v` **no** calcula por sí solo el producto escalar: genera los productos de cada pareja de componentes, pero todavía falta **sumarlos**; con un sum() legacy o np.sum() indistintamente, obtendrás un escalar de Numpy.


#### 2.5.3.1.  Problemas, requisito, cuándo procede una u otra

- **Misma longitud:** Ambos vectores deben tener el **mismo número de componentes** para calcular el producto escalar de vectores ordinarios.

- **Posiciones correspondientes:** Se multiplica la primera componente de un vector por la primera del otro, la segunda por la segunda, y así sucesivamente.

- **Resultado escalar:** Se suman todos los productos parciales.


> [!WARNING]
> **Cuidado con las dimensiones:** en NumPy, `np.dot` y `@` también admiten matrices y otros tipos de arrays:  
>   
>   - **Su comportamiento cambia según las dimensiones**  
>   - No siempre significan simplemente multiplicar y sumar todos los elementos  


> [!TIP]
> **¿Cuándo usar cada cuál?**  
>  
> 1. Para dos vectores 1D, elegiría `u @ v` si quieres expresar directamente la operación matemática  
> 2. `np.dot(u, v)` también es claro y muy habitual  
> 3. Usaría `np.sum(u * v)` cuando necesite inspeccionar o reutilizar los productos parciales  

***

### 2.5.4.  Interpretación geométrica

El producto escalar también relaciona los vectores con el **ángulo** que forman:  

$$
\boxed{\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\|_2 \, \|\mathbf{v}\|_2 \cos(\theta)}
$$

Aquí:  

- $\|\mathbf{u}\|_2$ y $\|\mathbf{v}\|_2$ son las **normas euclídeas** o longitudes de los vectores.
- $\theta$ es el **ángulo** entre ellos.
- $\cos(\theta)$ determina cómo influye la **orientación** de los vectores en el resultado.

Esto permite interpretar el **signo** del producto escalar:  

| Signo    | Ángulo                                                   |
| -------- | -------------------------------------------------------- |
| Positivo | Agudo, menor de $90^\circ$                               |
| Cero     | Perpendiculares, siempre que ambos vectores sean no nulos |
| Negativo | Obtuso, mayor de $90^\circ$                              |

> [!NOTE]
> Esta interpretación es útil más adelante para comprender la **similitud entre vectores** en aprendizaje automático.

---
