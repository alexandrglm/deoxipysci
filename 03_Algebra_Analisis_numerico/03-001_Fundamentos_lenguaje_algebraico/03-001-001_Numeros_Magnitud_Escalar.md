# 03-001:   Fundamentos del lenguaje algebraico

Empezamos por el lenguaje que utilizaremos en todo el bloque, aunque sea muy, muy obvio.  

Antes de trabajar con vectores, matrices o funciones, necesitamos distinguir **qué representa cada número**, **qué papel tiene una variable** y **cómo se construyen las expresiones matemáticas**.  

---

## 1.1. Números, magnitudes y escalares

***

### 1.1.1   Número

Un **número** es un valor matemático. Según el conjunto al que pertenezca, puede representar cantidades enteras, fraccionarias, reales, etc.  

Algunos conjuntos importantes:  

| Conjunto   | Símbolo        | Ejemplos                            |
| ---------- | -------------- | ----------------------------------- |
| Naturales  | $\mathbb{N}$   | $0, 1, 2, 3, \ldots$ (según convención) |
| Enteros    | $\mathbb{Z}$   | $-3, -2, -1, 0, 1, \ldots$          |
| Racionales | $\mathbb{Q}$   | $\frac{1}{2}, -\frac{3}{4}, 2$      |
| Reales     | $\mathbb{R}$   | $\sqrt{2}, \pi, -1.5$               |

Estos conjuntos se relacionan entre sí: **todo entero es racional, y todo racional es real**. No todo número real es racional; por ejemplo, $\sqrt{2}$ no puede expresarse como una fracción exacta de dos enteros.  

***

### 1.1.2.  Magnitud

Una **magnitud** es una propiedad que se puede medir o cuantificar: longitud, masa, tiempo, temperatura, precio o distancia.  

Conviene distinguir la magnitud de su valor numérico y de su unidad:  

- **Distancia:** magnitud.
- $12$: valor numérico.
- **Metros:** unidad.
- $12\ \text{m}$: cantidad expresada con valor y unidad.

> [!IMPORTANT]
> Esta distinción importa al calcular con datos: sumar 12 metros y 5 metros tiene sentido; sumar 12 metros y 5 segundos, en general, no.

***

### 1.1.3.  Escalar

Un **escalar** es una cantidad representada por **un único valor**, en contraposición a un vector o una matriz, que contienen varias componentes.  

Ejemplos:

- Un precio: $25.50$.  
- Una temperatura: $21$.  
- El número de registros de una tabla: $500$.  
- La media de una columna: $18.4$.  

En Python, un escalar puede representarse mediante un `int`, un `float` o un tipo numérico de NumPy, entre otros. La representación concreta depende del tipo de dato.  

> [!NOTE]
> Un escalar no tiene por qué ser un número entero ni carecer de unidades. La característica principal es que representa **un único valor**.

---
