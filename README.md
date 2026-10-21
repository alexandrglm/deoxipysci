
## Idea de temariop

### Bloque 1. Fundamentos y entorno

- **1.1** Presentación de la formación y objetivos
- **1.2** Entorno de trabajo: Python, NumPy, Jupyter/scripts
- **1.3** Repaso de Python esencial para cálculo numérico
  - Listas, arrays, bucles, funciones, tipos numéricos.
- **1.4** Introducción a NumPy
  - `np.array`, `dtype`, `shape`, `ndim`, `size`, broadcasting básico.
- **1.5** Buenas prácticas y depuración
  - Lectura de errores, `nan`, `inf`, comparaciones con tolerancia (`np.isclose`).

---

### Bloque 2. Álgebra lineal:   VECTORES

- **2.1** ¿Qué es un vector?
  - Interpretación geométrica y como lista de datos.

- **2.2** Creación y representación en NumPy
  - Vectores 1D, `shape`, `dtype`.

- **2.3** Operaciones básicas con vectores
  - Suma, resta, multiplicación por escalar.

- **2.4** Normas vectoriales
  - L1 (`ord=1`), L2 (`ord=2`), L∞ (`ord=np.inf`); cálculo manual vs. `np.linalg.norm`.

- **2.5** Producto escalar
  - `u @ v`, `np.dot`, `np.sum(u * v)`; propiedades; interpretación geométrica.

- **2.6** Relación entre producto escalar, norma y ángulo
  - Coseno del ángulo, `np.arccos`, `np.clip`; ángulo agudo/recto/obtuso; signo del producto escalar.

- **2.7** Similitud del coseno
  - Fórmula, rango [−1,1], interpretación, caso del vector cero, aplicaciones en datos.

---

### Bloque 3. Álgebra lineal:   MATRICES

- **3.1** Introducción al bloque de matrices (contexto)

- **3.2** Vectores (bloque ya trabajado; referencia de cierre)

- **3.3** Matrices
  - **3.3.1** ¿Qué es una matriz? `shape`, `ndim`, `size`.
  - **3.3.2** Acceso a filas, columnas y elementos (indexación).
  - **3.3.3** Operaciones básicas: elemento a elemento (Producto de Hadamard), escalar, multiplicación matricial (`@`, Esquema de Falk) y compatibilidad.
  - **3.3.4** Transpuesta y matrices simétricas.
  - **3.3.5** Determinante, traza y rango.
  - **3.3.6** Matriz inversa y matrices singulares.
  - **3.3.7** Sistemas de ecuaciones lineales (`np.linalg.solve`, `lstsq`).

- **3.4** Operaciones avanzadas con matrices
  - Producto de Kronecker, particionado, broadcasting avanzado.

- **3.5** Autovalores y autovectores
  - `np.linalg.eig`, diagonalización, interpretación geométrica.

- **3.6** Descomposiciones matriciales
  - SVD (`np.linalg.svd`), LU, QR; aplicaciones.

- **3.7** Aplicaciones en datos
  - PCA, regresión lineal, similitud, reducción de dimensionalidad.

---

### Bloque 4. Cálculo diferencial e integral

- **4.1** Funciones y límites

- **4.2** Derivadas
  - Reglas básicas, derivadas parciales, gradiente.

- **4.3** Optimización
  - Mínimos/máximos, descenso de gradiente.

- **4.4** Integrales
  - Integral definida, aproximación numérica.

- **4.5** Aplicaciones en datos
  - Funciones de pérdida, ajuste de modelos.

---

### Bloque 5. Probabilidad y estadística

- **5.1** Variables aleatorias y distribuciones

- **5.2** Medidas de tendencia central y dispersión

- **5.3** Distribuciones comunes (normal, uniforme, binomial)

- **5.4** Correlación y covarianza

- **5.5** Inferencia básica
  - Muestreo, intervalos de confianza, contraste de hipótesis.

- **5.6** Aplicaciones en datos
  - Análisis exploratorio, simulación.

---

### Bloque 6. Puente a Machine Learning, Aplicaciones integradas y proyectos

- **6.1** Análisis de datos con álgebra lineal

- **6.2** Modelos básicos de machine learning desde cero

- **6.3** Proyecto integrador
  - Dataset real, pipeline completo: *limpieza, transformación, modelo, evaluación*

- **6.4** Repaso y consolidación

---