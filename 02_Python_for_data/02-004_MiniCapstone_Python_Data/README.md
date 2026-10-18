# Bloque 2.4:   Mini proyecto integrador

- OBJETIVO: **Elegir la herramienta adecuada y justificar esa elección.**

---

## 1. Escenario

Trabajas con un conjunto de registros de operaciones de una empresa. Cada fila representa una operación registrada, con su categoría, región, precio unitario y unidades.

En este caso utilizaremos un DataFrame construido en memoria. Más adelante, el mismo flujo podrá adaptarse a un CSV, una API o una base de datos.

```python
datos = {
    "id": [101, 102, 103, 104, 105, 106, 107, 108],
    "categoria": [
        "Hardware", "Software", "Hardware", "Software", "Hardware", "Software", "Hardware", "Software"
    ],
    "region": [
        "Norte", "Sur", "Norte", "Este", "Sur", "Norte", "Este", "Sur"
    ],
    "precio": [120, 80, 150, 100, 90, 200, 110, 80],
    "unidades": [2, 5, 1, 3, 4, 2, 3, 6]
}
```

> [!INFO] 
> Conexión con ETL 
>  
> - Extract: en este ejercicio, los datos ya están disponibles en Python; no necesitamos leer un fichero.  
> - Transform: inspeccionaremos, validaremos y calcularemos nuevas variables.  
> - Load: prepararemos tablas de resultados que podrían exportarse a CSV, almacenarse en una base de datos o utilizarse en Power BI.  

## 2. Ejercicios

### Ejercicio 1 --> Inspección y validación

- Objetivo: conocer la estructura de los datos antes de transformarlos.

1. Muestra el DataFrame y consulta sus dimensiones.
2. Obtén los nombres de las columnas y los tipos de datos.
3. Utiliza `info()` y `describe()` para inspeccionar la información disponible.
4. Comprueba si existen valores nulos y registros duplicados.
5. Comprueba si la columna `id` contiene identificadores duplicados.

---


### Ejercicio 2 --> Transformación y operaciones vectorizadas

Objetivo: crear variables derivadas sin recorrer las filas manualmente.

1. Añade una columna `importe`, calculada a partir de `precio` y `unidades`.
2. Calcula el importe total de todas las operaciones.
3. Calcula el importe medio, el máximo y el mínimo.
4. Obtén la fila correspondiente a la operación con mayor importe.
5. Ordena las operaciones por importe, de mayor a menor.

> [!NOTE] 
> Una distinción importante
>
> El precio unitario medio no es lo mismo que el importe medio por operación. Tampoco es lo mismo que la facturación total. Debes seleccionar la columna y la operación estadística que correspondan a cada pregunta.

### Ejercicio 3 --> Filtrado y selección

Objetivo: seleccionar registros según criterios de negocio.

1. Obtén las operaciones cuyo importe sea superior a 250.
2. Selecciona las operaciones de la región Norte.
3. Selecciona las operaciones de Hardware con al menos dos unidades.
4. Combina una condición de región con una condición numérica.
5. Devuelve únicamente las columnas `id`, `categoria` e `importe` de las operaciones que cumplan una condición.

> [!WARNING] 
> Sintaxis de condiciones
>
> Para combinar condiciones vectorizadas en pandas, utiliza `&` para AND y `|` para OR, poniendo cada comparación entre paréntesis. No utilices `and` u `or` directamente entre Series.

---

### Ejercicio 4 --> Agrupación y agregación

Objetivo: obtener indicadores por categoría y región.

1. Agrupa por `categoria` y calcula la facturación total.
2. Agrupa por `region` y calcula el importe medio.
3. Agrupa por `categoria` y calcula simultáneamente:
   - Unidades totales.
   - Facturación total.
   - Importe medio por operación.
   - Número de registros.
4. Repite el análisis agrupando por `region` y `categoria`.
5. Presenta al menos uno de los resultados como un DataFrame con las columnas de agrupación visibles, en lugar de utilizarlas como índice.

> [!INFO] 
> Relación con Power BI y SQL
>
> Estas operaciones se relacionan con las agregaciones de una tabla visual o una matriz de Power BI y con `GROUP BY` en SQL. La elección de las dimensiones y las métricas determina qué resumen obtienes.
>
> Puedes resolver el tercer apartado con `.agg()`. Antes de elegir una función, piensa en qué métrica necesitas y qué columna debe utilizarse para calcularla.

---

### Ejercicio 5 --> NumPy y análisis numérico

Objetivo: aplicar NumPy a los datos numéricos extraídos del DataFrame.

1. Convierte la columna `importe` en un array de NumPy.
2. Calcula su media, desviación estándar, mínimo y máximo.
3. Selecciona mediante indexación booleana los importes superiores a la media.
4. Calcula qué porcentaje del importe total representa cada operación.
5. Comprueba si los resultados de suma y media coinciden con los obtenidos mediante pandas, teniendo en cuenta las convenciones utilizadas para calcular la desviación estándar.

> [!NOTE] Comparación entre bibliotecas
>
> NumPy y pandas ofrecen operaciones similares, pero sus estructuras y algunas convenciones difieren. En particular, revisa el parámetro `ddof` de la desviación estándar: el valor predeterminado de NumPy no coincide con el de pandas.

---

### Ejercicio 6 --> Preparación de resultados para ETL

Objetivo: generar resultados que puedan consumirse en otro sistema.

1. Construye una tabla resumen con la facturación por región.
2. Ordena esa tabla por facturación descendente.
3. Comprueba que la suma de las facturaciones regionales coincide con el total global, dado que cada operación pertenece a una sola región.
4. Exporta el resumen a un CSV sin guardar el índice como una columna adicional.
5. Explica qué parte del proceso corresponde a extracción, transformación y carga en este ejercicio, y qué cambiaría si los datos de origen procedieran de un fichero CSV.


