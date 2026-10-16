# EJERCICIO 2
heredoc = """
Ejercicio 2 --> Operaciones vectorizadas

Con `precios = np.array([20, 15, 12, 10])`:
- Calcula un array con el IVA del 21 % incluido
- No uses (evidentemente) bucles ni comprensiones

- Deconstruye manualmente después sin numpe desde distintos enfoques.
    - Los resultantes te darán tipos raros en dtype, no es problema
    - Puedes hacer cast para dejar una lista preciosa

- Crea un array normal despues (NO NP) con los mismos precios y haz la misma operacion de iva
"""

import numpy as np

precios = np.array( [20,15, 12, 10])
iva = 1.21

precios_iva_21 = precios * iva

print(precios)
print(precios_iva_21)


deconstruido_raw = [
    precio * iva for precio in precios
]

deconstruido_float = [
    float(precio * iva) for precio in precios
]

print(deconstruido_raw)
print(deconstruido_float)


# Como NO quitar el iva
quitar_iva_21_MAL = 0.79
# No se puede "deshacer" así, ya no cuentas con la msima base
import math


sin_iva_MAL = [
    precio * quitar_iva_21_MAL for precio in deconstruido_float
]

sin_iva_ceil_arregla_este_desastre_por_ser_linear_no_log_peeeero = [
    math.ceil(precio * quitar_iva_21_MAL) for precio in deconstruido_float
]

print(sin_iva_MAL)
print(sin_iva_ceil_arregla_este_desastre_por_ser_linear_no_log_peeeero)

quitar_iva_bien_float = [

    precio / iva for precio in deconstruido_float

]
print(quitar_iva_bien_float)

quitar_iva_bien_int = [

    int( precio / iva ) for precio in deconstruido_float
]

print(quitar_iva_bien_int)
print(type(quitar_iva_bien_int))
devolver_type_original = np.array(quitar_iva_bien_int)
print(devolver_type_original)
print(type(devolver_type_original))


# CORRECCION  DETALLADA
"""

"""