import numpy as np

heredoc = """
# 13. Relación con las normas

Dados `u = np.array([3, 4])` y `v = np.array([4, 3])`, calcula:

- El producto escalar.
- La norma euclídea de cada vector con `np.linalg.norm()`.
- Si el producto escalar es positivo, negativo o cero.
"""
print(heredoc)

u = np.array([3, 4])
v = np.array([4, 3])

heredoc_explica_1 = """
A ojo, producto escalar es 24.
Distancia euclidea, normal L2 es 5 para ambos
El producto escalar es positivo, y tendrá un ángulo agudo

Ahora, a demostrarlo:
"""
print(heredoc_explica_1)

producto_escalar = u @ v

euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.linalg.norm(v, ord=2)



# Normal, manuales, para recordarlos
print("\n-----------\n")
print("(KIT-KAT - Normas, manualmente, ara recordarlo)")
cuadrado_u_0 = u[0] ** 2
cuadrado_u_1 = u[1] ** 2

cuadrado_v_0 = v[0] ** 2
cuadrado_v_1 = v[1] ** 2

suma_cuadrados_u = np.sum(cuadrado_u_0 + cuadrado_u_1)
suma_cuadrados_v = cuadrado_v_0 + cuadrado_v_1

print(suma_cuadrados_u)
print(type(suma_cuadrados_u))
print(suma_cuadrados_v)
print(type(suma_cuadrados_v))
print(suma_cuadrados_u == suma_cuadrados_v)

euclidea_manual_u = np.sqrt(suma_cuadrados_u)
euclidea_manual_v = np.sqrt(suma_cuadrados_v)

norma_L1_u = np.sum( np.abs(u) )
norma_L1_v = np.sum( np.abs(v) )

infinito = np.inf

norma_Linf_u = np.max( np.abs(u) )
norma_Linf_v = np.max( np.abs(v) )

print(f"Euclidea manual de u:  {euclidea_manual_u}")
print(f"Euclidea manual de v:  {euclidea_manual_v}")

print(f"Norma L1 manual de u:  {norma_L1_u}")
print(f"Norma L1 directa de u:  {np.linalg.norm(u, ord=1)}")
print(f"Norma L1 manual de v:  {norma_L1_v}")
print(f"Norma L1 directa de v:  {np.linalg.norm(v, ord=1)}")
print(f"{norma_L1_u == np.linalg.norm(u, ord=1)} / {norma_L1_v == np.linalg.norm(v, ord=1)} ")

print(f"Norma L-inf manual de u:  {norma_Linf_u}")
print(f"Norma L-inf directa de u:  {np.linalg.norm(u, ord=infinito)}")
print(f"Norma L-inf manual de v:  {norma_Linf_v}")
print(f"Norma L-inf directa de v:  {np.linalg.norm(v, ord=infinito)}")
print(f"{norma_Linf_u == np.linalg.norm(u, ord=infinito)} / {norma_Linf_v == np.linalg.norm(v, ord=infinito)} ")

print("\n-----------\n")


coseno_theta =  producto_escalar / (euclidea_u * euclidea_v)
theta = np.degrees( np.arccos( np.clip(coseno_theta, -1, 1) ) )

print(producto_escalar)
print(euclidea_u)
print(euclidea_v)
print(coseno_theta)
print(theta)


heredoc_explica_2 = f"""
- Producto escalar:  {producto_escalar}
- Euclideas de {u} es: {euclidea_u}
- Euclidea de {v} es: {euclidea_v}
- Coseno theta es {coseno_theta}
- Angulo es de {theta:.2f} grados
"""
print(heredoc_explica_2)