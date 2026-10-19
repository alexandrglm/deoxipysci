import numpy as np

u = np.array([1, 0])
v = np.array([0, 1])

u_2 = np.array([7, 9])
v_2 = np.array([-5, 3])

u_3 = np.array([None, 3])
v_3 = np.array([1, 4])

def producto_escalar(u, v):

    if (u is None) or (v is None) or any(componente is None for componente in u) or any(componente is None for componente in v):
        return "Uno de los vectores, o alguna de sus componenes, es nulo!"
    
    return f"Producto escalar de vectores {u} y {v} es:  {u @ v}"


print(producto_escalar(u, v))
print(producto_escalar(u_2, v_2))
print(producto_escalar(u_3, v_3))

#

u_4 = np.array([7, 9])
v_4 = np.array([-5, 3])



coseno_theta = (u @ v) / ( np.linalg.norm(u_4) * np.linalg.norm(v_4) )
print(f"\nCoseno Theta es... \n  1. El producto escalar de los vectores {u_4} y {v_4} (u @ v)\n  2. Divido entre la norma (euclídea L2) de uno POR la del otro vector")

theta = np.degrees( np.arccos( np.clip( coseno_theta, -1, 1 ) ) )

print("Coseno angular: ", coseno_theta)
print("Tipo de ángulo: ", theta)