import pandas as pd

ventas = pd.DataFrame({
    "producto" : ["A", "B", "C", "D", "E", "F", "G"],
    "precio" : [20, 15, 12, 10, 14, 27, 30],
    "unidades" : [3, 7, 2, 4, 9, 5, 2]
})

print(ventas)

print("\n- 1. Tipo:    ", type(ventas))
print("\n- 2. Tipos que contiene ( .dtypes ):          \n", ventas.dtypes)

print("\n- 3. Info del DataFrame ( .info() ):            \n", 
      "\n     * 3.1 info() es un metodo inplace=True, un print() retoranará esto: ", ventas.info(),
      "\n     * 3.2 La info() completa de un dataframe con un invoke directo de info es:\n ")
ventas.info()

print("\n- 4. Descripción de DataFrame ( .describe() ):  \n", 
      "\n     * Muestra las operaciones algebráicas básicas para todos los valores:\n")
print(ventas.describe())


print("\n- 5. Shape del DataFrame ( .shape ): ", ventas.shape)

print("\n- 6. Columnas del DataFrame ( .columns ):     \n   ", ventas.columns)

print("\n- 7. Primeras CINCO filas ( .head() ):                \n   ", ventas.head())
print("\n- 8. Ultimas CINCO filas ( .tail() ):                 \n   ", ventas.tail())


