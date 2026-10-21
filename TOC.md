
## BLOQUE 1:    Fundamentos y entorno
| Status | Guide | Type | Title |
|---|---|---|---|
| [X] | 01-001 | | Presentación de la formación y objetivos |
| [X] | 01-002 | | Entorno de trabajo: Python, NumPy, Jupyter/scripts |
| [ ] | 01-003 | | Repaso de Python esencial para cálculo numérico (listas, arrays, bucles, funciones, tipos numéricos) |
| [X] | 01-004 | | Introducción a NumPy (`np.array`, `dtype`, `shape`, `ndim`, `size`, broadcasting básico) |
| [X] | 01-005 | | Buenas prácticas y depuración (lectura de errores, `nan`, `inf`, comparaciones con tolerancia `np.isclose`) |

## BLOQUE 2:    Álgebra lineal: VECTORES
| Status | Guide | Type | Title |
|---|---|---|---|
| [X] | 02-001 | | ¿Qué es un vector? Interpretación geométrica y como lista de datos |
| [X] | 02-002 | | Creación y representación en NumPy (vectores 1D, `shape`, `dtype`) |
| [X] | 02-003 | | Operaciones básicas con vectores (suma, resta, multiplicación por escalar) |
| [X] | 02-004 | | Normas vectoriales (L1 `ord=1`, L2 `ord=2`, L∞ `ord=np.inf`; cálculo manual vs. `np.linalg.norm`) |
| [X] | 02-005 | | Producto escalar (`u @ v`, `np.dot`, `np.sum(u * v)`; propiedades; interpretación geométrica) |
| [X] | 02-006 | | Relación entre producto escalar, norma y ángulo (coseno, `np.arccos`, `np.clip`; agudo/recto/obtuso; signo) |
| [X] | 02-007 | | Similitud del coseno (fórmula, rango [−1,1], interpretación, vector cero, aplicaciones en datos) |

## BLOQUE 3:    Álgebra lineal: MATRICES
| Status | Guide | Type | Title |
|---|---|---|---|
| [X] | 03-001 | | Introducción al bloque de matrices (contexto) |
| [X] | 03-002 | | Vectores  |
| [X] | 03-003 | | ¿Qué es una matriz? `shape`, `ndim`, `size` |
| [X] | 03-004 | | Acceso a filas, columnas y elementos (indexación) |
| [X] | 03-005 | | Operaciones básicas: elemento a elemento (Producto de Hadamard), escalar, multiplicación matricial (`@`, Esquema de Falk) y compatibilidad |
| [ ] | 03-006 | | Transpuesta y matrices simétricas |
| [ ] | 03-007 | | Determinante, traza y rango |
| [ ] | 03-008 | | Matriz inversa y matrices singulares |
| [ ] | 03-009 | | Sistemas de ecuaciones lineales (`np.linalg.solve`, `lstsq`) |
| [ ] | 03-010 | | Operaciones avanzadas con matrices (producto de Kronecker, particionado, broadcasting avanzado) |
| [ ] | 03-011 | | Autovalores y autovectores (`np.linalg.eig`, diagonalización, interpretación geométrica) |
| [ ] | 03-012 | | Descomposiciones matriciales (SVD `np.linalg.svd`, LU, QR; aplicaciones) |
| [ ] | 03-013 | | Aplicaciones en datos (PCA, regresión lineal, similitud, reducción de dimensionalidad) |

## BLOQUE 4:    Cálculo diferencial e integral
| Status | Guide | Type | Title |
|---|---|---|---|
| [ ] | 04-001 | | Funciones y límites |
| [ ] | 04-002 | | Derivadas (reglas básicas, derivadas parciales, gradiente) |
| [ ] | 04-003 | | Optimización (mínimos/máximos, descenso de gradiente) |
| [ ] | 04-004 | | Integrales (integral definida, aproximación numérica) |
| [ ] | 04-005 | | Aplicaciones en datos (funciones de pérdida, ajuste de modelos) |

## BLOQUE 5:    Probabilidad y estadística
| Status | Guide | Type | Title |
|---|---|---|---|
| [ ] | 05-001 | | Variables aleatorias y distribuciones |
| [ ] | 05-002 | | Medidas de tendencia central y dispersión |
| [ ] | 05-003 | | Distribuciones comunes (normal, uniforme, binomial) |
| [ ] | 05-004 | | Correlación y covarianza |
| [ ] | 05-005 | | Inferencia básica (muestreo, intervalos de confianza, contraste de hipótesis) |
| [ ] | 05-006 | | Aplicaciones en datos (análisis exploratorio, simulación) |

## BLOQUE 6:    uente a Machine Learning, Aplicaciones integradas y proyectos
| Status | Guide | Type | Title |
|---|---|---|---|
| [ ] | 06-001 | | Análisis de datos con álgebra lineal |
| [ ] | 06-002 | | Modelos básicos de machine learning desde cero |
| [ ] | 06-003 | | Proyecto integrador (dataset real, pipeline completo: limpieza, transformación, modelo, evaluación) |
| [ ] | 06-004 | | Repaso y consolidación |