import numpy as np

vector = np.array ([3, 4])

print("\n DESCOMPONIENDO LA EXPRESION MANUALMENTE: \n")

vector_cuadrado = vector ** 2
suma_cuadrados = np.sum(vector_cuadrado)

norma_euclidea_manual = np.sqrt(suma_cuadrados)
norma_euclidea_directa = np.linalg.norm(vector)

print(f" - VECTOR ORIGINAl:  {vector} ")
print(f"    Paso 1. Componentes al cuadrado (3^2, 4^2): {vector_cuadrado}")
print(f"    Paso 2. Suma de los cuadrados (9 + 16): {suma_cuadrados}")
print(f"    Paso 3. Raíz cuadrada de {suma_cuadrados}: {norma_euclidea_manual}")

print(f"\n - Valor manual:      {norma_euclidea_manual} \n - Calculo directo con np.linalg.norm(): {norma_euclidea_directa}")
print(f"\n       Son valores idénticos?:  {norma_euclidea_directa == norma_euclidea_manual} ")