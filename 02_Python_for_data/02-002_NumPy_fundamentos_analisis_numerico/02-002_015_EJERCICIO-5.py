
# EJERCIO 5
heredoc = """
Ejercicio 5 --> Mini análisis de ventas

    precios = np.array([20, 15, 12, 10])

    unidades = np.array([3, 7, 2, 4])

- Calcula los importes por producto
- la facturación total
- la media de los importes
- el importe más alto
"""
import numpy as np

precios = np.array([20,15, 12, 10])
unidades = np.array([3, 7, 2, 4])

importes_por_producto = precios * unidades
print(importes_por_producto)

facturacion_total = sum(importes_por_producto)
print(facturacion_total)

importes_producto_sorted = np.sort(importes_por_producto)
print(importes_producto_sorted)

media_importes = np.mean(importes_producto_sorted)
print(media_importes)

importe_mas_alto = np.max(importes_producto_sorted)
print(importe_mas_alto)


# CORRECCION DETALLADA
"""

"""