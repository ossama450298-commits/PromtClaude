# Módulo 03 · Operadores

## Operadores aritméticos

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `+` | suma | `7 + 2` | `9` |
| `-` | resta | `7 - 2` | `5` |
| `*` | multiplicación | `7 * 2` | `14` |
| `/` | división | `7 / 2` | `3.5` |
| `//` | división entera | `7 // 2` | `3` |
| `%` | resto (módulo) | `7 % 2` | `1` |
| `**` | potencia | `7 ** 2` | `49` |

Dos muy útiles:
- `//` te dice **cuántas veces cabe** un número en otro: 125 minutos son `125 // 60` = 2 horas…
- `%` te da **lo que sobra**: …y `125 % 60` = 5 minutos.
- `%` también sirve para saber si un número es par: `n % 2 == 0`.

### Orden de las operaciones

Igual que en matemáticas: primero `**`, luego `*` `/` `//` `%`, y después `+` `-`. Usa paréntesis cuando dudes.

```python
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20
```

### Atajos de asignación

```python
x = 10
x += 5    # igual que x = x + 5  → 15
x -= 3    # x = x - 3            → 12
x *= 2    # x = x * 2            → 24
x /= 4    # x = x / 4            → 6.0
```

### Redondear

```python
print(round(3.14159, 2))   # 3.14
print(round(2.7))          # 3
```

## Operadores de comparación

Comparan dos valores y devuelven `True` o `False`.

| Operador | Significado | Ejemplo | Resultado |
|----------|-------------|---------|-----------|
| `==` | igual a | `5 == 5` | `True` |
| `!=` | distinto de | `5 != 3` | `True` |
| `>` | mayor que | `5 > 3` | `True` |
| `<` | menor que | `5 < 3` | `False` |
| `>=` | mayor o igual | `5 >= 5` | `True` |
| `<=` | menor o igual | `4 <= 3` | `False` |

> ⚠️ No confundas `=` (guardar en una variable) con `==` (comparar).

Python permite encadenar: `0 < edad < 120`.

## Operadores lógicos

Combinan condiciones.

| Operador | Devuelve `True` si… | Ejemplo |
|----------|---------------------|---------|
| `and` | **las dos** son verdaderas | `edad >= 18 and tiene_carnet` |
| `or` | **al menos una** es verdadera | `es_sabado or es_domingo` |
| `not` | la condición es falsa (la invierte) | `not lloviendo` |

```python
edad = 20
tiene_entrada = True
print(edad >= 18 and tiene_entrada)   # True
print(edad < 18 or tiene_entrada)     # True
print(not tiene_entrada)              # False
```

## 🏋️ Ejercicios

1. Pide un número de segundos y muéstralo en horas, minutos y segundos (ej: `3725` → `1 h 2 min 5 s`).
2. Pide el precio de un producto y el porcentaje de descuento; muestra el precio final redondeado a 2 decimales.
3. Pide un número y muestra `True` si es par y `False` si es impar (sin usar `if`).
4. Pide la edad y muestra `True` si la persona está entre 18 y 65 años (ambos incluidos).
5. Calcula el área de un círculo de radio pedido al usuario (`área = 3.14159 * r²`).

💡 Solución: [`soluciones/03_operadores.py`](../soluciones/03_operadores.py)

➡️ Siguiente: [Módulo 04 · Cadenas de texto](04-cadenas.md)
