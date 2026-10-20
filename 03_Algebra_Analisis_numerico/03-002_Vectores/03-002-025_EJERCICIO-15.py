import numpy as np

heredoc = """
## Ejercicio 15. Direcciones opuestas

Calcula la similitud del coseno entre `u = np.array([1, 0])` y `v = np.array([-3, 0])`.

Interpreta el resultado.
"""

u, v = np.asarray([1, 0]), np.asarray([-3, 0])

euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.linalg.norm(v, ord=2)

similitud_coseno_theta = u @ v / (euclidea_u * euclidea_v)

print(similitud_coseno_theta)

angulo_medido = np.degrees(np.arccos(np.clip(similitud_coseno_theta, -1, 1)))

heredoc_explica = f"""
- El valor de similitud de coseno para {u} y {v} es:  {similitud_coseno_theta}

    * Es el máximo valor negativo
    * Direcciones absolutamente opuestas para cada vector
    * Se podría visualizar como un ángulo llano (de {angulo_medido} grados)
"""
print(heredoc_explica)