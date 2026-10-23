# Ejercicio 1. Dimensiones

Crea una matriz con los valores [[1, 2], [3, 4], [5, 6]]. Indica su shape, ndim y size, y explica qué representa cada resultado.

---

# Ejercicio 2. Indexación

Con la misma matriz, obtén el valor 4, la primera fila y la segunda columna.

---

# Ejercicio 3. Interpretación

Si una matriz tiene shape == (4, 3), ¿cuántas filas, columnas y elementos contiene?

---


# Ejercicio 4. Operaciones elemento a elemento

Crea las matrices `A = [[1, 2], [3, 4]]` y `B = [[5, 6], [7, 8]]`. Calcula `A + B`, `A - B` y `A * B`.

---

# Ejercicio 5. Escalar

Calcula `A * 3`. Explica qué ocurre con cada elemento.

---

# Ejercicio 6. Multiplicación matricial

Calcula `A @ B`. Comprueba el resultado manualmente para la primera fila y explica por qué el resultado tiene forma `(2, 2)`.

---

# Ejercicio 7. Traspuestas I

Crea una matriz de forma `(2, 3)` con los valores `[[1, 2, 3], [4, 5, 6]]`. Calcula su traspuesta e indica su `shape`.

---

# Ejercicio 8. Traspuesta II

Crea una matriz cuadrada de `3 × 3`, calcula su traspuesta y comprueba qué ocurre con los elementos de la diagonal principal.

---

# Ejercicio 9.  Traspuesta III

Explica brevemente la diferencia entre `A.T` y `A * A`, utilizando una matriz NumPy de ejemplo.

---


# Ejercicio 10. Determinante I
Calcula manualmente el determinante de:

$$
A=\begin{pmatrix}
2 & 3 \\
1 & 4
\end{pmatrix}
 $$

---

# Ejercicio 11. Determinante II

Calcula el mismo determinante con `np.linalg.det(A)`. 
Compara el resultado con el cálculo manual.

---

# Ejercicio 12. Determinante  III

Calcula el determinante de:

$$
B=\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}
$$

- Indica qué resultado obtienes y qué implica respecto a la existencia de su matriz inversa

---


# Ejercicio 13. Determinante $2 \times 2$

Calcula a mano el determinante de $\begin{pmatrix} 3 & 1 \\ 2 & 5 \end{pmatrix}$.


---

# Ejercicio 14. Determinante - Tiene inversa?

Sin usar NumPy, ¿es invertible $\begin{pmatrix} 2 & 4 \\ 1 & 2 \end{pmatrix}$? 
Justifica con su determinante.

---

# Ejercicio 15. Sarrus

Calcula con la regla de Sarrus el determinante de $\begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 0 \\ 3 & 0 & 1 \end{pmatrix}$.

---

# Ejercicio 16. Propiedades de las determinantes

Si $A$ es una matriz $3 \times 3$ con $\det(A) = 5$, ¿cuánto vale $\det(2A)$?

---

# Ejercicio 17. Determinantes -  NumPy, tipos según método

Si `d = np.linalg.det(A)` devuelve `-2.0000000000000004`
    - ¿Por qué `d == -2` da `False`? 
    - ¿Qué debes usar en su lugar?