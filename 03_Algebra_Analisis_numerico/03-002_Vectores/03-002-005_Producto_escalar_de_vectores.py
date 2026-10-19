import numpy as np

u = np.array([2, 3])
v = np.array([4, 5])


# Sin método, operación vectorizada tipica
producto_escalar_operacion_vectorizada = u * v

# Metodo 1 np.dot(u,v)
producto_escalar_metodo_1 = np.dot(u, v)

# Metodo 2 `u @ v`
producto_escalar_metodo_2 = u @ v
test_modo_at = np.array(np.array([2]) @ np.array([3]))

# Metodo 3 np.sum(u * v)
producto_escalar_metodo_3 = np.sum(u * v)


print(producto_escalar_operacion_vectorizada)
print(type(producto_escalar_operacion_vectorizada))


print(producto_escalar_metodo_1)
print(type(producto_escalar_metodo_1))

print(producto_escalar_metodo_2)
print(type(producto_escalar_metodo_2))

print(producto_escalar_metodo_3)
print(type(producto_escalar_metodo_3))

print(test_modo_at)
print(type(test_modo_at))