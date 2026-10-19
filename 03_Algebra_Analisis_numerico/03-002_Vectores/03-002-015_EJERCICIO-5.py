import numpy as np

heredoc = """
# 5. Norma euclídea

Calcula manualmente la norma L2 de 
- f{v}=(6,8). 
- Muestra los pasos.
"""

vector = np.array([6, 8])

vector_cuadrados = vector ** 2

suma_cuadrados = np.sum(vector_cuadrados)

raiz_suma_cuadrados = np.sqrt(suma_cuadrados)

print(f"\n Norma L2 - Euclídea es: {raiz_suma_cuadrados}")