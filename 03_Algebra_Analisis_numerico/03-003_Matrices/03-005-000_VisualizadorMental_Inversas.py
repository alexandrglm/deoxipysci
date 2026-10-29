import os
import textwrap

import numpy as np

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    HAY_MATPLOTLIB = True
except ImportError:
    HAY_MATPLOTLIB = False



class TransformacionCuadrado:
    """Aplica una matriz 2*2 al cuadrado unidad y dibuja el resultado.
    Si la matriz es regular, A⁻¹ devuelve cada punto a su sitio; si es singular, no."""

    CUADRADO = np.array([[0, 0], [1, 0], [1, 1], [0, 1]]).T  # vértices como columnas

    def __init__(self, A):
        self.A = np.array(A, dtype=float)

    @property
    def det(self):
        return float(np.linalg.det(self.A))

    @property
    def es_regular(self):
        return not np.isclose(self.det, 0)

    def imagen(self):
        """Vértices del cuadrado unidad tras aplicar A."""
        return self.A @ self.CUADRADO

    def _ejes(self, ax, puntos, titulo, nota=None):
        ax.axhline(0, color="gray", lw=0.8)
        ax.axvline(0, color="gray", lw=0.8)
        ax.grid(True, alpha=0.3)
        ax.set_aspect("equal")
        ax.set_xlim(min(-0.5, puntos[0].min() - 0.5), puntos[0].max() + 0.5)
        ax.set_ylim(min(-0.5, puntos[1].min() - 0.5), puntos[1].max() + 0.5)
        ax.set_title(titulo, fontsize=10)
        if nota:
            ax.set_xlabel(textwrap.fill(nota, 38), fontsize=8)

    def panel_cuadrado(self, ax):
        v = self.CUADRADO
        ax.add_patch(Polygon(v.T, closed=True, facecolor="tab:blue", alpha=0.25, edgecolor="tab:blue", lw=1.5))
        for vec, c, et in (((1, 0), "tab:blue", "e1=(1, 0)"), ((0, 1), "tab:orange", "e2=(0, 1)")):
            ax.annotate("", xy=vec, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2.5))
            ax.text(vec[0] + 0.05, vec[1] + 0.05, et, color=c, weight="bold", fontsize=9)
        self._ejes(ax, np.hstack([v, self.imagen()]), "1. Cuadrado unidad (área 1)")

    def panel_tras_A(self, ax):
        img = self.imagen()
        ax.add_patch(Polygon(img.T, closed=True, facecolor="tab:green", alpha=0.25, edgecolor="tab:green", lw=1.5))
        for k, (c, et) in enumerate((("tab:blue", "A·e1"), ("tab:orange", "A·e2"))):
            col = self.A[:, k]
            ax.annotate("", xy=tuple(col), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=2.5))
            ax.text(col[0] + 0.05, col[1] + 0.05, f"{et}={tuple(int(x) for x in col)}", color=c, weight="bold", fontsize=9)
        self._ejes(ax, np.hstack([self.CUADRADO, img]),
                   f"2. Tras aplicar A: área = |det(A)| = {abs(self.det):.0f}",
                   "Las columnas de A son las imágenes de e1 y e2")

    def panel_vuelta(self, ax):
        img = self.imagen()
        inv = np.linalg.inv(self.A)
        vuelta = inv @ img  # debe recuperar el cuadrado unidad
        ax.add_patch(Polygon(img.T, closed=True, facecolor="none", edgecolor="tab:green", lw=1.5, ls="--"))
        ax.add_patch(Polygon(vuelta.T, closed=True, facecolor="tab:blue", alpha=0.25, edgecolor="tab:blue", lw=2))
        self._ejes(ax, np.hstack([self.CUADRADO, img]),
                   f"3. Tras aplicar A⁻¹: vuelve al cuadrado (área {abs(np.linalg.det(inv) * self.det):.0f})",
                   f"det(A⁻¹) = 1/det(A) = {1 / self.det:.1f}: el área pasa de {abs(self.det):.0f} a 1")

    def panel_singular(self, ax):
        img = self.imagen()
        extremos = img[:, [0, np.argmax(np.linalg.norm(img, axis=0))]]
        ax.plot(extremos[0], extremos[1], color="tab:red", lw=5, alpha=0.5, solid_capstyle="round")
        punto = self.A @ np.array([1, 0])
        ax.plot(*punto, "o", color="black", ms=8)
        ax.annotate("(1, 0) y (0, 0.5)\nllegan al mismo punto", xy=tuple(punto), xytext=(punto[0] + 0.7, punto[1] - 1.6),
                    arrowprops=dict(arrowstyle="->"), fontsize=9)
        self._ejes(ax, np.hstack([self.CUADRADO, img]),
                   f"4. Matriz singular (det = {self.det:.0f}): el cuadrado se aplasta",
                   "Dos puntos distintos acaban en el mismo sitio: no hay forma de saber de cuál venían")


class Galeria:
    def __init__(self, regular, singular):
        self.regular = TransformacionCuadrado(regular)
        self.singular = TransformacionCuadrado(singular)

    def informe(self):
        for nombre, t in (("REGULAR", self.regular), ("SINGULAR", self.singular)):
            print(f"\n  {nombre}: A = {t.A.tolist()}   det = {t.det:.2f}")
            if t.es_regular:
                print(f"  A⁻¹ = {np.linalg.inv(t.A).tolist()}   det(A⁻¹) = {np.linalg.det(np.linalg.inv(t.A)):.2f}")
            else:
                print("  No existe A⁻¹")

    def dibujar(self, archivo="img/03-005_inversa.png"):
        if not HAY_MATPLOTLIB:
            print("\n(Instala matplotlib para ver el gráfico: pip install matplotlib)")
            return
        os.makedirs(os.path.dirname(archivo) or ".", exist_ok=True)
        fig, ejes = plt.subplots(2, 2, figsize=(10, 9))
        self.regular.panel_cuadrado(ejes[0, 0])
        self.regular.panel_tras_A(ejes[0, 1])
        self.regular.panel_vuelta(ejes[1, 0])
        self.singular.panel_singular(ejes[1, 1])
        fig.tight_layout()
        fig.savefig(archivo, dpi=150, bbox_inches="tight")
        print(f"\nGráfico guardado en {archivo}")
        plt.show()


if __name__ == "__main__":
    galeria = Galeria(regular=[[2, 1], [0, 1]], singular=[[1, 2], [2, 4]])
    galeria.informe()
    galeria.dibujar()