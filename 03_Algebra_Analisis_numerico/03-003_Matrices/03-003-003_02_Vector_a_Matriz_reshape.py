import numpy as np

v = np.array([1, 2, 3])

print(f"""
PARTE 1: EL PROBLEMA DE LOS VECTORES 1D Y EL .T


- Vector original v:
{v}

  - Shape de v: {v.shape}
""")


## Si  transponemos un vector 1D
v_transpuesto = v.T
print(f"""
- v.T (intentando transponer un 1D):
{v_transpuesto}

  - Shape de v.T: {v_transpuesto.shape} 
""")





print("""
PARTE 2: LA SOLUCIÓN CON .reshape(x, y) Y EL COMODÍN '-1'

- Para convertir un vector plano en una matriz real (columna o fila), 
  necesitamos obligatoriamente añadirle un segundo eje usando .reshape():
""")

### Convertimos a matriz columna (3 filas, 1 columna)
v_columna = v.reshape(3, 1)

print(f"""
- Matriz columna usando v.reshape(3, 1):
{v_columna}

  - Shape:  {v_columna.shape}
""")

## Convertimos a matriz fila (1 fila, 3 columnas)
v_fila = v.reshape(1, 3)

print(f"""
- Matriz fila usando v.reshape(1, 3):
{v_fila}

  - Shape: {v_fila.shape}
""")





print("""
PARTE 3: EL COMODÍN '-1' (AUTOMATIZACIÓN EN ML)

- En lugar de escribir el número exacto de filas a mano, usamos '-1'
- Esto le dice a NumPy: 
    'Ey, calcula tú automáticamente cuántas filas hacen falta para que encajen todos los elementos, pero déjame exactamente 1 columna!'
""")

## Usando el comodín -1 para transformar v en una columna perfecta automáticamente
v_columna_automatica = v.reshape(-1, 1)

print(f"""
- v.reshape(-1, 1):
{v_columna_automatica}")

    -Shape: {v_columna_automatica.shape}
""")

## Si a esa columna reshapeada le aplicamos .T, pasa a ser fila de forma limpia
v_columna_a_fila = v.reshape(-1, 1).T

print(f"""
- v.reshape(-1, 1).T (pasando de columna a fila):
{v_columna_a_fila}

    - Shape final: {v_columna_a_fila.shape}
""")