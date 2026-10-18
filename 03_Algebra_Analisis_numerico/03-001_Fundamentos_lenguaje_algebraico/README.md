# 03-001:    Fundamentos del lenguaje algebraico

Empezamos por el lenguaje que utilizaremos en todo el bloque, aunque sea muy muy obvio.  

Antes de trabajar con vectores, matrices o funciones, necesitamos distinguir qué representa cada número, qué papel tiene una variable y cómo se construyen las expresiones matemáticas.

---

## 1.1. Números, magnitudes y escalares

***

### Número

Un número es un valor matemático. Según el conjunto al que pertenezca, puede representar cantidades enteras, fraccionarias, reales, etc.

Algunos conjuntos importantes:

| Conjunto   | Símbolo          | Ejemplos                                |
| ---------- | ---------------- | --------------------------------------- |
| Naturales  | \\(\mathbb{N}\\) | \\(0,1,2,3,\ldots\\) (según convención) |
| Enteros    | \\(\mathbb{Z}\\) | \\(-3,-2,-1,0,1,\ldots\\)               |
| Racionales | \\(\mathbb{Q}\\) | \\(\frac12,-\frac34,2\\)                |
| Reales     | \\(\mathbb{R}\\) | \\(\sqrt{2},\pi,-1.5\\)                 |

Estos conjuntos se relacionan entre sí: todo entero es racional, y todo racional es real. No todo número real es racional; por ejemplo, \\(\sqrt{2}\\) no puede expresarse como una fracción exacta de dos enteros.

***

### Magnitud

Una magnitud es una propiedad que se puede medir o cuantificar: longitud, masa, tiempo, temperatura, precio o distancia.

Conviene distinguir la magnitud de su valor numérico y de su unidad:

- Distancia: magnitud.
- \\(12\\): valor numérico.
- Metros: unidad.
- \\(12\ \text{m}\\): cantidad expresada con valor y unidad.

Esta distinción importa al calcular con datos: sumar 12 metros y 5 metros tiene sentido; sumar 12 metros y 5 segundos, en general, no.

***

### Escalar

Un escalar es una cantidad representada por un único valor, en contraposición a un vector o una matriz, que contienen varios componentes.

Ejemplos:

- Un precio: \\(25.50\\).
- Una temperatura: \\(21\\).
- El número de registros de una tabla: \\(500\\).
- La media de una columna: \\(18.4\\).

En Python, un escalar puede representarse mediante un `int`, un `float` o un tipo numérico de NumPy, entre otros. La representación concreta depende del tipo de dato.

> [!NOTE] 
> Un escalar no tiene por qué ser un número entero ni carecer de unidades. La característica principal es que representa un único valor.

---

## 1.2. Variables y constantes

Una variable es un símbolo cuyo valor puede cambiar o que utilizamos para representar un valor que todavía no conocemos.

Por ejemplo:

\\[ x=5 \\]

Aquí, \\(x\\) es la variable y \\(5\\) es el valor que toma en esta expresión.

Una constante es un valor que se mantiene fijo dentro del contexto matemático considerado. Por ejemplo, en:

\\[ y=2x+3 \\]

- \\(x\\): variable de entrada.
- \\(y\\): variable de salida.
- \\(2\\): coeficiente constante de \\(x\\).
- \\(3\\): término constante.

Si \\(x=4\\):

\\[ y=2\cdot4+3=11 \\]

Si \\(x=10\\):

\\[ y=2\cdot10+3=23 \\]

La expresión establece una relación entre \\(x\\) e \\(y\\).

***


### Relación con Python

