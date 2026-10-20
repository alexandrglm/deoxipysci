import numpy as np

A = np.array([ [10, 20, 30], [40, 50, 60] ])

A_mezcla_tipos = np.array([ [10, "20", 30], [40, np.inf, None] ])

print(f"""
- ATRIBUTOS

Para array numérico puro, {A} :

    - Shape:                {A.shape}
    - Dimensiones:          {A.ndim}
    - Tamaño de valores:    {A.size}

    - Tipo de objeto:       {type(A)}

    - Tipo de valores num:  {A.dtype}
    - Tipo de Array fila:   {A[0].dtype}
    - Tipo de fila-valor 2: {type(A[0][1])}
    
    - Tamaño de Array colum:    {A[1].size}
    - Conte de valores reales:  {np.count_nonzero(A[0])}

Para array numérico con tipos mezclados,  {A_mezcla_tipos} :

    - Shape:                {A_mezcla_tipos.shape}
    - Dimensiones:          {A_mezcla_tipos.ndim}
    - Tamaño de valores:    {A_mezcla_tipos.size}

    - Tipo de objeto:       {type(A_mezcla_tipos)}

    - Tipo de valores num:  {A_mezcla_tipos.dtype}
    - Tipo de Array fila:   {A_mezcla_tipos[0].dtype}
    - Tipo de fila-valor 2: {type(A_mezcla_tipos[0][1])}
    
    - Tamaño de Array colum:    {A_mezcla_tipos[1].size}
    - Conte de valores reales:  {np.count_nonzero(A_mezcla_tipos[0])}

""")

print(f"""
- ACCESO A VALORES-ELEMENTOS INDIVIDUALES [x, y] vs [x][y]:

El acceso a valores es por [filas, columnas] -  También puede verse como [Numero de Array/Eje  - Valor]:

- PRIMERA FILA - PRIMERA COLUMNA [0, 0]:     {A[0, 0]}
- SEGUNDA FILA - TERCERA COLUMNA [1, 2]:     {A[1, 2]}
- SEGUNDA FILA ENTERA               [1]:     {A[1]}
- SEGUNDA COLUMNA ENTERA         [:, 1]      {A[:, 1]}

También se permite sintáxis de anidación de índices [][] para acceder a valoreS:

- PRIMERA FILA - PRIMERA COLUMNA [0][0]:     {A[0][0]}
- SEGUNDA FILA - TERCERA COLUMNA [1][2]:     {A[1][2]}
- SEGUNDA COLUMNA ENTERA         [:][1]      {A[:][1]}

""")

print(f"""
Ambas sintaxis funcionan igual SOLO para un elemento individual:

    - Usando sintaxis NumPy [fila, columna] -> A[0, 0]: {A[0, 0]}
    - Usando sintaxis anidada [fila][columna] -> A[0][0]: {A[0][0]}

    - Elemento segunda fila, tercera columna [1, 2]: {A[1, 2]}
    - Elemento segunda fila, tercera columna [1][2]: {A[1][2]}
""")


print(f"""
- ACCESO A FILAS-COLUMNAS COMPLETAS [x, y] vs [x][y] NO HACEN LO MISMO:

A) EXTRACCIÓN DE FILAS:
- Segunda fila entera usando índice directo [1]: {A[1]} 
  (Devuelve un array 1D de shape {A[1].shape})

B) EXTRACCIÓN DE COLUMNAS (La gran trampa):
- Correcto en NumPy [:, 1] (Todas las filas, columna 1):
    * Resultado: {A[:, 1]}
    * Shape: {A[:, 1].shape} (Pasa a ser unidimensional)

- PELIGROSO / INCORRECTO si buscabas columna con [:][1]:
    * Resultado: {A[:][1]}
    * Shape: {A[:][1].shape}
    * ¿Qué ha pasado?: 
        'A[:]' devuelve una copia/vista de toda la matriz completa, 
        y el segundo '[1]' coge la SEGUNDA FILA completa, ¡NO la columna!
""")



columna_colapsada = A[:, 1]
columna_preservada = A[:, [1] ]
print(f"""
- MANTENER LA ESTRUCTURA DE MATRIZ BIDIMENSIONAL - 2D:

Cuando extraes una columna con 'A[:, 1]', NumPy la colapsa a 1D (shape: {columna_colapsada.shape})

Si necesitas conservar la estructura de columna de tamaño (2x1), debes pasar una lista de índices:

- Usando A[ :, [COLUMNA] ]:
    * Resultado:\n{columna_preservada}
    * Nuevo Shape: {columna_preservada.shape}
    * Nuevo ndim: {columna_preservada.ndim}
""")


print(f"""
Cuando de una matriz se extrae una serie o valor, el tipo, dimensiones, shape, cambian
 - Si sacas una columna, no se mantiene como una "columna", sino como una serie

   - Tipo de la matriz  type(A):                     {type(A)}
        - Shape:                                     {A.shape}
        - Dimensiones:                               {A.ndim}

   - Tipo de la extracción de sus colimna A[:,1] :   {type(A[:, 1])} 
        - Shape:                                     {A[:, 1].shape}
        - Dimensiones:                               {A[:, 1].ndim}
         

   - Tipo de la extracción de sus colimna A[:][1] :   {type(A[:][1])} 
        - Shape:                                     {A[:][1].shape}
        - Dimensiones:                               {A[:][1].ndim}
""")

