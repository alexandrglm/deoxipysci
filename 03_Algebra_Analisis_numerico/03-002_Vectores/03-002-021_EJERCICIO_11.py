import numpy as np

heredoc = """
# 11. Interpretación

Calcula el producto escalar de `[1,2]` y `[2, 1]`. 
¿Es positivo, negativo o cero?
¿Qué te indica sobre el ángulo?
"""
print(heredoc)


u = np.array([1, 2])
v = np.array([2, 1])

producto_escalar = u @ v
euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.linalg.norm(v, ord=2)

print(producto_escalar)
heredoc_explica = """
Es positivo, por lo que hablamos de un ángulo agudo.
Vamos a visualizarlo en datos
"""
print(heredoc_explica)


coseno_theta = producto_escalar / ( euclidea_u * euclidea_v )
theta = np.degrees(
    np.arccos(
        np.clip(coseno_theta, -1, 1)
    )
)

print(theta)
print(coseno_theta)

heredoc_explica_2 = f"""
- Es un ángulo de {theta:.1f} grados
    - Al encontrarse entre 0° y 90°, se trata de un ángulo agudo
    
- Esto confirma lo que anticipaba el producto escalar positivo (4): 
    * Los vectores `u` y `v` apuntan de manera general hacia la misma dirección (comparten cuadrante).
    * NOTA de correccion detallada:\n      Que compartan cuadrante no es regla general para concluir que el producto escalar es positivo\n      Con que su ángulo sea agudo, es suficiente (dos vectores pueden tener producto escalar positivo sin que todas sus componentes tengan el mismo signo!)
"""
print(heredoc_explica_2)