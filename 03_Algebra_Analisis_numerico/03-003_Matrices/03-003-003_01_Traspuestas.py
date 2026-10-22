import numpy as np

A = np.asarray([ [1, 2, 3], [4, 5, 6]])

print(A.shape)


A_transpuesta = A.T
A_transpuesta_metodo = np.transpose(A)

print(A_transpuesta)
print(A_transpuesta.shape)

print(A_transpuesta_metodo)
print(A_transpuesta_metodo.shape)


# A)    Vista directa VS *copy()
print("PARTE 1:     VISTA VS MODIFICACION (EFECTO COLATERAL)")

A = np.asarray([[1, 2, 3], [4, 5, 6]])

print(f"Matriz A original:\n{A}\n")

## Primera transpuesta... NO es un objeto nuevo, es una vista
A_transpuesta = A.T
# A_transpuesta_metodo = np.transpose(A)

print(f"Matriz transpuesta (A.T):\n{A_transpuesta}")
print(f"Shape de la transpuesta: {A_transpuesta.shape}\n")

print(f"""
- Los métodos 'matriz.T' / 'np.transpose(matriz)' NO duplican los datos:

  * SOLO crean una VISTA de la matriz original con los ejes intercambiados.
  * Como comparten memoria, si modificas un valor en la transpuesta, 
    AUTOMÁTICAMENTE se modificará en la matriz inicial 'A'
""")

## Modificamos la transpuesta
A_transpuesta[0, 0] = 99

print(f"""
- Modificamos el primer componente de la transpuesta ( A_transpuesta[0,0] = 99 ):
{A_transpuesta}

- Si revisamos la matriz A original, el cambio se ha propagado:
{A}
""")


# B)    DEMOSTRACIÓN DE CÓMO AISLARLO CON .copy()
print("PARTE 2:     CÓMO AISLARLO USANDO .copy()")


## Reiniciamos la matriz A a sus valores originales
A = np.asarray([[1, 2, 3], [4, 5, 6]])

print(f"- Restauramos la matriz A original:\n{A}\n")

print("""
- PARA PRESERVAR LA MATRIZ ORIGINAL, conviene crear una copia independiente:
  * Usamos: A.T.copy() /  np.transpose(A).copy()
""")

## Creamos una copia transpuesta e independiente
A_copiada_transpuesta = A.T.copy()

print(f"- A copiada y transpuesta (aislada en memoria):\n{A_copiada_transpuesta}\n")

## Modificamos esta nueva matriz
A_copiada_transpuesta[0, 0] = 99

print(f"""
- Modificamos el primer componente de la copia transpuesta a 99:
{A_copiada_transpuesta}

- Comprobamos que estamos trabajando con la copia... y que la matriz A original está intacta:
{A}
""")