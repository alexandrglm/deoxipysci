import numpy as np

heredoc = """
# 3. Multiplicación por un escalar

Calcula $4\,(2,3,5)$.
"""
print(heredoc)

escalar = 4
vector = np.array([2, 3, 5])

mult_vect_escalar = vector * escalar

print(vector)
print(escalar)
print(mult_vect_escalar)