# EJERCICIO 1
print("\n --- EJERCIO 1------ \n")
heredoc = """
1. Calcula los importes de las cuatro ventas con una comprensión de listas
y  obtén el total

ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]
"""

print(heredoc)
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



# CORRECCION DETALLADA
"""
- List comprehension bien aplicada:

    ventas_totales_listcomprehension = [
        valor["precio"] * valor["unidades"]
        for valor in ventas
    ]

ventas_totales_sum = sum(ventas_totales_listcomprehension)

Con los datos del ejercicio, obtienes:
- Importes: [60, 105, 24, 40]
- Total: 229

"""

"""
PERO... 


1. No era necesario ventasA, ventasB, ventasC y ventasD individualmente. 
Se repite manualmente un trabajo que la comprensión de listas ya automatiza.


2. Además, las dos construcciones con zip() no producen exactamente el desglose que se quería:

    ventas_totalagrupado_desglose_zip = zip(
        list(zip(ventas[0]["producto"], ventasA)),
        list(zip(ventas[1]["producto"], ventasB)),
        list(zip(ventas[2]["producto"], ventasC)),
        list(zip(ventas[3]["producto"], ventasD))
    )
zip() aplicado a "X" y ventasX empareja los caracteres de la cadena con los elementos de la lista. 
Funciona accidentalmente con nombres de una letra, pero no es la estructura más adecuada.



Una solución limpia sería:

        desglose = [
            (venta["producto"], venta["precio"] * venta["unidades"])
            for venta in ventas
        ]

        print(desglose)
        # [('A', 60), ('B', 105), ('C', 24), ('D', 40)]

        print(sum(importe for _, importe in desglose))
        # 229


        Observa for _, importe in desglose: el guion bajo indica que no necesitamos utilizar el primer elemento de cada pareja.
"""