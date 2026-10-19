import numpy as np

heredoc = """
# 6. Norma L1

Calcula la norma L1 de f{v}=(-2,5,-3)
"""
print(heredoc)

vector = np.array([-2, 5, -3])

norma_L1 = np.linalg.norm(vector, ord=1)

print(f"- L1 del vector dado: {norma_L1}")
heredoc_explica = """
La Norma L1 es la suma de los valores ABSOLUTOS (es decir, sin signo).
Es la distancia total, la suma absoluta, entre los componentes del vector.
"""
print(heredoc_explica)