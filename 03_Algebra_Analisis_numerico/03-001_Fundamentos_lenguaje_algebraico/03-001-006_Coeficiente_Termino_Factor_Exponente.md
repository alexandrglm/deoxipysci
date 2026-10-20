# 03-001:   Fundamentos del lenguaje algebraico

***

## 1.6. Coeficiente, término, factor y exponente

Estos cuatro conceptos aparecen constantemente en álgebra, fórmulas estadísticas y operaciones numéricas.  

Tomemos como ejemplo:  

$$
3x^2 + 5x - 7
$$

- **Término:** cada parte separada por una suma o una resta, **incluyendo su signo**. Aquí tenemos $3x^2$, $5x$ y $-7$.
- **Coeficiente:** el factor numérico que multiplica a una variable. En $3x^2$, es $3$; en $5x$, es $5$.
- **Factor:** cada elemento que participa en una multiplicación. En $3x^2$, los factores son $3$ y $x^2$.
- **Exponente:** indica la potencia a la que se eleva una base. En $x^2$, el exponente es $2$.

> [!NOTE]
> Un término constante, como $-7$, no contiene variables. Si un término no muestra su coeficiente, este se sobreentiende: $x = 1x$ y $-x = -1x$.

### 1.6.1.  Otro ejemplo

En la expresión:  

$$
4ab^3
$$

- **Coeficiente numérico:** $4$.
- **Variables:** $a$ y $b$.
- **Exponente de $a$:** $1$, aunque no aparezca escrito.
- **Exponente de $b$:** $3$.
- **Factores:** $4$, $a$ y $b^3$.

La expresión equivale a:  

$$
4 \cdot a \cdot b \cdot b \cdot b
$$

### 1.6.2.  Aplicación en Python

```python
a = 2
b = 3
resultado = 4 * a * b**3

print(resultado)  # 216
```

En Python, `**` representa la potenciación. La expresión reproduce directamente la fórmula matemática.  

---
