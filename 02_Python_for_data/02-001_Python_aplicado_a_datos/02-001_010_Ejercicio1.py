# Ejercicio 1
"""
ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]

"""

# EJERCICIO 1
print("\n --- EJERCIO 1------ \n")
"""
Calcula los importes de las cuatro ventas con una comprensión de listas
y  obtén el total
"""
ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]

ventasA = [ventas[0]["precio"] * ventas[0]["unidades"] ]
ventasB = [ventas[1]["precio"] * ventas[1]["unidades"] ]
ventasC = [ventas[2]["precio"] * ventas[2]["unidades"] ]
ventasD = [ventas[3]["precio"] * ventas[3]["unidades"] ]

ventas_totales_listcomprehension = [ valor["precio"] * valor["unidades"] for valor in ventas ]

ventas_totales_sum = sum(ventas_totales_listcomprehension)
 
# ventas_totales_list = list(ventasA, ventasB, ventasC, ventasD)

# ventas_totales = sum(ventas_totales_list)

ventas_totalagrupado_desglose_zip = zip(
    list(zip(ventas[0]["producto"], ventasA)),
    list(zip(ventas[1]["producto"], ventasB)),
    list(zip(ventas[2]["producto"], ventasC)),
    list(zip(ventas[3]["producto"], ventasD))
)


ventas_totalagrupado_desglose_list = zip(
    ventasA, ventasB, ventasC, ventasD
)

print("\nGanancias totales")
print("  ", ventas_totales_sum)

print("\n Total ganacias por modelo desglosado\n")
print("  Ventas Modelo A: ", ventasA)
print("  Ventas Modelo B: ", ventasB)
print("  Ventas Modelo C: ", ventasC)
print("  Ventas Modelo D: ", ventasD)

print("\n\n Ganancias por modelo usando List Comprehension")
print("    ", ventas_totales_listcomprehension)

print("\n\n Ganancias por modelo usando zip()+list()+zip()")
print("    ", list(ventas_totalagrupado_desglose_zip))

print("\n\n Ganancias por modelo usando zip() simple")
print("    ", list(ventas_totalagrupado_desglose_list))



# EJERCICIO 2
print("\n --- EJERCIO 2------ \n")
"""
Obtén una lista con los nombres de los productos cuyo importe sea superior a 50 €
"""
ventas = [
    {"producto": "A", "precio": 22, "unidades": 3},
    {"producto": "B", "precio": 51, "unidades": 7},
    {"producto": "C", "precio": 101, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]

list_comprehension_previa = [ valor["precio"] for valor in ventas]

# condicion = list(list_comprehension_previa >= 51)

filtradoMal = [ valor["precio"] > 50 for valor in ventas ]
# Daroa bools porque se está haciendo una comparación directa, no un filtrado

# NEW_LIST for ITEM in COLLECTION if CONDITION

filtrados = [ valor["precio"] for valor in ventas if valor["precio"] > 50 ]

print("\n Productos cuyo precio es superior a 50:", filtrados)


# EJERCICIO 3
print("\n --- EJERCIO 3------ \n")
"""
Dadas estas listas, combina cada producto con su importe usando zip()

productos = ["A", "B", "C"]
importes = [60, 105, 24]

"""

productos = ["A", "B", "C"]
importes = [60, 105, 24, 99] # Meto un valor de mas para autorecordarme que zip() se detendrá en el momento en que unos valores con otros se unan

merged_zip = list(zip(productos, importes))

print("\n Lista mezclada de importes y productos: ", merged_zip)



# EJERCICIO 4
print("\n --- EJERCICIO 4------ \n")
"""
Recogiendo el ejercicio anterior, explica con tus palabras la diferencia entre map(), zip() y una comprensión de listas.
"""

productos = ["A", "B", "C"]
importes = [60, 105, 24, 99] # Meto un valor de mas para autorecordarme que zip() se detendrá en el momento en que unos valores con otros se unan

merged_zip = zip(productos, importes)

print("Contenido de  'merged_zip = zip(productos, importes)'\n   ", list(merged_zip))
print("\n - ¿Qué tipo este nuevo zip() a secas? -> ", type(merged_zip))
print("\n - En cuanto se ha usado el zip ... SE CONSUME, por lo que merged_zip es VACIO a partir de este momento\n")
print("   Lo usamos de nuevo y .... ", list(merged_zip), "... está vacío!")
print("   \nPor ello, creo de nuevo pero con 'list( zip() )':")

merged_zip_list = list(zip(productos, importes))

print("\n Invocamos al nuevo list mergeado: ", merged_zip_list)
print("\n Ya lo hemos usado, ¿Se ha consumido?: ", merged_zip_list)
print("   No. Una lista no se consume.\n    - Objetos como zip(), map() o filter() SIEMPRE se consumen, son como una 'cinta transportadora'")

