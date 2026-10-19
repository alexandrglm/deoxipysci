import numpy as np

u = np.array([2, 4, 6])
v = np.array([1, 3, 5])

sum = u + v
subs = u - v
mult = u * v

heredoc = """Dados estos arrays:\n
    u = np.array([2, 4, 6])
    v = np.array([1, 3, 5])

Operamos fácilmente:\n
    sum = u + v
    subs = u - v
    mult = u * v

"""
print (heredoc)

print("     * Suma de u, v: ", sum)
print("     * Resta de u, v: ", subs)
print("     * Multiplicacion de u, v: ", mult)

print("\n - Siempre estamos trabajando y recibiendo Arrays de NumPy:")
print(type(u))
print(type(sum))
