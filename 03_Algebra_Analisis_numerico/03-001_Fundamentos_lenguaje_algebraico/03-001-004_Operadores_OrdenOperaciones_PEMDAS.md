# 03-001:   Fundamentos del lenguaje algebraico

***

## 1.4. Operadores y orden de las operaciones

Las operaciones básicas son:  

| Operación      | Símbolo matemático | Python    |
| -------------- | ------------------ | --------- |
| Suma           | $a + b$            | `a + b`   |
| Resta          | $a - b$            | `a - b`   |
| Multiplicación | $a \cdot b$        | `a * b`   |
| División       | $\frac{a}{b}$      | `a / b`   |
| Potencia       | $a^b$              | `a ** b`  |
| Paréntesis     | $(a + b)$          | `(a + b)` |

> [!WARNING]
> En Python, `^` **no** representa una potencia: es el operador XOR bit a bit para enteros.  

El orden habitual de evaluación se recuerda con la regla **PEMDAS**:  

> *Please Excuse My Dear Aunt Sally*

```text
Please -> Parentheses     ()
Excuse -> Exponents       **
My     -> Multiplication  *
Dear   -> Division        /
Aunt   -> Addition        +
Sally  -> Subtraction     -
```

1. **Paréntesis.**
2. **Potencias.**
3. **Multiplicaciones y divisiones.**
4. **Sumas y restas.**

> [!NOTE]
> Multiplicación y división tienen la **misma prioridad** y se evalúan de izquierda a derecha. Lo mismo ocurre con suma y resta.

Por ejemplo:  

$$
2 + 3 \cdot 4 = 14
$$

Pero:  

$$
(2 + 3) \cdot 4 = 20
$$

Los paréntesis cambian el orden de evaluación y, por tanto, el resultado.  

---
