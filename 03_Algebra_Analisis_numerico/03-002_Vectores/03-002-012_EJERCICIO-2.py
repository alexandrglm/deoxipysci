import numpy as np

heredoc = """
# 2
Calcula $(2,5,7) + (1,3,4)$.

"""
print(heredoc)
v_1 = np.array([2, 5, 7])
v_2 = np.array([1, 3, 4])

suma_vectores = v_1 + v_2

print("\n Suma de vectores: ", suma_vectores)