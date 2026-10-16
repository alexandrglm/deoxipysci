import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2]
})


# Seleccionar UNA columna

precios = ventas["precio"]

print(precios)
print(type(precios))

# Selecc. VARIAS columnas

precios_unidades = ventas[["precio", "unidades"]]
print(precios_unidades)
print(type(precios_unidades))


# Crear nueva columnna, vectorizar operaciones a nuevas columnas

ventas["ventas"] = ventas["precio"] * ventas["unidades"]

print(ventas)



# Evidentemmente, los métodos para exponer el DataFrame son permitidos

precios_tail = precios.tail()
precios_head = precios.head()


print(precios_head)
print(precios_tail)


