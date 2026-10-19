import math

import numpy as np

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Arc

    HAY_MATPLOTLIB = True
except ImportError:
    HAY_MATPLOTLIB = False


def _p(x):
    """Formatea un número; los negativos van entre paréntesis."""
    return f"({x})" if x < 0 else f"{x}"


class ParVectores:
    """Un par de vectores y todo lo que se deduce de ellos:
    producto escalar, normas, cos(θ), ángulo y tipo de ángulo."""

    ANCHO = 62
    COLORES = {
        "agudo": "tab:green",
        "obtuso": "tab:red",
        "perpendiculares": "tab:purple",
        "paralelos, misma dirección": "black",
        "paralelos, dirección opuesta": "black",
    }

    def __init__(self, u, v, nombre=""):
        self.nombre = nombre
        self.u = u
        self.v = v
        self.error = self._validar()
        if self.error is None:
            self.u = np.array(u)
            self.v = np.array(v)

    # ---------- validación ----------
    def _validar(self):
        if self.u is None or self.v is None:
            return "Uno de los vectores es nulo (None)."
        if any(c is None for c in self.u) or any(c is None for c in self.v):
            return "Alguna componente es nula (None)."
        if len(self.u) != len(self.v):
            return "Los vectores tienen distinta longitud."
        return None

    # ---------- cálculo ----------
    @property
    def producto_escalar(self):
        return self.u @ self.v

    @property
    def norma_u(self):
        return float(np.linalg.norm(self.u))

    @property
    def norma_v(self):
        return float(np.linalg.norm(self.v))

    @property
    def cos_theta(self):
        if self.norma_u == 0 or self.norma_v == 0:
            return None  # el vector cero no tiene dirección
        c = self.producto_escalar / (self.norma_u * self.norma_v)
        return float(np.clip(c, -1.0, 1.0))  # evita 1.0000000002 -> arccos = nan

    @property
    def theta(self):
        c = self.cos_theta
        return None if c is None else float(np.degrees(np.arccos(c)))

    @property
    def tipo(self):
        c = self.cos_theta
        if c is None:
            return "indefinido (hay un vector cero)"
        if np.isclose(c, 1):
            return "paralelos, misma dirección"
        if np.isclose(c, -1):
            return "paralelos, dirección opuesta"
        if np.isclose(self.producto_escalar, 0):
            return "perpendiculares"
        return "agudo" if self.producto_escalar > 0 else "obtuso"

    # ---------- consola ----------
    def _titulo(self):
        print("\n╔" + "═" * (self.ANCHO - 2) + "╗")
        print("║" + f" {self.nombre}".ljust(self.ANCHO - 2) + "║")
        print("╚" + "═" * (self.ANCHO - 2) + "╝")

    def _regla_angulo(self):
        """Regla de 0° a 180° con un marcador en el ángulo calculado."""
        ancho = 40
        regla = list("─" * (ancho + 1))
        for i in (0, 10, 20, 30, 40):
            regla[i] = "┼"
        regla[0], regla[ancho] = "├", "┤"

        etiquetas = "0°".ljust(10) + "45°".ljust(10) + "90°".ljust(10) + "135°".ljust(10) + "180°"
        zonas = "AGUDO (cos > 0)".center(20) + "│" + "OBTUSO (cos < 0)".center(20)
        pos = round(self.theta / 180 * ancho)
        marcador = " " * pos + "▲ " + f"θ = {self.theta:.1f}°"

        print("\n  ÁNGULO ENTRE LOS VECTORES")
        print("    " + etiquetas)
        print("    " + "".join(regla))
        print("    " + zonas)
        print("    " + marcador)

    def _regla_coseno(self):
        """Regla de -1 a +1 con un marcador en cos(θ)."""
        ancho = 40
        regla = list("─" * (ancho + 1))
        for i in (0, 20, 40):
            regla[i] = "┼"
        regla[0], regla[ancho] = "├", "┤"
        etiquetas = "-1".ljust(20) + "0".ljust(20) + "+1"
        pos = round((self.cos_theta + 1) / 2 * ancho)

        print("\n  COSENO (alineación: -1 opuestos, 0 perpendiculares, +1 misma dirección)")
        print("    " + etiquetas)
        print("    " + "".join(regla))
        print("    " + " " * pos + "▲ " + f"cos θ = {self.cos_theta:.3f}")

    def informe(self):
        self._titulo()
        if self.error is not None:
            print(f"\n  ✗ No se puede calcular: {self.error}")
            return

        print(f"\n  u = {self.u}      v = {self.v}\n")

        terminos = " + ".join(f"{_p(a)}·{_p(b)}" for a, b in zip(self.u, self.v))
        print(f"  Paso 1. Producto escalar:  u·v = {terminos} = {self.producto_escalar}")
        print(f"  Paso 2. Normas:            ‖u‖ = {self.norma_u:.4f}    ‖v‖ = {self.norma_v:.4f}")

        if self.cos_theta is None:
            print("\n  ✗ Con un vector cero no hay ángulo: no tiene dirección.")
            return

        print(f"  Paso 3. Coseno:            cos θ = {self.producto_escalar} / "
              f"({self.norma_u:.4f} · {self.norma_v:.4f}) = {self.cos_theta:.4f}")
        print(f"  Paso 4. Ángulo:            θ = arccos({self.cos_theta:.4f}) = {self.theta:.2f}°")
        print(f"\n  → Tipo de ángulo: {self.tipo.upper()}")

        self._regla_angulo()
        self._regla_coseno()

    # ---------- gráfico ----------
    def dibujar(self, ax):
        ax.set_aspect("equal")
        ax.axhline(0, color="gray", lw=0.8)
        ax.axvline(0, color="gray", lw=0.8)
        ax.grid(True, alpha=0.3)

        if self.error is not None or self.theta is None:
            motivo = self.error or "Vector cero: no hay ángulo"
            ax.set_title(f"{self.nombre}\n{motivo}", fontsize=9)
            ax.set_xlim(-1, 1)
            ax.set_ylim(-1, 1)
            return

        color = self.COLORES.get(self.tipo, "black")
        lim = max(np.abs(self.u).max(), np.abs(self.v).max()) * 1.4
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)

        for vec, etiqueta, c in ((self.u, "u", "tab:blue"), (self.v, "v", "tab:orange")):
            ax.annotate("", xy=tuple(vec), xytext=(0, 0),
                        arrowprops=dict(arrowstyle="-|>", color=c, lw=2))
            ax.text(vec[0] * 1.08, vec[1] * 1.08, etiqueta, color=c, fontsize=12, weight="bold")

        # arco del ángulo (siempre el menor, entre 0° y 180°)
        a1 = math.degrees(math.atan2(self.u[1], self.u[0]))
        a2 = math.degrees(math.atan2(self.v[1], self.v[0]))
        dif = (a2 - a1 + 180) % 360 - 180
        inicio = a1 if dif >= 0 else a2
        radio = lim * 0.3
        ax.add_patch(Arc((0, 0), 2 * radio, 2 * radio, theta1=inicio,
                         theta2=inicio + abs(dif), color=color, lw=2.5))
        medio = math.radians(inicio + abs(dif) / 2)
        ax.text(radio * 1.45 * math.cos(medio), radio * 1.45 * math.sin(medio),
                f"{self.theta:.1f}°", color=color, ha="center", va="center", weight="bold")

        ax.set_title(f"{self.nombre}: {self.tipo}\nu·v = {self.producto_escalar}", fontsize=9)


