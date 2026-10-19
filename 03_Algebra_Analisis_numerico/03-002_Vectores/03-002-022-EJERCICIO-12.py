import numpy as np

heredoc = """
# 12. Perpendicularidad

Comprueba mediante NumPy si `u = np.array([3, 0])` y `v = np.array([0, 4])` son perpendiculares.
Justifica la respuesta a partir del producto escalar.
"""
print(heredoc)

u = np.array([3, 0])
v = np.array([0, 4])



producto_escalar_sera_cero = u @ v
print(producto_escalar_sera_cero)

euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.linalg.norm(v, ord=2)

print(f"Euclidea de {u} es:  {euclidea_u}\nEuclidea de {v} es: {euclidea_v}")

coseno_theta_de_producto_cero_sera_cero = producto_escalar_sera_cero / (euclidea_u * euclidea_v)
print(coseno_theta_de_producto_cero_sera_cero)

theta = np.degrees( np.arccos( np.clip(coseno_theta_de_producto_cero_sera_cero, -1, 1) ) )
print(theta)


heredoc_explica = """
Algunas de sus componentes son 0, por lo que los ángulos finales serán ... ¿Inexistentes?
Es vector cero. Veamos ... 

1. Su producto escalar será 0 :   [0 0] = 0
2. Pero sus normas euclideas sí tienen valores:  f(u)=[3, 0] es 3, f(v)=[0, 4] es 4
3. Su coseno será 0 ... ¿Nulo? .. El producto escalar se divide entre L2 de u por L2 de v, producto era cero, coseno theta es cero.
4. Pero su theta, su ángulo, es de 90º, ángulo recto

Los ángulos rectos siempre son perpendiculares/ortogonales.
"""
print(heredoc_explica)


correccion_detallada = """
NOTA de correccion detallada:

- Que algunas componentes sean cero no significa que el ángulo sea inexistente. 
- Los dos vectores de este ejercicio son no nulos, porque sus normas son distintas de cero. El ángulo está perfectamente definido.

El caso especial es el vector cero,(0,0): su norma es cero y no tiene una dirección definida. 
Por eso, no se puede calcular el ángulo con otro vector mediante la fórmula del coseno, ya que el denominador sería cero.
"""

print(correccion_detallada)