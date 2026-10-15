import numpy as np

heredoc = """
- Operaciones vectorizadas tìpicas

Al igual que las legacy o math's, NumPy tiene multitud, entre ellas:

Suma - np.sum(importes)
Media - np.mean(importes)
Mínimo - np.min(importes)
Máximo - np.max(importes)
Desviación típica - np.std(importes)
Raíz cuadrada - `np.sqrt(importes)`

"""
print(heredoc)

precios = np.array([20, 15, 12, 10])
unidades = np.array([3, 7, 2, 4])

importes = precios * unidades

print("- Trabajando con Arrays, podemos aplicar operaciones directamente SIN NECESIDAD DE BUCLES:\n")

print("\n - Importes: ", importes) 
# [ 60 105 24  40]
print("\n   Es MUY importante enteder que a diferencia de zip merges, el numero de valores en cada Array SIEMPRE DEBE COINCIDIR!")

print("\n - Suma de Importes /", importes, "/ : ", importes.sum()) 
# 229

print("\n - Media Aritrmética  /.mean()/  de Importes: ", importes.mean()) 
# 57.25


print(" - Aplicando IVA's, descuentos, directamente:\n")

precios_iva_21 = precios * 1.21
precios_dto_10 = precios * 0.90

iva_21 = 1.21
iva_10 = 0.10
dto_15 = 0.85
dto_50 = 0.50

precios_iva_21_dto_50 = (precios * iva_21) * dto_50
precios_dto_15_iva_10 = (precios * dto_15) * iva_10

print("  * Precios BASE :                 ", precios)
print("\n")
print("  * Precios con 21% IVA:           ", precios_iva_21)
print("  * Precios 21%IVA, luego 50%dto.: ", precios_iva_21_dto_50)
print("\n")
print("  * Precios BASE con 10% dto.:     ", precios_dto_10)
print("\n")
print("  * Precios 15%dto., luego 10%IVA: ", precios_dto_15_iva_10)


print("\n\n\n[LO IMPORTANTE]")
print("Usando Arrays, en OPERACIONES VECTORIZADAS, ...")
print(" ... NO NECESITAMOS USAR BUCLES ...")
print("... Podemos operar directamente sobre los valores del array")