```python
x = 4
y = 2 * x + 3

print(y)  # 11

En Python, `=` asigna un valor a una variable. No es una afirmación de igualdad matemática entre dos expresiones, como veremos a continuación.  

---

## 1.3. Expresiones, ecuaciones e igualdades

Estos tres conceptos están relacionados, pero no son equivalentes.

- **Expresión algebraica**: combina números, variables y operadores.

    \\[ 3x+5 \\]

    Por sí sola, no afirma que el resultado sea igual a un valor concreto.

- **Igualdad**: afirma que dos expresiones tienen el mismo valor.

    \\[ 3+2=5 \\]

- **Ecuación**: es una igualdad que contiene una o más incógnitas y que queremos resolver.

    \\[ 3x+5=20 \\]

    Para resolverla, buscamos el valor de \\(x\\) que hace verdadera la igualdad:

    \\[ 3x=20-5=15 \\]

    \\[ x=\frac{15}{3}=5 \\]

    - En Python, podemos calcular el resultado:
    ```python
    x = (20 - 5) / 3

    print(x)  # 5.0
    ```
    
    El resultado es `5.0` porque el operador `/` realiza división real y devuelve un `float`, incluso cuando el cociente es entero.

> [!WARNING] 
> En una ecuación, podemos realizar la misma operación en ambos miembros sin alterar la igualdad, siempre que la operación sea válida. Por ejemplo, podemos restar 5 a ambos lados.  
> **No se debe confundir esa manipulación algebraica con asignar un valor a una variable** en Python.

---

## 1.4. Operadores y orden de las operaciones

Las operaciones básicas son:

| Operación      | Símbolo matemático | Python    |
| -------------- | ------------------ | --------- |
| Suma           | \\(a+b\\)          | `a + b`   |
| Resta          | \\(a-b\\)          | `a - b`   |
| Multiplicación | \\(a\cdot b\\)     | `a * b`   |
| División       | \\(\frac{a}{b}\\)  | `a / b`   |
| Potencia       | \\(a^b\\)          | `a ** b`  |
| Paréntesis     | \\((a+b)\\)        | `(a + b)` |

> [!WARNING]
> En Python, `^` no representa una potencia: es el operador XOR bit a bit para enteros.  


El orden habitual de evaluación es **PEMDAS**:

Please, excuse my dear aunt Sophie
Parans, Exponents, Multiplications, Divisions, Additions, Substractions
```text
Please -> Parans ()
Excuse -> Exponents **
My -> Multiplication *
Dear -> Division /
Aunt -> Addition +
Sophie -> Subtraction -
```

1. Paréntesis.
2. Potencias.
3. Multiplicaciones y divisiones.
4. Sumas y restas.

Por ejemplo:

\\[ 2+3\cdot4=14 \\]

Pero:

\\[ (2+3)\cdot4=20 \\]

Los paréntesis cambian el orden de evaluación y, por tanto, el resultado.

---

## 1.5. Por qué importa en análisis de datos

Las fórmulas de análisis de datos son expresiones algebraicas aplicadas a conjuntos de valores.

Por ejemplo, el importe de una operación puede calcularse así:

\\[ \text{importe}=\text{precio}\cdot\text{unidades} \\]

En pandas:

```
datos["importe"] = datos["precio"] * datos["unidades"]
```

La expresión matemática es sencilla, pero el código aplica la operación a los valores correspondientes de las columnas. Más adelante veremos por qué esto se relaciona con los vectores y la vectorización.


---

## 1.6. Coeficiente, término, factor y exponente

Estos cuatro conceptos aparecen constantemente en álgebra, fórmulas estadísticas y operaciones numéricas.

Tomemos como ejemplo:

\\[ 3x^2+5x-7 \\]

- Término: cada parte separada por una suma o una resta, **incluyendo su signo**. Aquí tenemos \\(3x^2\\), \\(5x\\) y \\(-7\\).
- Coeficiente: el factor numérico que multiplica a una variable. En \\(3x^2\\), es \\(3\\); en \\(5x\\), es \\(5\\).
- Factor: cada elemento que participa en una multiplicación. En \\(3x^2\\), los factores son \\(3\\) y \\(x^2\\).
- Exponente: indica la potencia a la que se eleva una base. En \\(x^2\\), el exponente es \\(2\\).

> [!NOTE] 
> Un término constante, como \\(-7\\), no contiene variables. Si un término no muestra su coeficiente, este se sobreentiende: \\(x=1x\\) y \\(-x=-1x\\).

### Otro ejemplo

En la expresión:

\\[ 4ab^3 \\]

- Coeficiente numérico: \\(4\\).
- Variables: \\(a\\) y \\(b\\).
- Exponente de \\(a\\): \\(1\\), aunque no aparezca escrito.
- Exponente de \\(b\\): \\(3\\).
- Factores: \\(4\\), \\(a\\) y \\(b^3\\).

La expresión equivale a:

\\[ 4\cdot a\cdot b\cdot b\cdot b \\]

### Aplicación en Python

```python
a = 2b = 3
resultado = 4 * a * b**3

