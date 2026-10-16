import numpy as np


importes = np.array([60, 105, 24, 40])

print(importes[0])     
# 60

print(importes[-1])
# 40

print(importes[1:3])
# [105  24]


#
importes = np.array([60, 105, 24, 40])
mas_de_50 = importes > 50

print("\n Indexacion booleana:  ", mas_de_50)
# [ True  True False False]

print(importes[mas_de_50])
# [ 60 105]


print(importes[importes > 50])
# [ 60 105]

importes = np.array([60, 105, 24, 40])
descuentos = np.array([15, 20, 50])

print(importes[(importes >= 40) & (importes < 100)])
# [60 40]
