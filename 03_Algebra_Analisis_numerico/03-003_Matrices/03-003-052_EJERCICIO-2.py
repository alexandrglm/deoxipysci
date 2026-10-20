# EJERCICIO 2
import numpy as np

print(f"""
# Ejercicio 2. Indexación

Con la misma matriz, obtén el valor 4, la primera fila y la segunda columna.
""")

matriz = np.array([ 
    [1, 2], 
    [3, 4], 
    [5, 6] 
])

anidados = np.asarray( [matriz[0][1], matriz[1][1], matriz[2][1] ] )
heredoc_explica = f"""
    - Valor 4 con [][]:  {matriz[1][1]} 
    - Valor 4 con [x,y]: {matriz[1, 1]}

    - Primera fila, segunda columna:   {matriz[0, 1]}
    - Segunda columna:                 {matriz[:, 1]}

    - Segunda columna con [][][]:      {anidados}
            {matriz[:, 1] == anidados}
"""
print(heredoc_explica)