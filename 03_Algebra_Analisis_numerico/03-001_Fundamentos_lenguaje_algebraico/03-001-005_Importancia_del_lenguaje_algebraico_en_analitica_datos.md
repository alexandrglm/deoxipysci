# 03-005:   Fundamentos del lenguaje algebraico

***

## 1.5. Por qué importa en análisis de datos

Las fórmulas de análisis de datos son **expresiones algebraicas aplicadas a conjuntos de valores**.  

Por ejemplo, el importe de una operación puede calcularse así:  

$$
\text{importe} = \text{precio} \cdot \text{unidades}
$$

En pandas:

```python
datos["importe"] = datos["precio"] * datos["unidades"]
```

La expresión matemática es sencilla, pero el código aplica la operación a los valores correspondientes de las columnas. Más adelante veremos por qué esto se relaciona con los vectores y la vectorización.  
