# EJERCICIO 16
import numpy as np

print(f"""
# Ejercicio 16. Propiedades de las determinantes

Si $A$ es una matriz 3x3 con determinante = 5:

- Cuanto vale determinante de 2A

""")

A = np.asarray([[1, 2, 3], [3, 5, 1], [2, 3, 3]])
print(A)
determinante_A = np.linalg.det(A)
print(determinante_A)

determinante_2_A = np.linalg.det(2 * A)
print(determinante_2_A)


A_producto_A = A * A
print(A_producto_A)
determinante_A_producto_A = np.linalg.det(A_producto_A)
determinante_producto_A_producto = determinante_A * determinante_A
print(determinante_A_producto_A)
print(determinante_producto_A_producto)
A_at_A = A @ A
determinante_A_at_A = np.linalg.det(A_at_A)
print(determinante_A_at_A)


explica = f"""
Dada la matriz... :
{A}

- Calculamos su determinante: {determinante_A}

- Qué determinante tendría 2A?

Una de las propiedades de las determinates, respecto al producto escalar de una matriz, dice literalmente:
"AL MULTIPLICAR UNA MATRIZ POR UN ESCALAR, POR CADA FILA SALE ESE NUMERO FUERA DEL DETERMINANTE.
POR ESO, SI LA MATRIZ TIENE n FILAS....EL NUMERO SALE n VECES"

Y como la norma se entiende bastante peor que la propia fórmula, aquí la fórmula:

    det(kA) = K^n * det(A), donde n es el numero de componentes (siendo sarrus, 3)
        es decir ...
    det(2A) = 2 ** 3 * det(A)

Dado escalar: 2
Determinante de 2A será:    {2 ** 3 * determinante_A}

{np.isclose(2 ** 3 * determinante_A, determinante_2_A)}

Por lo que queda demostrada la propiedad de la determinante de producto de escalar por matriz.

- ¿qué determinante tendría A * A?

Por curiosidad, quiero hacer la multiplicación matricial y comprobar su propiedad específica (PRODUCTO DE MATRICES):

"EL DETERMINANTE DE LOS PRODUCTOS es LOS PRODUCTOS DEL DETERMINANTE"

det(AB) = det(A) * det(B)

Por lo que ...
det(AA) = det(a) * det(B)

{np.linalg.det(A) * np.linalg.det(A)}


Lo que, a nivel de código podemos aplicarlo así:

- np.linalg.det(A) * np.linalg.det(A)
{np.isclose(determinante_producto_A_producto, np.linalg.det(A) * np.linalg.det(A))}
- np.linalg.det(A @ A)
{np.isclose(determinante_A_at_A, np.linalg.det(A) * np.linalg.det(A))}
- Incluso, así:   np.linalg.det( np.linalg.det(A) * np.linalg.det(A) )
{np.isclose(determinante_producto_A_producto, np.linalg.det(A) * np.linalg.det(A))}


- Pero, JAMAS, JAMAS DE LOS JAMASES, A NIVEL CODIGO, APLICAR: determinate_AA = np.lingalg.det(A * A) JAMAS
{np.isclose(determinante_producto_A_producto, np.linalg.det(A * A))}
    Porque estamos sacando la determinante de dos determinantes previas, no calculando la determinante del
    correcto producto matricial.
    


"""
print(explica)