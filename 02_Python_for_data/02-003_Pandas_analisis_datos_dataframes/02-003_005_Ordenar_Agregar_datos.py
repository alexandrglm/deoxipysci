import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2],
    "ventas" : [60, 105, 24, 40, 126, 135, 60]
})


ventas_sort_values = ventas.sort_values(

    by="producto",
    ascending=False
)

print("\n - Usando .sort_values() para la columna /producto/:\n")
print(ventas_sort_values)


ventas_sort_index = ventas.sort_index(
    ascending=False
)
print("\n - Usando .sort_index():\n")
print(ventas_sort_index)


# sum - mean - max - min en UNA columna

ventas_ventas_sum = ventas["ventas"].sum()
ventas_ventas_mean = ventas["ventas"].mean()
ventas_ventas_max = ventas["ventas"].max()
ventas_ventas_min = ventas["ventas"].min()

print("\n - sum() de ventas por producto:  ", ventas_ventas_sum,
      "\n - mean() de ventas por producto: ", ventas_ventas_mean,
      "\n - max() de ventas por producto:  ", ventas_ventas_max,
      "\n - min() de ventas por producto:  ", ventas_ventas_min)


# operaciones sobre VARIAS columnas

ventas_mean_por_columnas = ventas[  ["precio", "unidades", "ventas" ] ].std()

print("\n - Con una operacion algebráica sobre varias columnas, obtenemos una Series con estadísticas:")

print('\n   * [ ["precio", "unidades", "ventas" ]].mean() :')
print(ventas_mean_por_columnas)