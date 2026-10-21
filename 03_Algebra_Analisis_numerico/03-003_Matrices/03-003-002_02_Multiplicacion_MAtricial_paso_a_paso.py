import numpy as np

# fila_A = int(input("Numero de FILAS de la matriz A? :"))
# col_A = int(input("Numero de COLUMNAS de la matriz A? :"))

# fila_B = int(input("Numero de FILAS de la matriz B? :"))
# col_A = int(input("Numero de COLUMNAS de la matriz B? :"))

"""
A = 3 * 2 -->   3 filas, cada una con 2 números
                    [ a11  a12 ]
                    [ a21  a22 ]
                    [ a31  a32 ]
                         ↑
                    2 columnas -> 2 valores por fila

"""
"""
NECESIDAD DE UN ESQUEMA MENTAL

                    B
              col0  col1  col2
            ┌─────┬─────┬─────┐
            │ 10  │ 20  │ 30  │
            ├─────┼─────┼─────┤
            │ 40  │ 50  │ 60  │
            └─────┴─────┴─────┘
              │     │     │
     A        │     │     │
   ┌─────┬───┼─────┼─────┼─────┐
   │     │   ↓     ↓     ↓     │
   │ 1  2│ 90   120   150      │  ← fila 0
   ├─────┼─────────────────────┤
   │ 3  4│ 190  260   330      │  ← fila 1
   ├─────┼─────────────────────┤
   │ 5  6│ 290  400   510      │  ← fila 2
   └─────┴─────────────────────┘
              C (3 * 3)
"""
class Matrices:

    @staticmethod
    def introduce_dimensiones():
        
        componentes_fila_A = int(input("Numero de FILAS de la matriz A? : "))
        componentes_col_A = int(input("Numero de COLUMNAS de la matriz A? : "))

        componentes_fila_B = int(input("Numero de FILAS de la matriz B? : "))
        componentes_col_B = int(input("Numero de COLUMNAS de la matriz B? : "))

        return (componentes_fila_A, componentes_col_A), (componentes_fila_B, componentes_col_B)

    @staticmethod
    def verifica(columnas_de_a, filas_de_b):

        cols_a_condicion = columnas_de_a.shape[1] if hasattr(columnas_de_a, 'shape') else columnas_de_a
        filas_b_condicion = filas_de_b.shape[0] if hasattr(filas_de_b, 'shape') else filas_de_b

        if cols_a_condicion != filas_b_condicion:

            print("NO SE PUEDE HACER MULTIPLICACIÓN MATRICIAL!")
            return False

        print("[OK] Las matrices son viables para multiplicación matricial!")
        return True

    @staticmethod
    def rellena_dimensiones(matriz, filas, columnas):

        filas_datos = []

        for posicion in range(filas):

            while True:

                try:

                    entrada = input(f"Matriz {matriz} - Fila {posicion}:  Introduce {columnas} valores: ")
                    valores = [ float( valor.strip() ) if '.' in valor.strip() else int( valor.strip() ) for valor in entrada.split(',')]
                    
                    if len(valores) != columnas:
                        
                        print(f"[ERROR] Has metido {len(valores)}, pero se esperaban {columnas}!")
                        continue


                    filas_datos.append(valores)
                    break

                except ValueError:
                    
                    print("Putísimo error porque no metiste números, tontopolla")

        return np.array(filas_datos)


    @staticmethod
    def genera():

        (componentes_fila_A, componentes_col_A), (componentes_fila_B, componentes_col_B) = Matrices.introduce_dimensiones()

        if not Matrices.verifica(componentes_col_A, componentes_fila_B):
            print("[ERROR] NO ES VIABLE!")
            return None, None

        matriz_A = Matrices.rellena_dimensiones("A", componentes_fila_A, componentes_col_A)
        matriz_B = Matrices.rellena_dimensiones("B", componentes_fila_B, componentes_col_B)

        print(f"""
        
- MATRICES GENERADAS (y verificadas):

  * Matriz A:     
{matriz_A}
    
  * Matriz_B:     
{matriz_B}

- Resultado de multiplicación matricial: 
{matriz_A @ matriz_B}

        """)

        return matriz_A, matriz_B




matriz_A, matriz_B = np.asmatrix([ [1, 2, 3], [4, 5, 6] ]), np.asmatrix([ [10, 20,], [30, 40], [50, 60] ])
matriz_A2, matriz_B2 = np.asmatrix([ [1, 2, None], [4, 5, 6] ]), np.asmatrix([ [10, 20,], [30, 40], [50, 60] ])
matriz_A3, matriz_B3 = np.asmatrix([ [1, 2, 3, 4], [4, 5, 6, 7] ]), np.asmatrix([ [10, 20,], [30, 40], [50, 60] ])
matriz_A4, matriz_B4 = np.asmatrix([ [1, 2, 3], [4, 5, 6] ]), np.asmatrix([ [10, 20,], [30, 40], [50, 60], [70, 80] ])

print(Matrices.verifica(matriz_A, matriz_B))
print(Matrices.verifica(matriz_A2, matriz_B2))
print(Matrices.verifica(matriz_A3, matriz_B3))
print(Matrices.verifica(matriz_A4, matriz_B4))

Matrices.genera()
