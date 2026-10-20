# 03-001:   Fundamentos del lenguaje algebraico

***

## 1.2. Variables y constantes

Una **variable** es un símbolo cuyo valor puede cambiar o que utilizamos para representar un valor que todavía no conocemos.  

Por ejemplo:  

$$
x = 5
$$

Aquí, $x$ es la variable y $5$ es el valor que toma en esta expresión.  

Una **constante** es un valor que se mantiene fijo dentro del contexto matemático considerado. Por ejemplo, en:  
  
$$
y = 2x + 3
$$

- $x$: variable de entrada.
- $y$: variable de salida.
- $2$: coeficiente constante de $x$.
- $3$: término constante.

Si $x = 4$:  

$$
y = 2 \cdot 4 + 3 = 11
$$

Si $x = 10$:  

$$
y = 2 \cdot 10 + 3 = 23
$$

La expresión establece una **relación** entre $x$ e $y$.  

***

### 1.2.1.  Relación con Python

```python
x = 4
y = 2 * x + 3

print(y)  # 11
```

> [!WARNING]
> En Python, `=` **asigna** un valor a una variable. No es una afirmación de igualdad matemática entre dos expresiones, como veremos a continuación.

---