print(resultado)  # 216
```

En Python, `**` representa la potenciación. La expresión reproduce directamente la fórmula matemática.

---

## 1.7. Simplificación de expresiones y sustitución de variables

Vamos a cerrar los fundamentos algebraicos con dos operaciones que utilizarás constantemente: **simplificar expresiones** y **sustituir variables por valores**.

### A. Simplificación de expresiones

Simplificar consiste en **expresar una fórmula de manera más sencilla sin cambiar su valor**.  

Una regla fundamental es que podemos sumar o restar términos semejantes: aquellos que tienen las mismas variables elevadas a los mismos exponentes.  

Por ejemplo:  

\\[ 3x+5x=8x \\]

- Ambos términos contienen \\(x\\) con exponente \\(1\\); solo sumamos sus coeficientes.

En cambio:

\\[ 3x+5x^2 \\]

- No se puede reducir a \\(8x^3\\) ni a \\(8x^2\\). Los términos no son semejantes: tienen exponentes distintos.

Otros ejemplos:  

\\[ \begin{aligned} 7a-2a+4 &= 5a+4\\\ 3x^2+2x-x^2 &= 2x^2+2x\\\ 2(a+3) &= 2a+6 \end{aligned} \\]

En la última expresión aplicamos la **propiedad distributiva**: el factor exterior multiplica a cada término del paréntesis.

\\[ a(b+c)=ab+ac \\]

> [!WARNING]
> La suma y la multiplicación no funcionan igual con los exponentes: 
>  \\(x^2+x^2=2x^2\\), pero \\(x^2\cdot x^2=x^4\\)  
>  
>  En la suma se combinan coeficientes; en la multiplicación de potencias con la misma base se suman exponentes.

  
### B. Sustitución de variables

Sustituir significa **reemplazar una variable por un valor y calcular la expresión resultante**.  

Considera:  

\\[ f(x)=2x^2+3x-1 \\]

- Si \\(x=2\\), sustituimos todas las apariciones de \\(x\\):  

\\[ \begin{aligned} f(2)&=2\cdot2^2+3\cdot2-1\\\ &=2\cdot4+6-1\\\ &=13 \end{aligned} \\]  

- La notación \\(f(2)\\) significa «el valor de la función \\(f\\) cuando su entrada es 2». Más adelante estudiaremos formalmente las funciones.  
  

Con varias variables, el procedimiento es el mismo. Para:

\\[ g(x,y)=3x+2y \\]

- si \\(x=4\\) e \\(y=5\\):

\\[ g(4,5)=3\cdot4+2\cdot5=22 \\]
  
  
### C. Relación con Python y el análisis de datos

```python
x = 2

expresion = 2 * x**2 + 3 * x - 1

print(expresion)  # 13
```

> [!NOTE]
> **Simplificar** una fórmula matemáticamente puede hacerla más legible, pero **no siempre implica que el programa vaya a ejecutarse más rápido**. Son cuestiones distintas.


> [!IMPORTANT]
> En pandas, sustituir valores de una columna por una expresión calculada es una operación habitual:

```python
datos["importe"] = datos["precio"] * datos["unidades"]
```

Aquí se calcula el producto de los valores correspondientes de ambas columnas. Más adelante veremos cómo se relaciona con las operaciones vectorizadas.


