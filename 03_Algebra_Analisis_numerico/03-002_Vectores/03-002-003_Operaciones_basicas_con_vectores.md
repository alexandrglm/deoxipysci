# 03-002:   Vectores

## 2.3. Operaciones básicas con vectores

Ahora que sabemos representar un vector, podemos operar con sus componentes. Consideremos:

$$
\mathbf{u} = (2, 4, 6), \qquad \mathbf{v} = (1, 3, 5)
$$

**Suma:** se suman las componentes que ocupan la misma posición.

$$
\mathbf{u} + \mathbf{v} = (2+1,\ 4+3,\ 6+5) = (3, 7, 11)
$$

**Resta:** se restan las componentes correspondientes.

$$
\mathbf{u} - \mathbf{v} = (2-1,\ 4-3,\ 6-5) = (1, 1, 1)
$$

**Multiplicación por un escalar:** se multiplican todas las componentes por el mismo número.

$$
3\mathbf{u} = (3 \cdot 2,\ 3 \cdot 4,\ 3 \cdot 6) = (6, 12, 18)
$$

> [!IMPORTANT]
> La suma y la resta **requieren que ambos vectores tengan el mismo número de componentes**.

En NumPy:

```python
u = np.array([2, 4, 6])
v = np.array([1, 3, 5])

print(u + v)  # [ 3  7 11]
print(u - v)  # [1 1 1]
print(3 * u)  # [ 6 12 18]
```

### 2.3.1.  Una diferencia importante: listas frente a arrays

En Python, el operador `+` aplicado a **listas concatena** sus elementos:

```python
[2, 4] + [1, 3]  # [2, 4, 1, 3]
```

En cambio, con **arrays NumPy suma componente a componente**:

```python
np.array([2, 4]) + np.array([1, 3])
# array([4, 7])
```

> [!WARNING]
> Mismo operador, resultado distinto: `+` **concatena** listas pero **suma** arrays. Esta diferencia será esencial al trabajar con cálculos numéricos y datos.

---
