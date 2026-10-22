import math
import os
import textwrap

import numpy as np

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Arc, Polygon

    HAY_MATPLOTLIB = True
except ImportError:
    HAY_MATPLOTLIB = False


class ParalelogramaDeterminante:
    """Una matriz 2×2 vista como dos vectores (sus columnas) y el paralelogramo
    que forman: su área es |det(A)| y el sentido de giro u -> v da el signo."""

    def __init__(self, A, nombre=""):
        self.A = np.array(A)
        if self.A.shape != (2, 2):
            raise ValueError("Solo se dibujan matrices 2×2.")
        self.nombre = nombre
        self.u = self.A[:, 0]  # primera columna
        self.v = self.A[:, 1]  # segunda columna

    @property
    def det(self):
        return float(np.linalg.det(self.A))

    @property
    def tipo(self):
        if np.isclose(self.det, 0):
            return "det = 0: los vectores quedan alineados (área 0)"
        if self.det > 0:
            return "det > 0: u → v gira en sentido antihorario"
        return "det < 0: u → v gira en sentido horario"

    def informe(self):
        a, b, c, d = self.A[0, 0], self.A[0, 1], self.A[1, 0], self.A[1, 1]
        print(f"\n  {self.nombre}")
        print(f"  A = {self.A.tolist()}   u = {self.u.tolist()}   v = {self.v.tolist()}")
        print(f"  det(A) = {a}·{d} - {b}·{c} = {a * d - b * c}")
        print(f"  Área del paralelogramo = |det| = {abs(a * d - b * c)}")
        print(f"  {self.tipo}")

    def dibujar(self, ax):
        det = self.det
        color = "gray" if np.isclose(det, 0) else ("tab:green" if det > 0 else "tab:red")

        puntos = [(0, 0), tuple(self.u), tuple(self.u + self.v), tuple(self.v)]
        ax.add_patch(Polygon(puntos, closed=True, facecolor=color, alpha=0.25,
                             edgecolor=color, lw=1.5))

        for vec, etiqueta, c in ((self.u, "u", "tab:blue"), (self.v, "v", "tab:orange")):
            ax.annotate("", xy=tuple(vec), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=c, lw=2.5))
            ax.text(vec[0] * 1.07, vec[1] * 1.07, f"{etiqueta}={tuple(int(x) for x in vec)}",
                    color=c, weight="bold", fontsize=10)

        if not np.isclose(det, 0):  # arco que va de u a v
            a1 = math.degrees(math.atan2(self.u[1], self.u[0]))
            a2 = math.degrees(math.atan2(self.v[1], self.v[0]))
            dif = (a2 - a1 + 180) % 360 - 180
            inicio = a1 if dif >= 0 else a2
            radio = 0.35 * min(np.linalg.norm(self.u), np.linalg.norm(self.v))
            ax.add_patch(Arc((0, 0), 2 * radio, 2 * radio, theta1=inicio,
                             theta2=inicio + abs(dif), color=color, lw=2.5))

        extremos = np.array(puntos)
        margen = 0.8
        ax.set_xlim(min(-0.5, extremos[:, 0].min() - margen), extremos[:, 0].max() + margen)
        ax.set_ylim(min(-0.5, extremos[:, 1].min() - margen), extremos[:, 1].max() + margen)
        ax.set_aspect("equal")
        ax.axhline(0, color="gray", lw=0.8)
        ax.axvline(0, color="gray", lw=0.8)
        ax.grid(True, alpha=0.3)
        ax.set_title(f"A = {self.A.tolist()}\ndet(A) = {det:.0f}  ·  área = {abs(det):.0f}",
                     fontsize=10)
        ax.set_xlabel(textwrap.fill(self.tipo, 34), fontsize=8)


class Galeria:
    def __init__(self, pares):
        self.pares = pares

    def informes(self):
        for par in self.pares:
            par.informe()

    def dibujar(self, archivo="img/03-004_determinante.png"):
        if not HAY_MATPLOTLIB:
            print("\n(Instala matplotlib para ver el gráfico: pip install matplotlib)")
            return
        os.makedirs(os.path.dirname(archivo) or ".", exist_ok=True)
        fig, ejes = plt.subplots(1, len(self.pares), figsize=(5 * len(self.pares), 5))
        for ax, par in zip(np.atleast_1d(ejes), self.pares):
            par.dibujar(ax)
        fig.tight_layout()
        fig.savefig(archivo, dpi=150, bbox_inches="tight")
        print(f"\nGráfico guardado en {archivo}")
        plt.show()


if __name__ == "__main__":
    galeria = Galeria([
        ParalelogramaDeterminante([[2, 1], [0, 3]], "Caso 1: det positivo"),
        ParalelogramaDeterminante([[1, 2], [3, 0]], "Caso 2: columnas intercambiadas: misma área, signo opuesto"),
        ParalelogramaDeterminante([[1, 2], [2, 4]], "Caso 3: det cero"),
    ])
    galeria.informes()
    galeria.dibujar()
