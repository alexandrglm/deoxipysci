import numpy as np

try:
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle

    HAY_MATPLOTLIB = True

except ImportError:
    HAY_MATPLOTLIB = False


def _p(x):
    """Formatea un número; los negativos van entre paréntesis."""
    return f"({x})" if x < 0 else f"{x}"


class MultiplicacionMatricial:
    """Multiplica dos matrices celda a celda (cada celda es un producto escalar)
    y muestra el esquema de Falk en consola y en gráficos."""

    W = 7  # ancho de cada celda en consola
    AZUL, NARANJA, VERDE = "#ff563f", "#ffe5b4", "#a1f541"

    PASOS = {
        1: "PASO 1. B va arriba a la derecha",
        2: "PASO 2. A va abajo a la izquierda",
        3: "PASO 3. C se coloca en el cruce (su forma sale del dibujo)",
        4: "PASO 4. Cada celda = fila de A  *  columna de B",
    }

    def __init__(self, A, B):
        self.A = np.array(A)
        self.B = np.array(B)
        self._validar()
        self.m, self.n = self.A.shape
        self.p = self.B.shape[1]
        self.C = self._calcular()

    # ---------- validación y cálculo ----------
    def _validar(self):
        if self.A.ndim != 2 or self.B.ndim != 2:
            raise ValueError("A y B deben ser matrices (2 ejes).")
        if self.A.shape[1] != self.B.shape[0]:
            raise ValueError(
                f"No se puede calcular {self.A.shape} @ {self.B.shape}: "
                f"las columnas de A ({self.A.shape[1]}) deben coincidir "
                f"con las filas de B ({self.B.shape[0]})."
            )

    def _calcular(self):
        C = np.zeros((self.m, self.p), dtype=np.result_type(self.A, self.B))
        for i in range(self.m):
            for j in range(self.p):
                C[i, j] = self.A[i, :] @ self.B[:, j]  # un producto escalar por celda
        return C

    def terminos(self, i, j):
        """Desarrollo de C[i, j] como texto: 1*20 + 2*50"""
        return " + ".join(f"{_p(a)} * {_p(b)}" for a, b in zip(self.A[i, :], self.B[:, j]))

    # ---------- consola ----------
    def _celda(self, valor, tipo="normal"):
        s = str(valor)
        if tipo == "operando":
            return f"[{s:^5}]"
        if tipo == "resultado":
            return f"«{s:^5}»"
        return f" {s:^5} "

    def esquema(self, i=None, j=None, etapa=4):
        """
        Esquema de Falk: 
            B arriba a la derecha
            A abajo a la izquierda
            C en el cruce.
        
        etapa 1: solo B
        etapa 2: B y A
        etapa 3: C vacía
        etapa 4: C completa
        """
        w = self.W
        ancho_a = self.n * w
        sangria = ancho_a + 3
        total = sangria + self.p * w
        marcar = etapa >= 3 and i is not None

        titulo_a = f"A ({self.m}×{self.n})" if etapa >= 2 else ""
        print("\n" + titulo_a.ljust(sangria) + f"B ({self.n}×{self.p})")
        print(" " * sangria + "".join(f"col {c}".center(w) for c in range(self.p)))
        for k in range(self.n):
            fila = "".join(self._celda(self.B[k, c], "operando" if marcar and c == j else "normal")
                           for c in range(self.p))
            print(" " * sangria + fila)
        print("─" * (ancho_a + 1) + "┼" + "─" * (total - ancho_a - 2))

        for r in range(self.m):
            if etapa >= 2:
                izq = "".join(self._celda(self.A[r, c], "operando" if marcar and r == i else "normal")
                              for c in range(self.n))
            else:
                izq = " " * ancho_a
            if etapa < 3:
                der = ""
            else:
                celdas = []
                for c in range(self.p):
                    valor = self.C[r, c] if etapa == 4 else "?"
                    tipo = "resultado" if marcar and (r, c) == (i, j) else "normal"
                    celdas.append(self._celda(valor, tipo))
                der = "".join(celdas)
            print(f"{izq} │ {der}" + (f"  ← fila {r}" if etapa >= 2 else ""))
        if etapa >= 3:
            print(" " * sangria + f"C ({self.m}×{self.p})")
        if marcar:
            print(f"\n  [ ] fila {i} de A y columna {j} de B   « » celda C[{i}, {j}]")

    def construccion(self, i, j):
        """Imprime el esquema de Falk construyéndose paso a paso."""
        for etapa in (1, 2, 3, 4):
            print("\n" + "=" * 62)
            print(f"  {self.PASOS[etapa]}")
            print("=" * 62)
            self.esquema(i, j, etapa)
        self.detalle_celda(i, j)

    def detalle_celda(self, i, j):
        print(f"\n  Fila {i} de A:     {self.A[i, :]}")
        print(f"  Columna {j} de B:  {self.B[:, j]}")
        print(f"  C[{i}, {j}] = {self.terminos(i, j)} = {self.C[i, j]}")

    def tabla_celdas(self):
        print(f"\n  LAS {self.m * self.p} CELDAS DE C ({self.m}×{self.p}), "
              f"cada una con {self.n} productos:\n")
        for i in range(self.m):
            for j in range(self.p):
                print(f"  C[{i}, {j}] = {self.terminos(i, j):<24} = {self.C[i, j]}")

    def verificar(self):
        directo = self.A @ self.B
        print("\n  Manual:\n" + str(self.C))
        print("  A @ B:\n" + str(directo))
        print(f"  ¿Coinciden?: {np.array_equal(self.C, directo)}")

    # ---------- gráficos ----------
    def _pintar(self, ax, i, j, etapa=4, titulo=None, pie=None):
        gap = 1
        x_b = self.n + gap
        y_a = self.n + gap
        resaltar = etapa >= 3

        def celda(x, y, texto, fondo, negrita, color="black"):
            ax.add_patch(Rectangle((x, y), 1, 1, facecolor=fondo, edgecolor="black", lw=1))
            ax.text(x + 0.5, y + 0.5, str(texto), ha="center", va="center", fontsize=13,
                    weight="bold" if negrita else "normal", color=color)

        for r in range(self.n):                              # matriz B (siempre)
            for c in range(self.p):
                en_col = resaltar and c == j
                celda(x_b + c, r, self.B[r, c], self.NARANJA if en_col else "white", en_col)

        if etapa >= 2:                                       # matriz A
            for r in range(self.m):
                for c in range(self.n):
                    en_fila = resaltar and r == i
                    celda(c, y_a + r, self.A[r, c], self.AZUL if en_fila else "white", en_fila)

        if etapa >= 3:                                       # matriz C
            for r in range(self.m):
                for c in range(self.p):
                    if (r, c) == (i, j):
                        fondo, negrita = self.VERDE, True
                    elif r == i:
                        fondo, negrita = self.AZUL, False
                    elif c == j:
                        fondo, negrita = self.NARANJA, False
                    else:
                        fondo, negrita = "white", False
                    texto = self.C[r, c] if etapa == 4 else "?"
                    gris = "gray" if etapa == 3 and (r, c) != (i, j) else "black"
                    celda(x_b + c, y_a + r, texto, fondo, negrita, gris)

        ax.text(x_b + self.p / 2, -1.0, f"B ({self.n}×{self.p})", ha="center", weight="bold")
        for c in range(self.p):
            ax.text(x_b + c + 0.5, -0.3, f"col {c}", ha="center", fontsize=8, color="gray")
        if etapa >= 2:
            ax.text(self.n / 2, y_a - 0.3, f"A ({self.m}×{self.n})", ha="center", weight="bold")
            for r in range(self.m):
                ax.text(-0.25, y_a + r + 0.5, f"fila {r}", ha="right", va="center",
                        fontsize=8, color="gray")
        if etapa >= 3:
            ax.text(x_b + self.p / 2, y_a + self.m + 0.45, f"C ({self.m}×{self.p})",
                    ha="center", weight="bold")
        if pie:
            ax.text((x_b + self.p) / 2, y_a + self.m + 1.4, pie, ha="center", fontsize=12,
                    weight="bold", color="darkgreen")
        if titulo:
            ax.set_title(titulo, fontsize=11, pad=8)

        ax.set_xlim(-1.6, x_b + self.p + 0.3)
        ax.set_ylim(y_a + self.m + 2, -1.5)
        ax.set_aspect("equal")
        ax.axis("off")

    def dibujar(self, i, j, archivo="03-003_multiplicacion.png"):
        """Una sola figura: el esquema de Falk completo con la celda (i, j) resaltada."""
        if not HAY_MATPLOTLIB:
            print("\n(Instala matplotlib para ver el gráfico: pip install matplotlib)")
            return
        fig, ax = plt.subplots(figsize=(1.1 * (self.n + self.p + 2), 1.1 * (self.n + self.m + 3)))
        pie = f"C[{i}, {j}] = {self.terminos(i, j)} = {self.C[i, j]}"
        self._pintar(ax, i, j, etapa=4, pie=pie)
        fig.savefig(archivo, dpi=150, bbox_inches="tight")
        print(f"Gráfico guardado en {archivo}")

    def dibujar_construccion(self, i, j, archivo="03-003_falk_construccion.png"):
        """Cuatro paneles: el esquema de Falk construyéndose paso a paso."""
        if not HAY_MATPLOTLIB:
            print("\n(Instala matplotlib para ver el gráfico: pip install matplotlib)")
            return
        ancho = 1.0 * (self.n + self.p + 3)
        alto = 1.0 * (self.n + self.m + 4)
        fig, ejes = plt.subplots(2, 2, figsize=(2 * ancho, 2 * alto))
        titulos = {1: "1. B arriba a la derecha", 2: "2. A abajo a la izquierda",
                   3: f"3. C en el cruce: {self.m}×{self.p}", 4: "4. Celda = fila * columna"}
        pie = f"C[{i}, {j}] = {self.terminos(i, j)} = {self.C[i, j]}"
        for etapa, ax in zip((1, 2, 3, 4), ejes.ravel()):
            self._pintar(ax, i, j, etapa, titulo=titulos[etapa], pie=pie if etapa == 4 else None)
        fig.tight_layout()
        fig.savefig(archivo, dpi=150, bbox_inches="tight")
        print(f"Gráfico guardado en {archivo}")


if __name__ == "__main__":
    # ---- EJEMPLO 1: el mínimo, 2×2 con números distintos ----
    mini = MultiplicacionMatricial([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    mini.construccion(0, 1)
    mini.tabla_celdas()
    mini.verificar()
    mini.dibujar_construccion(0, 1, "03-003_falk_construccion.png")

    # ---- EJEMPLO 2: 3×2 por 2×3 (la forma importa) ----
    grande = MultiplicacionMatricial([[1, 2], [3, 4], [5, 6]],
                                     [[10, 20, 30], [40, 50, 60]])
    grande.esquema(1, 2)
    grande.detalle_celda(1, 2)
    grande.tabla_celdas()
    grande.verificar()
    grande.dibujar(1, 2, "03-003_multiplicacion.png")

    # ---- ERROR DE FORMA ----
    print("\n  ERROR DE FORMA:")
    try:
        MultiplicacionMatricial([[10, 20, 30], [40, 50, 60]], [[10, 20, 30], [40, 50, 60]])
    except ValueError as error:
        print(f"  ValueError: {error}")

    if HAY_MATPLOTLIB:
        plt.show()