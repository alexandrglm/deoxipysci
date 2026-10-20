import numpy as np

u = np.array([1, 2])
v = np.array([2, 4])

euclidea_u = np.linalg.norm(u, ord=2)
euclidea_v = np.linalg.norm(v, ord=2)

similitud_del_coseno = np.dot(u, v) / (euclidea_u * euclidea_v)
similitud_del_coseno_dos = u @ v / (euclidea_u * euclidea_v)

que_tan_similar = 1
print(
    np.isclose(
        similitud_del_coseno, que_tan_similar
    )
)


print(similitud_del_coseno)


## Version hiper-robusta para comparar similitud cosenos

class SimilitudCoseno:

    @staticmethod
    def calcula(u, v):

        u, v = np.asarray(u), np.asarray(v)
        # Metodo np.asarray(vector), parsea a vector, y puedes concatenarlo para generar tantos vectores como necesites
        # En esta función, sólo usas dos vectores unidimentsionales, de dos componentes cada uno

        if u is None or v is None or any(componente is None for componente in u) or any(componente is None for componente in v):
            return "Los vectores no pueden tener ninguna componente nula!"
        
        if u.shape != v.shape:
            
            return "Los vectores deben tener la misma len de componentes!"

        euclidea_u = np.linalg.norm(u, ord=2)
        # sum_cuadrados_v = np.sum( (v[0] **2 ) + (v[1] ** 2) )
        sum_cuadrados_v = np.sum(v ** 2)
        euclidea_v = np.sqrt(sum_cuadrados_v)

        denominador = euclidea_u * euclidea_v

        if denominador == 0:
            return None

        theta = u @ v / denominador

        return np.clip(theta, -1.0, 1.0)





print(SimilitudCoseno.calcula( [1, 2], [2, 4] ))
print(SimilitudCoseno.calcula( [4, 0], [4, 2] ))
print(SimilitudCoseno.calcula( [4, 0], [0, 4] ))
print(SimilitudCoseno.calcula( [4, 0], [-1, 3] ))
print(SimilitudCoseno.calcula( [9, 0], [-9, 0] ))
print(SimilitudCoseno.calcula( [9, 12, 12], [-9, 22] ))
print(SimilitudCoseno.calcula( [9, None], [-9, 22] ))