class Galeria:
    """Colección de pares: imprime los informes y dibuja todos juntos."""

    def __init__(self, pares):
        self.pares = pares

    def informes(self):
        for par in self.pares:
            par.informe()

    def dibujar(self, archivo="03-002_006_angulos.png"):
        if not HAY_MATPLOTLIB:
            print("\n(Instala matplotlib para ver el gráfico: pip install matplotlib)")
            return
        n = len(self.pares)
        cols = min(3, n)
        filas = math.ceil(n / cols)
        fig, ejes = plt.subplots(filas, cols, figsize=(4.5 * cols, 4.5 * filas))
        ejes = np.atleast_1d(ejes).ravel()
        for ax, par in zip(ejes, self.pares):
            par.dibujar(ax)
        for ax in ejes[n:]:
            ax.axis("off")
        fig.tight_layout()
        fig.savefig(archivo, dpi=150)
        print(f"\nGráfico guardado en {archivo}")
        plt.show()


if __name__ == "__main__":
    galeria = Galeria([
        ParVectores([1, 0], [0, 1], "Par 1"),
        ParVectores([7, 9], [-5, 3], "Par 2"),
        ParVectores([None, 3], [1, 4], "Par 3"),
        ParVectores([3, 1], [2, 2], "Par 4"),
        ParVectores([1, 0], [-2, 0], "Par 5"),
        ParVectores([0, 0], [1, 4], "Par 6"),
    ])
    galeria.informes()
    galeria.dibujar()