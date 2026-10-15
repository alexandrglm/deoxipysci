import numpy as np
import math

# .zeros(cuantos), rellenar de ceros
# .ones(cuantos), rellenar de unos
# .arrange(INICIO, FIN(pero NO añade el último), DeCuantosEnCuantos)
# .linspace(INICIO, FIN(incluido), RANGOS) - el LINEAR SPACE por RANGOS

cuantos = 4

ceros = np.zeros(cuantos)
unos = np.ones(cuantos)

secuencia_de_uno_en_uno = np.arange(0, 5, 1)
secuencia_dos_en_dos = np.arange(0, 10, 2)
secuencia_tres_en_tres = np.arange(0, 12, 3)
secuencia_de_pi_en_pi_xd = np.arange(0, 20, math.pi)

valores_lineales_recta = np.linspace(0, 1, 5)
valores_lineales_curva_1 = np.linspace(0, 7, 6)


print(ceros)      
# [0. 0. 0. 0.]

print(unos)       
# [1. 1. 1. 1.]


print("\n\n * .arange() - `np.arange(inicio, fin, paso)`\n  Genera valores separados por un paso determinado, sin incluir normalmente el límite final")
print(secuencia_de_uno_en_uno)
# [0 1 2 3 4] ... De cero a 5 ... DE UNO EN UNO
print(secuencia_dos_en_dos)  
# [0 2 4 6 8] ... De cero a 10 ... DE DOS EN DOS
print(secuencia_tres_en_tres)
# [0 3 6 9] ... De cero a 12 ... DE TRES EN TRES
print(secuencia_de_pi_en_pi_xd)
# [ 0.          3.14159265  6.28318531  9.42477796 12.56637061 15.70796327 [18.84955592] ... de PI en PI



print("\n\n * .linspace() - `np.linspace(inicio, fin, cantidad)`\n  Genera una cantidad concreta de valores espaciados uniformemente, incluyendo los extremos por defecto.")
print(valores_lineales_recta)    
# [0.   0.25 0.5  0.75 1.  ]
print(valores_lineales_curva_1)
# [0.  1.4 2.8 4.2 5.6 7. ]