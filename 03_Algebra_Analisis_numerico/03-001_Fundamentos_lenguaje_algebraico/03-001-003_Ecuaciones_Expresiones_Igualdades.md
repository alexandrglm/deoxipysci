# 03-001:   Fundamentos del lenguaje algebraico

***

## 1.3. Expresiones, ecuaciones e igualdades

Estos tres conceptos están relacionados, pero **no son equivalentes**.  

**Expresión algebraica:** combina números, variables y operadores.  

$$
3x + 5
$$

Por sí sola, no afirma que el resultado sea igual a un valor concreto.  

**Igualdad:** afirma que dos expresiones tienen el mismo valor.  

$$
3 + 2 = 5
$$

**Ecuación:** es una igualdad que contiene una o más incógnitas y que queremos resolver.  

$$
3x + 5 = 20
$$

Para resolverla, buscamos el valor de $x$ que hace verdadera la igualdad:  

$$
3x = 20 - 5 = 15
$$

$$
x = \frac{15}{3} = 5
$$

En Python, podemos calcular el resultado:  

```python
x = (20 - 5) / 3

print(x)  # 5.0
```

El resultado es `5.0` porque el operador `/` realiza división real y devuelve un `float`, incluso cuando el cociente es entero.  

> [!WARNING]
> En una ecuación, podemos realizar la misma operación en ambos miembros sin alterar la igualdad, siempre que la operación sea válida. Por ejemplo, podemos restar 5 a ambos lados.
>
> **No se debe confundir esa manipulación algebraica con asignar un valor a una variable** en Python.

---
