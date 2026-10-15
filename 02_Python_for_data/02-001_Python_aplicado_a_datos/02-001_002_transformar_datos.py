ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4},
]

# OBJETIVO: calcular el importe de cada venta: precio multiplicado por unidades

importes = [

    (venta["precio"] * venta["unidades"]) for venta in ventas
]

print(importes)
# [60, 105, 24, 40]


# El total es
total = sum(importes)

print(total)
# sum() ya resuelve la acumulación. Para este caso, no necesitamos reduce()

