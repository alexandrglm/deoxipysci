import numpy as np

heredoc = """
Dados `u = np.array([1, 2, 3])` y `v = np.array([4, 5, 6])`
 - Calcula su producto escalar usando `np.dot()` y `@`
 - ¿Obtienes el mismo resultado?

"""
print(heredoc)

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])

escalar_metodo_dot = np.dot(u, v)
escalar_metodo_at = u @ v

print(escalar_metodo_dot)
print(escalar_metodo_at)
print(escalar_metodo_dot == escalar_metodo_at)
print(type(escalar_metodo_dot) == type(escalar_metodo_at))