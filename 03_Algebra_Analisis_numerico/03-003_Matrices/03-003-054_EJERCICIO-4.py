import numpy as np

print("""
# Ejercicio 4. Operaciones elemento a elemento

Crea las matrices `A = [[1, 2], [3, 4]]` y `B = [[5, 6], [7, 8]]`

    -Calcula `A + B`, `A - B` y `A * B`.
""")

print("""
A ojo, antes de calcular:
Suma:   [ [6, 8], [8, 12] ]
Resta:  [ [-4, -4],[-4, -4] ]
Mult:   [ [5, 12], [21, 32]]
""")
A, B = np.asarray([[1, 2], [3, 4]]), np.asarray([[5, 6], [7, 8]])

print(A)
print(B)

suma = A + B
resta = A - B
multiplicacion_directa = A * B

print(f"""
Dadas {A} y {B}:

 - Suma directa es:  {suma}
 - Resta directa es:  {resta}
 - Producto de ambas matrices es: {multiplicacion_directa}

""")