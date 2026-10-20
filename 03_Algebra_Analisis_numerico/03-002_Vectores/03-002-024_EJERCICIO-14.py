import numpy as np

heredoc = """
Calcula la similitud del coseno entre `f(u)=(1, 2)` y `f(v)=(2, 4)`

¿Por qué no es necesario que ambos vectores tengan la misma magnitud para que su similitud sea 1?

"""
print(heredoc)
u, v = np.asarray([1, 2]), np.asarray([2, 4])

print(u)
print(v)

euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.sqrt( np.sum(v ** 2) )


similitud_coseno =  u @ v / (euclidea_u * euclidea_v)


print( np.clip(similitud_coseno, -1, 1) )
print(np.isclose(similitud_coseno, 1))

heredoc_explica_1 = """
Al medir la similitud de coseno entre dos vectores, no estamos teniendo en cuenta la magnitud de las componentes:

- Queremos visualizar la dirección, la ORIENTACIÓN RELATIVA, 
- Es decir, COMPARAR HACIA DONDE APUNTA CADA VECTOR, no saber o comparar lo que miden
- Por lo que nos da igual su magnitud

Además, si el valor de similitud de coseno es 1 exacto, significa que ambos vectores contienen componentes en equivalencia,
y que la dirección de ambos va a ser exactamente la misma.

"""

print(heredoc_explica_1)



heredoc_correccion_matiz = """
Matiz conceptual: 
- Una similitud del coseno igual a 1 significa que los vectores no nulos apuntan en la misma dirección. 

No significa que sus componentes sean equivalentes o iguales: por ejemplo, [1, 2] y [2, 4] tienen componentes diferentes, pero la misma dirección.
"""
print(heredoc_correccion_matiz)