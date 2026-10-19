
# **1. Componentes y dimensión**

Dado $\mathbf{v} = (8, 2, 6, 4)$, indica cuántos componentes tiene y cuál es su tercer componente.

---

# **2. Suma**

Calcula $(2,5,7) + (1,3,4)$.

---

# **3. Multiplicación por un escalar**

Calcula $4\,(2,3,5)$.

---

# **4. NumPy**

Si `v = np.array([10, 20, 30])`, ¿qué devuelven `v.shape`, `v.ndim` y `v.size`?


---

# 5. Norma euclídea

Calcula manualmente la norma L2 de \\(\mathbf{v}=(6,8)\\). Muestra los pasos.

---

# 6. Norma L1

Calcula la norma L1 de \\(\mathbf{v}=(-2,5,-3)\\).

---

# 7. NumPy II

Escribe el código para calcular la norma euclídea del vector `[1, 2, 2]` y señala el resultado esperado.

---


# 8. Cálculo manual

Dados los vectores \\(\mathbf{u}=(3,4)\\) y \\(\mathbf{v}=(2,5)\\) :

 - Calcula su producto escalar
 - Explica brevemente las operaciones.

---

# 9. NumPy III

Dados `u = np.array([1, 2, 3])` y `v = np.array([4, 5, 6])`
 - Calcula su producto escalar usando `np.dot()` y `@`
 - ¿Obtienes el mismo resultado?


---

# 10. Comprender `u * v`

Con los vectores del ejercicio 2,
-  ¿qué devuelve `u * v`?
-  ¿Por qué ese resultado no es todavía el producto escalar?

---

# 11. Interpretación

Calcula el producto escalar de `u = np.array([1, 2])` y `v = np.array([2, 1])`. ¿Es positivo, negativo o cero? ¿Qué te indica sobre el ángulo?

---

# 12. Perpendicularidad

Comprueba mediante NumPy si `u = np.array([3, 0])` y `v = np.array([0, 4])` son perpendiculares. Justifica la respuesta a partir del producto escalar.

---

# 13. Relación con las normas

Para `u = np.array([3, 4])` y `v = np.array([4, 3])`, calcula:

- El producto escalar.
- La norma euclídea de cada vector con `np.linalg.norm()`.
- Si el producto escalar es positivo, negativo o cero.