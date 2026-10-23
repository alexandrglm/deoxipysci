# EJERCICIO 17
import numpy as np

print(f"""
# Ejercicio 17. Determinantes -  NumPy, tipos según método

Si `d = np.linalg.det(A)` devuelve `-2.0000000000000004`
    - ¿Por qué `d == -2` da `False`? 
    - ¿Qué debes usar en su lugar?

""")

explica = f"""
- Por que NO se debe usar la comparación directa, ya que los métodos con NumPy trabajan con floats,
y los valores que nos devuelvan nunca serán idénticos, sino aproximados.

- Para eso, está el método np.isclose(VALOR, VALOR A COMPARAR)
    - Nos indica, retornando un boolean, si los valores son cercanos
    - Como apunte, si las componentes, o los valores, si las magnitudes fueran "desbordantes" (tolerancias, notación científica),
        podemos ajustar su tolerancia relativa y tolerancia abolustas con los argumentos rtol= y atol=

"""