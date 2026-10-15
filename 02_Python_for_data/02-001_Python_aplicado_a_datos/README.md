
## Bloque 1. Python aplicado a datos


## Qué debes dominar antes de pasar a NumPy

- Diferenciar transformación (`map`), combinación (`zip`) y filtrado o transformación mediante comprensiones.
- Saber cuándo utilizar `sum()`, `min()`, `max()` y `len()`.
- Entender que las listas de Python pueden contener estructuras complejas, como diccionarios.
- Elegir la herramienta más legible, sin complicar el código innecesariamente.

AL terminar, pasaremos a NumPy, donde veremos por qué los arrays son fundamentales para el análisis numérico y el aprendizaje automático.

---


### 1.1. Preparar el entorno

Como trabajas en Linux con VS Code, abre un terminal y ejecuta:

```bash
python3 --version
python3 -m pip --version
```

Si ya tienes NumPy y pandas instalados en el entorno de Python que vas a utilizar, no necesitas reinstalarlos. Puedes comprobarlo con:

```bash
python3 -c "import numpy, pandas; print(numpy.__version__); print(pandas.__version__)"
```

Si faltan, crea un venv dentro de la carpeta de estudio:

```bash
mkdir -p ~/estudio-ia/dia2
cd ~/estudio-ia/dia2

python3 -m venv .venv
source .venv/bin/activate

python -m pip install numpy pandas
```

En VS Code, selecciona como intérprete el Python de `dia2/.venv`. Así evitas mezclar las dependencias de distintos proyectos.

---


### 1.2. Repaso dirigido: transformar datos

Vamos a reutilizar un escenario usado: productos con precio y unidades vendidas.

```python
ventas = [
    {"producto": "A", "precio": 20, "unidades": 3},
    {"producto": "B", "precio": 15, "unidades": 7},
    {"producto": "C", "precio": 12, "unidades": 2},
    {"producto": "D", "precio": 10, "unidades": 4}
]
```

El objetivo es calcular el importe de cada venta: precio multiplicado por unidades.

```python
importes = [    
    venta["precio"] * venta["unidades"]    
    for venta in ventas
]

print(importes)
# [60, 105, 24, 40]
```

El total es:

```python
total = sum(importes)

print(total)  
# 229
```

> [!IMPORTANT]
> Fíjate en que `sum()` ya resuelve la acumulación. Para este caso, no necesitamos `reduce()`.

---

### 1.3. `map()`, `zip()` y List Comprehesion

Son herramientas que conviene distinguir, porque pueden resolver problemas parecidos, pero no hacen lo mismo.

* `map()` -->  **aplicar una transformación a cada elemento**

```python
precios = [20, 15, 12, 10]

resultado = map(lambda precio: precio * 1.21, precios)

print(list(resultado))
# [24.2, 18.15, 14.52, 12.1]
```

- `map()` devuelve un iterador, no una lista. 
- Por eso usamos `list()` para ver todos sus resultados.


* La misma operación con comprensión de listas:  

```python
resultado = [precio * 1.21 for precio in precios]
```
    - Para transformaciones sencillas, la comprensión suele ser más legible.


- `zip()` -->  **combinar elementos de varias secuencias por posición**

```python
productos = ["A", "B", "C"]
importes = [60, 105, 24]

print(list(zip(productos, importes)))
# [('A', 60), ('B', 105), ('C', 24)]
```

En cada pareja, el primer elemento procede de `productos` y el segundo de `importes`.  
Por defecto, `zip()` se detiene cuando se agota la secuencia más corta.

---

- Comprensión de listas -->  **transformar y, opcionalmente, filtrar**

```python
numeros = [1, 2, 3, 4, 5, 6]

cuadrados_pares = [    x**2 for x in numeros    if x % 2 == 0]
print(cuadrados_pares)
# [4, 16, 36]
```


---



