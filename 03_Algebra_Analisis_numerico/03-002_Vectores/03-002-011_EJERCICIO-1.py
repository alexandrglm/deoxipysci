import numpy as np

heredoc = """
# **1. Componentes y dimensión**

Dado v = (8, 2, 6, 4) ....
-   Indica cuántos componentes tiene
-   Cuál es su tercer componente
"""
print(heredoc)
v = np.array([8, 2, 6 ,4])

print(" Dimensiones: ", v.shape, "(tiene cuatro componentes)")
print(" Tercer componente es: ", v[2])