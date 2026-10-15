
# EJERCICIO 2
print("\n --- EJERCIO 2------ \n")
heredoc = """
Obtén una lista con los nombres de los productos cuyo importe sea superior a 50 €

ventas = [
    {"producto": "A", "precio": 22, "unidades": 3},
    {"producto": "B", "precio": 51, "unidades": 7},
    {"producto": "C", "precio": 101, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]
"""

print(heredoc)


ventas = [
    {"producto": "A", "precio": 50 , "unidades": 3},
    {"producto": "B", "precio": 51, "unidades": 7},
    {"producto": "C", "precio": 101, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]

list_comprehension_previa = [ valor["precio"] for valor in ventas]

# condicion = list(list_comprehension_previa >= 51)

filtradoMal = [ valor["precio"] > 50 for valor in ventas ]
# Daría bools porque se está haciendo una comparación directa, no un filtrado
# Y no se usa el NOMBRE DE LOS PRODUCTOS


# NEW_LIST for ITEM in COLLECTION if CONDITION

filtrados = [ valor["producto"] for valor in ventas if valor["precio"] >= 51 ]

print("\n Productos cuyo precio es superior a 50:", filtrados)



# CORRECCION DETALLADA

"""
- Identificado correctamente que esta expresión produce booleanos:

    filtradoMal = [valor["precio"] > 50 for valor in ventas]

    Devuelve:   [False, True, True, False]
    Y con esto no solventamos lo que se solicita


Sintaxis a recordaR: [ NEW_LIST for ITEM in COLLECTION if CONDITION ]

filtrados = [ valor["producto"] for valor in ventas if valor["precio"] >= 51 ]


MUY importante entender la forma y el uso de las condiciones en las extracciones
"""