import numpy as np

# .array([ valores ]) - CREAR ARRAY
# Identificar tipos /es legacy, no np) 
## type() - Type of clasico
## .dtype - Tipo de dato almacenado
## .shape - Dimensiones Y tamaño de cada dimensión
## .ndim - Numero de dimensiones


# A. Cómo SÍ hacerlo (precios = np.array([20, 15, 12, 10]))
precios = np.array([20, 15, 12, 10])

print("\n A. Cuando 'precios = np.array([20, 15, 12, 10])' ...")
print("   1. print:  ", precios)
print("   2. Tipo?:   ", type(precios))
print("   3. Tipo de dato almacenado (dtype)?: ", precios.dtype)
print("   4. Dimensiones y tamaño de cada dimension (shape)?: ", precios.shape)
print("   5. Numero de dimensiones (ndim)?: ", precios.ndim)
print("\n   Para este ejemplo, `shape` será `(4,)` y `ndim` será `1`: es un vector de cuatro elementos.")




# B. Cómo NO hacerlo ( precios = np.array(list(zip("1","2","3","4")))  )

precios_list_zip_strings = np.array(list(zip("1","2","3","4")))

print("\n B. Cuando metemos list-zip para generarlo en el acto ... 'precios_list_zip_strings = np.array(list(zip('1','2','3','4')))' ...")

print("   1. print:  ", precios_list_zip_strings)
print("   2. Tipo?:   ", type(precios_list_zip_strings))
print("   3. Tipo de dato almacenado (dtype)?: ", precios_list_zip_strings.dtype)
print("   4. Dimensiones y tamaño de cada dimension (shape)?: ", precios_list_zip_strings.shape)
print("   5. Numero de dimensiones (ndim)?: ", precios_list_zip_strings.ndim)
print("\n   Para este ejemplo, `shape` será `(1,4)` y `ndim` será `2`: Es un elemento de cuatro vectores.")
# pendiente arreglar este ejemplo y la explicación
