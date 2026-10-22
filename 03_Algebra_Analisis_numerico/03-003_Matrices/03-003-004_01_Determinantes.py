import numpy as np

# np.set_printoptions(suppress=True, precision=4)
# np.linalg.det(matriz)

A = np.array([ [1, 2], [3, 4] ])
S = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
U = np.array([ [2, 1, 3], [0, 4, 1], [0, 0, 5] ])

determinante_A = np.linalg.det(A)


determinante_S = np.linalg.det(S)

determinante_U = np.linalg.det(U)



print(A)
print(determinante_A)
print(type(determinante_A))

print(S)
print(np.array(determinante_S))
print(type(determinante_S))

print(U)
print(determinante_U)
print(type(determinante_U))

print(determinante_A == -2)
print(np.isclose(determinante_A, -2))

print(determinante_S == 0)
print(np.isclose(determinante_S, 0))


# Al lorito con los tipos
print(np.linalg.det(A))
print(np.linalg.det(A.T))
print(np.linalg.det(A) == np.linalg.det(A.T))
print(np.isclose(np.linalg.det(A), np.linalg.det(A.T)))
