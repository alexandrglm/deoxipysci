# 2. Deconstruir numpy y statistics 
"""
def estadisticas(valores) que reciba una lista numérica 
y devuelva un diccionario con la media, el mínimo y el máximo,
y salvaguardas rapidas para [].
Después, ve a por la mediana, con distintas aproximaciones
"""


# MODE 1, legacy statistics
valores = [1,2,3,4,5,6]

print(valores)

# MEDIA - MEAN/AVERGAGE

import statistics

print(statistics.mean(valores))

# MIN
elMin = min(valores)
print(elMin)

# MAX
elMax = max(valores)
print(elMax)


# -------

# MODE 2, NUMPY
import numpy

print(numpy.mean(valores))
print(numpy.min(valores))
print(numpy.max(valores))

# AVERAGE
# MODO "QUE HACE NUMPY REALMENTE PARA EL AVG???",
#   functools, reduce ->  sum / total de indices
from functools import reduce
valores = [1,2,3,4,5,6]

def sacar_average(valores):

    total = reduce(

        (lambda total, valor: total + valor),
        valores

    )

    return total / len(valores)



print(sacar_average(valores))



# EJERCICIO

valoresVacios = []
def estadisticas(valores):

    if not valores:
        return {"Error" : "La lista está vacía y esta es la salvaguarda para no cortar la ejecución"}


    return {

        "min" : min(valores),
        "max" : max(valores),
        "avg" : sacar_average(valores)

    }

def estadisticasDeconstruidas(valores):

    if not valores:
        return {"Error" : "La lista está vacía y esta es la salvaguarda para no cortar la ejecución"}


    return {

        "min" : min(valores),
        "max" : max(valores),
        "avg deconst" : reduce(lambda total, valor: total + valor, valores)  /  len(valores) 

    }


print(estadisticas(valores))
print(estadisticas(valoresVacios))
print(estadisticasDeconstruidas(valores))


# ----
# MEDIANA

