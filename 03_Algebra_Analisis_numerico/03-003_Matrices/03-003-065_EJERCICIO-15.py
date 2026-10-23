# EJERCICIO 15
import numpy as np

print(f"""
# Ejercicio 15. Sarrus

Calcula con la regla de Sarrus el determinante 
[ 1 & 0 & 2 ], [ 0 & 1 & 0 ], [ 3 & 0 & 1 ]
""")

a, b, c = 1, 0, 2
d, e, f = 0, 1, 0
g, h, i = 3, 0, 1

A = np.asarray([ [a, b, c], [d, e, f], [g, h, i] ])

aei = a * e * i
bfh = b * f * g
cdh = c * d * h

ceg = c * e * g
afh = a * f * h
bdi = b * d * i

positivos_diagonal_principal = ( aei + bfh + cdh )
negativos_diagonal_secundaria = ( ceg - afh - bdi )

sarrus_formula_final = positivos_diagonal_principal - negativos_diagonal_secundaria

print(sarrus_formula_final)
print(np.linalg.det(A))