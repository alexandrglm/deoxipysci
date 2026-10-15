# 1.3. map(), zip() y comprensión de listas

"""
Son herramientas que conviene distinguir, porque pueden resolver problemas parecidos,
PERO NO HACEN LO MISMO
"""

# map() - Aplicar una transformación a cada elemento

## IVA

precios = [20,15,12,10]
iva = 1.10

resultadoMap = map(lambda precio : precio * iva, precios)

print(resultadoMap)

print("\n  Modo map(): ", list(resultadoMap))
# map() devuelve un iterador, no una lista
# Por eso usamos list() para ver todos sus resultados

print("\n --------- \n")

# Usando LIST COMPREHENSION
## La misma operación con comprensión de listas
import math

precios = [20,15,12,10]
iva = 1.10

resultadoListComprehension = [precio * iva for precio in precios]
resultadoListComprehensionCeil = [math.ceil((precio * iva) * 100 ) / 100 for precio in precios]

print("\n  Modo ListComprehension: ", resultadoListComprehension)

# Para transformaciones sencillas, la comprensión suele ser más legible.

# Además, permite manipular mucho más sencillo los valores, por ejemplo, redondeos
resultadoListComprehensionCeil = [math.ceil((precio * iva) * 100 ) / 100 for precio in precios]
print("\n  Modo ListComprehension con Ceil: ", resultadoListComprehensionCeil)

print("\n --------- \n")


# zip()
## combinar elementos de varias secuencias por posición

productos = ["Modelo A", "Modelo B", "Modelo C", "Modelo D"]

importes = [60, 24, 120, 49, 15, 26]

productosImportesMerged = list(zip(productos, importes ))

print(productosImportesMerged)
# En cada agrupación hecha, el primer elemento procede de productos y el segundo de importes
# Por defecto, zip() se detiene cuando se agota la secuencia más corta

print("\n --------- \n")

# LIST COMPREHENSION 2
# transformar y, opcionalmente, filtrar

numeros = [1,2,3,4,5,6]

cuadrados_pares = [
    x**2 for x in  numeros if x % 2 == 0
]

cuadrados_impares = [
    x**2 for x in numeros if x % 2 != 0
]

print("\n - Cuadradors PARES: ", cuadrados_pares)
# [4, 16, 36]
print("\n - Cuadradors IMPARES: ", cuadrados_impares)
# [1, 9, 25]



# print("\n --------- \n")




