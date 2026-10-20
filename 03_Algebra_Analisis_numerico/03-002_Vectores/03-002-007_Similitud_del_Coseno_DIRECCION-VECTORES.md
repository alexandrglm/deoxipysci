# 03-002:   Vectores

## 2.7. Similitud del coseno (cosine similarity)

Este concepto es una **aplicación directa** de lo que acabas de aprender.  

- Se utiliza en aprendizaje automático para **comparar vectores**, por ejemplo, representaciones numéricas de textos, documentos o productos.

---

### 2.7.1. Fórmula

La **similitud del coseno** se define como:  

$$
\boxed{
\operatorname{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \, \|\mathbf{v}\|_2}
}
$$

Observa que es **exactamente la expresión** que ya has calculado para obtener `coseno_theta` anteriormente. Por tanto:  

$$
\operatorname{sim}(\mathbf{u}, \mathbf{v}) = \cos(\theta)
$$

> [!IMPORTANT]
> La similitud del coseno mide la **orientación relativa** entre dos vectores, **SIN TENER EN CUENTA SUS MAGNITUDES**:  
>  
> - Compara hacia dónde apuntan, no cuánto miden

***

### 2.7.2. Interpretación

Para vectores no nulos, el resultado está entre $-1$ y $1$:  

| Similitud | Ángulo $\theta$ | Interpretación geométrica |
| --------- | --------------- | ------------------------- |
| `1`       | $0^\circ$       | **Misma dirección**       |
| `0`       | $90^\circ$      | **Vectores perpendiculares/ortogonales** |
| `-1`      | $180^\circ$     | **Direcciones opuestas**  |

```text
 -1                       0                       +1
  ├───────────────────────┼───────────────────────┤
OPUESTOS            PERPENDICULARES          MISMA DIRECCION
```

- Un resultado **próximo a 1** indica que las direcciones son parecidas  
- **Próximo a 0**, que son ortogonales
- Si es **próximo a -1**, que apuntan en direcciones opuestas

> [!IMPORTANT]
> Una similitud de $1$ **no** significa que los vectores tengan las mismas componentes.  
>  
>  Por ejemplo, $(1, 2)$ y $(2, 4)$ tienen similitud $1$ porque apuntan en la misma dirección, aunque sus magnitudes sean diferentes.

***

### 2.7.3.  Implementación en NumPy

Puedes calcularla reutilizando los conceptos anteriores:  

```python
u = np.array([1, 2])
v = np.array([2, 4])

coseno_theta_es_similitud_del_coseno = (
    np.dot(u, v)
    / (np.linalg.norm(u) * np.linalg.norm(v))
)

print(coseno_theta_es_similitud_del_coseno)  # 0.9999999999999998  (≈ 1.0)
```

No existe aquí una nueva operación matemática: estás combinando el **producto escalar** con las **normas euclídeas**.  

> [!WARNING]
> El resultado es `0.9999999999999998` y no exactamente `1.0` por errores de redondeo de los `float`. No compares con `==`: usa `np.isclose(similitud, 1)`.

> [!WARNING]
> Si uno de los vectores es el **vector cero**, el denominador es cero y la similitud del coseno **no está definida**.  
> **Una implementación real debe contemplar ese caso**.

##### Nuevos métodos a tener en cuenta

> [!NOTE]
> `np.asarray( [x, y,... n])`, permite pasar valores lista [x, y, ...n] a Arrays de NumPy, perfecto para crear arrays rápidamente.


> [!NOTE]
> `np.clip`, usado aquí, evita que el redondeo produzca valores fuera de $[-1, 1]$, que romperían una posterior medición del ángulo con `np.arccos`.

---

### 2.7.4. Aplicación: comparar documentos

Cada documento se convierte en un vector contando cuántas veces aparece cada palabra del vocabulario:  

| Documento | Texto               | `gato` | `perro` | `python` | `código` |
| --------- | ------------------- | ------ | ------- | -------- | -------- |
| A         | "gato perro gato"   | 2      | 1       | 0        | 0        |
| B         | A repetido dos veces | 4      | 2       | 0        | 0        |
| C         | "python código..."  | 0      | 0       | 3        | 2        |
| D         | mezcla              | 1      | 1       | 1        | 0        |

```python
A = np.array([2, 1, 0, 0])
B = np.array([4, 2, 0, 0])
C = np.array([0, 0, 3, 2])
D = np.array([1, 1, 1, 0])
```

| Comparación | Similitud | Lectura                                         |
| ----------- | --------- | ----------------------------------------------- |
| A y B       | $\approx 1$     | Mismo tema, aunque B sea el doble de largo |
| A y C       | $0$             | Ningún tema en común                       |
| A y D       | $\approx 0.77$  | Comparten parte del vocabulario            |

> [!IMPORTANT]
> Esta es la gran ventaja de la similitud del coseno: **un documento largo y uno corto sobre el mismo tema** salen muy parecidos, porque solo importa la **dirección** del vector y no su magnitud.  
>  
> Con la distancia euclídea, A y B quedarían lejos.  

> [!NOTE]
> Como los recuentos de palabras son **no negativos**, en este tipo de datos la similitud siempre queda entre $0$ y $1$.  
>  
> Se habla también de **distancia del coseno**: 
>    - $1 - \operatorname{sim}(\mathbf{u}, \mathbf{v})$.
