# 01: Data Structures, list comprehesion, legacy methods, but Pandas

"""
- Facturación total y Facturación por producto para:
ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4}
]

"""

ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4}
]

# ACCESO A KEYS ESPECIFICAS

# MODO 1, for in, COMPRENSION DE LISTAS
listaPrecios = [valor["precio"] for valor in ventas]

print("\nModo 1 for in\n\n", listaPrecios)

# MODO 2, usando append(), LEGACY PURO
listaPrecios = []

for valor in ventas:
    listaPrecios.append(valor["precio"])

print("Modo 2, append()\n\n", listaPrecios)


# MODO 3 map() operator.itemgetter(), RENDIMIENTO PURO
from operator import itemgetter

ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4}
]

listaPrecios = []
listaPrecios = map(itemgetter("precio"), ventas)

print("Modo 3 itemgetter() map()\n\n", listaPrecios)


# Modo 4, PANDAS, RENDIMIENTO + MULTIPLES POSIBILIDADES
import pandas as pd

ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4}
]

dataFrameVentas = pd.DataFrame(ventas)

print("Modo 4, Pandas Dataframe\n\n  - Como se ve un DataFrame?\n\n", dataFrameVentas, "\n\n    Como una matriz, con todos los datos visualmente ordenados")

listaPrecios = []

listaPrecios = dataFrameVentas["precio"]
print("\n\n   - Como se ve la extración de las keys de un DataFrame?\n\n" , listaPrecios, "\n\n    Se ve como una lista ordenada, donde nuevas key - values son creadas, key por orden de lista, y values la extraccion de los valores que le hemos pedido extraer")


# EJERCICIO ventasTotales, ventasPorProducto

# MODO PANDAS con df pero con operaciones básicas no pd

listaPrecios = []
dfVentasTotales = pd.DataFrame(ventas)

productos = dfVentasTotales["producto"]
precios = dfVentasTotales["precio"]
unidades = dfVentasTotales["unidades"]


factTotales = sum(precios * unidades)
# exactamente igual que sum(precios) * sum(unidades)

print("\n  Facturarion Total:  ", factTotales)

print("\n\n---------------------------\n\n")

# Creando una nueva list()
factPorProducto = list(precios * unidades)

print("\n  Facturacion por producto:\n\n", factPorProducto )
# recibimos  [60, 105, 24, 40]

print("\n\n---------------------------\n\n")

# Creandola con list y Mostrando la data organizada con zip
factPorProducto = None

factPorProducto = list(zip(productos, precios * unidades))
print("\n  Facturacion por producto:\n\n", factPorProducto )
# [('A', 60), ('B', 105), ('C', 24), ('D', 40)]


print("\n\n---------------------------\n\n")

# CREANDO UNA NUEVA COLUMNA!!!!
# recuperamos el dfVentasProductos inicial, para trbajar sobre el directamente

dfVentasTotales["TotalVentasPorProducto"] = dfVentasTotales["precio"] * dfVentasTotales["unidades"]

print(dfVentasTotales)
print("\n\n   Al DataFrame se le ha añadido ... Una nueva columna! ... Y esa es una de las ideas principales para manipular orígenes de datos")





# ventas = [
#     {"producto": "A", "precio": 20, "unidades": 3},
#     {"producto": "B", "precio": 15, "unidades": 7},
#     {"producto": "C", "precio": 12, "unidades": 2},
#     {"producto": "D", "precio": 10, "unidades": 4}
# ]


# print(ventas[0])
# print(ventas[-1])

# print("\n", ventas, "\n")
# ventas.pop()

# print("\n", ventas)

# def calculaTotal():

#     return sum(precio for precio in listaPrecios)

# print(calculaTotal())
    

# ventas.add({"producto": "D", "precio": 10, "unidades": 4})

# print("\n", ventas)

# ventas = [
#     { 
#         "productoA": {
#             "producto": "A", 
#             "precio": 20, 
#             "unidades": 3
#         } 
#     },    
#     { 
#         "productoB": {
#             "producto": "B", 
#             "precio": 88, 
#             "unidades": 7
#         } 
#     }
# ]

# # print(ventas[0])

# productoA = ventas[0].get('productoA', 'No hay Producto A')
# productoB = ventas[1].get('productoB', 'No hay Producto B')
# # print(productoA)

# print(productoA.values() + "\n" + productoB.values().toString() )
