import numpy as np

# PARTE 1, usar los métodos vstack, hstack y delete citados


A = np.array([ [1, 2], [3, 4] ])
P = np.array([ [2, 0, 1], [1, 3, 2], [1, 1, 4] ])
S = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
U = np.array([ [2, 1, 3], [0, 4, 1], [0, 0, 5] ])


M = np.array([[10, 2, 3], [4, 5, 6]])

print(M)
M = np.vstack( ( M, np.ones(3, dtype=int) ) )
print(M)
M = np.vstack( ( M, np.zeros(3, dtype=int) ) )
print(M)
M = np.delete(M, 3, axis=0)
print(M)
M = np.delete(M, -1, axis=0)
print(M)


# PARTE 2, replicar Laplace en python
class DeterminanteManual:

    def calcular(matriz):

        matriz = np.asarray(matriz)

        matriz.ndim

        condicion_dim = matriz.ndim != 2
        condicion_cuadrada = matriz.shape[0] != matriz.shape[1]
        
        if condicion_dim:
            False
            return("No es viable la matriz NO es bidimensional!")
        if condicion_cuadrada:
            False
            return("No es viable, la matriz NO es cuadrada!")

        if True:

            n = matriz.shape[0]
            
            if n == 1:

                return matriz[0, 0]

            if n == 2:    

                return matriz[1, 1] * matriz[0, 1] - matriz[1, 0] * matriz[1, 0]
                # ab cd ad cb
            

            total = 0

            for j in range(n):

                menor = np.delete( ( np.delete(matriz, 0, axis=0) ), j, axis=1 )
                signo = ( -1 ) ** j
                total += signo * matriz[0, j] * DeterminanteManual.calcular(menor)


            return total


print(DeterminanteManual.calcular(A))
print(DeterminanteManual.calcular(P))
print(DeterminanteManual.calcular(S))
print(DeterminanteManual.calcular(U))
print(DeterminanteManual.calcular(M))
