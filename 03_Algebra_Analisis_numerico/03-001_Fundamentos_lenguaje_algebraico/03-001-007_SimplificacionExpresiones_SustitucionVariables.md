# 03-001:   Fundamentos del lenguaje algebraico

## 1.7. Simplificación de expresiones y sustitución de variables

Vamos a cerrar los fundamentos algebraicos con dos operaciones que utilizarás constantemente: **simplificar expresiones** y **sustituir variables por valores**.  

### 1.7.1.  A. Simplificación de expresiones

**Simplificar** consiste en expresar una fórmula de manera más sencilla **sin cambiar su valor**.  

Una regla fundamental es que podemos sumar o restar **términos semejantes**: aquellos que tienen las mismas variables elevadas a los mismos exponentes.  

Por ejemplo:  

$$
3x + 5x = 8x
$$

- Ambos términos contienen $x$ con exponente $1$; solo sumamos sus coeficientes.

En cambio:  

$$
3x + 5x^2
$$

- No se puede reducir a $8x^3$ ni a $8x^2$. Los términos **no son semejantes**: tienen exponentes distintos.
  
Otros ejemplos:  

$$
\begin{aligned}
7a - 2a + 4 &= 5a + 4 \\
3x^2 + 2x - x^2 &= 2x^2 + 2x \\
2(a + 3) &= 2a + 6
\end{aligned}
$$

En la última expresión aplicamos la **propiedad distributiva**: el factor exterior multiplica a cada término del paréntesis.  

$$
a(b + c) = ab + ac
$$

> [!WARNING]
> La suma y la multiplicación no funcionan igual con los exponentes:
> $x^2 + x^2 = 2x^2$, pero $x^2 \cdot x^2 = x^4$.
>
> En la suma se combinan coeficientes; en la multiplicación de potencias con la misma base se **suman exponentes**.

### 1.7.2.  B. Sustitución de variables

**Sustituir** significa reemplazar una variable por un valor y calcular la expresión resultante.  

Considera:  

$$
f(x) = 2x^2 + 3x - 1
$$

Si $x = 2$, sustituimos todas las apariciones de $x$:  

$$
\begin{aligned}
f(2) &= 2 \cdot 2^2 + 3 \cdot 2 - 1 \\
&= 2 \cdot 4 + 6 - 1 \\
&= 13
\end{aligned}
$$

> [!NOTE]
> La notación $f(2)$ significa «el valor de la función $f$ cuando su entrada es 2». Más adelante estudiaremos formalmente las funciones.

Con varias variables, el procedimiento es el mismo. Para:  

$$
g(x, y) = 3x + 2y
$$

si $x = 4$ e $y = 5$:

$$
g(4, 5) = 3 \cdot 4 + 2 \cdot 5 = 22
$$

### 1.7.3.  C. Relación con Python y el análisis de datos

```python
x = 2

expresion = 2 * x**2 + 3 * x - 1

print(expresion)  # 13
```

> [!NOTE]
> **Simplificar** una fórmula matemáticamente puede hacerla más legible, pero **no siempre implica que el programa vaya a ejecutarse más rápido**. Son cuestiones distintas.

> [!IMPORTANT]
> En pandas, sustituir valores de una columna por una expresión calculada es una operación habitual.

```python
datos["importe"] = datos["precio"] * datos["unidades"]
```

Aquí se calcula el producto de los valores correspondientes de ambas columnas. Más adelante veremos cómo se relaciona con las operaciones vectorizadas.  
