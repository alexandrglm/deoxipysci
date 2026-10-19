# import numpy as np

# heredoc = """
# | Norma            | Fórmula                       |
# | ---------------- | ----------------------------- |
# | L1               | Suma de los valores absolutos |
# | L2 o Euclidea    | Raíz de la suma de cuadrados  |
# | L∞               | Máximo valor absoluto         |
# """
# print(heredoc)

# vector = np.array([3, -4])
# infinito = np.inf

# norma_L1 = np.linalg.norm(vector, ord=1)
# norma_L2 = np.linalg.norm(vector, ord=2)
# L2_lo_mismo_euclidea = np.linalg.norm(vector)
# norma_L_inf = np.linalg.norm(vector, ord=infinito)

# print(norma_L1)
# print(norma_L2)
# print(L2_lo_mismo_euclidea)
# print(norma_L_inf)


# EXPLICADO SUPERVISUALMENTE EN CONSOLA
import numpy as np


class DescomposicionNormas:
    """Deconstruye L1, L2 y L∞ paso a paso y las compara con np.linalg.norm."""

    ANCHO = 60

    def __init__(self, vector):
        self.vector = np.array(vector)
        self.absolutos = np.abs(self.vector)

    def _titulo(self, texto):
        print("\n╔" + "═" * (self.ANCHO - 2) + "╗")
        print("║" + texto.center(self.ANCHO - 2) + "║")
        print("╚" + "═" * (self.ANCHO - 2) + "╝")

    def _barras(self, marcar=None):
        maximo = self.absolutos.max()
        escala = 1 if maximo <= 20 else 20 / maximo
        for i, (v, a) in enumerate(zip(self.vector, self.absolutos), start=1):
            barra = "█" * round(a * escala)
            marca = "  ◄ máximo" if marcar == i - 1 else ""
            print(f"    v{i} = {v:>4}  →  |v{i}| = {a:<4} {barra}{marca}")

    def _comparar(self, manual, directo):
        print(f"\n  Manual:           {manual}")
        print(f"  np.linalg.norm(): {directo}")
        print(f"  ¿Coinciden?:      {np.isclose(manual, directo)}")

    def l1(self):
        self._titulo("L1  ·  Suma de valores absolutos")
        print(f"\n  Vector: {self.vector}\n")
        print("  Paso 1. Valor absoluto de cada componente:")
        self._barras()

        suma = np.sum(self.absolutos)
        terminos = " + ".join(str(a) for a in self.absolutos)
        print(f"\n  Paso 2. Sumarlos: {terminos} = {suma}")

        self._comparar(suma, np.linalg.norm(self.vector, ord=1))

    def l2(self):
        self._titulo("L2  ·  Raíz de la suma de cuadrados")
        print(f"\n  Vector: {self.vector}\n")

        cuadrados = self.vector ** 2
        print("  Paso 1. Cada componente al cuadrado (el signo desaparece):")
        for i, (v, c) in enumerate(zip(self.vector, cuadrados), start=1):
            print(f"    ({v})² = {c}")

        suma = np.sum(cuadrados)
        terminos = " + ".join(str(c) for c in cuadrados)
        print(f"\n  Paso 2. Sumarlos: {terminos} = {suma}")

        raiz = np.sqrt(suma)
        print(f"\n  Paso 3. Raíz cuadrada: √{suma} = {raiz}")

        self._comparar(raiz, np.linalg.norm(self.vector, ord=2))
        print(f"  Sin ord (por defecto): {np.linalg.norm(self.vector)}  → es la L2")

    def l_inf(self):
        self._titulo("L∞  ·  Máximo valor absoluto")
        print(f"\n  Vector: {self.vector}\n")
        print("  Paso 1. Valor absoluto de cada componente:")
        posicion = int(np.argmax(self.absolutos))
        self._barras(marcar=posicion)

        maximo = np.max(self.absolutos)
        lista = ", ".join(str(a) for a in self.absolutos)
        print(f"\n  Paso 2. Quedarse con el mayor: max({lista}) = {maximo}")

        infinito = np.inf
        print(f"\n  ord=np.inf  →  tipo: {type(infinito).__name__}, valor: {infinito}")
        print(f"  ¿10**100 < np.inf?: {10 ** 100 < infinito}")

        self._comparar(maximo, np.linalg.norm(self.vector, ord=infinito))

    def resumen(self):
        self._titulo("RESUMEN")
        print(f"\n  Vector: {self.vector}\n")
        print("  ┌────────┬───────────┐")
        print("  │ Norma  │ Resultado │")
        print("  ├────────┼───────────┤")
        for nombre, orden in (("L1", 1), ("L2", 2), ("L∞", np.inf)):
            valor = np.linalg.norm(self.vector, ord=orden)
            print(f"  │ {nombre:<6} │ {valor:>9} │")
        print("  └────────┴───────────┘")

    def ejecutar(self):
        self.l1()
        self.l2()
        self.l_inf()
        self.resumen()


if __name__ == "__main__":
    DescomposicionNormas([3, -4]).ejecutar()