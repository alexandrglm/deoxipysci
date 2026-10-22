import numpy as np



# 2 x 2
print("\n- Determinante manual (2 x 2\n")
A = np.array([ [1, 2], [3, 4] ])

a, b = A[0]
c, d = A[1]

determinante_manual = a * d - b * c

print(A)
print(np.linalg.det(A))
print(determinante_manual)
print(np.isclose(determinante_manual, np.linalg.det(A) ))




# Regla de Sarrus, 3 x 3
P = np.array([ [2, 0, 1], [1, 3, 2], [1, 1, 4] ])
print(f"""
- 3 x 3, REGLA DE SARRUS:

{P}

Visualiza:

a, b, c 
d, e, f
g, h, i

POSITIVOS:  Tira por diagonales PRINCIPAL y la vas desplazando a la derecha
NEGATICOS:  Tira por diagonal SECUNDARIA, y desplazas a la derecha

(+)     a*e*i  +  b*f*g  +  c*d*h
(-)     c*e*g  -  a*f*h  -  b*d*i

DETERMINANTE (sarrus 3x3) = positivos - negativos
""")

a, b, c = P[0]
d, e, f = P[1]
g, h, i = P[2]

positivos = (a * e * i) + (b * f * g) + (c * d * h)
negativos = (c * e * g) + (a * f * h) + (b * d * i)

determinante_sarrus = positivos - negativos

aei = a * e * i
bfg = b * f *g
cdh = c * d * h

ceg = c * e * g
afh = a * f * h
bdi = b * d * i

positivos_negativos_en_serie_es_la_determinante_literal = aei + bfg + cdh - ceg - afh - bdi

print(positivos_negativos_en_serie_es_la_determinante_literal)
print(np.isclose(positivos_negativos_en_serie_es_la_determinante_literal, determinante_sarrus))

print(determinante_sarrus)
print(np.isclose(determinante_sarrus, np.linalg.det(P)))


# Matriz NO cuadrada, numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
M = np.array([[10, 2, 3], [4, 5, 6]])
# print(np.linalg.det(M))

## PEEEERO, TRUQUINI! Si le metes una nueva serie con las componentes que requiere para ser cuadrada ... ya puedes hacerle la determinada!
# Y meter UNO's es la opción más adecuada si no puedes introducir una serie REAL que tenga sentido con los datos de la propia matriz
unos = np.ones(3, dtype=int)
print(unos)

M = np.vstack( (M, unos) )

print(M)
# Eso sí ... la determinada será siempre CERO!
print(np.linalg.det(M))
