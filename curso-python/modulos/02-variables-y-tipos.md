# Módulo 02 · Variables y tipos de datos

## ¿Qué es una variable?

Una variable es una **caja con nombre** donde guardas un dato para usarlo después.

```python
nombre = "Lucía"
edad = 30

print(nombre)   # Lucía
print(edad)     # 30
```

El `=` **no** significa "igual" como en matemáticas: significa **"guarda lo de la derecha en la caja de la izquierda"**.

Puedes cambiar el contenido cuando quieras:

```python
puntos = 10
puntos = puntos + 5   # coge el valor actual (10), suma 5, y lo guarda otra vez
print(puntos)         # 15
```

### Reglas para los nombres

- Pueden tener letras, números y `_`, pero **no pueden empezar por número**.
- No pueden tener espacios: usa `_` → `precio_total`.
- Distinguen mayúsculas: `edad` y `Edad` son variables distintas.
- Usa nombres que expliquen qué guardan: `precio` mejor que `p`.

## Tipos de datos básicos

| Tipo | Nombre | Ejemplos |
|------|--------|----------|
| `int` | Número entero | `7`, `-3`, `2026` |
| `float` | Número decimal | `3.14`, `-0.5`, `1.0` |
| `str` | Texto (*string*) | `"hola"`, `'Python'`, `"123"` |
| `bool` | Verdadero / falso | `True`, `False` |

> ⚠️ Los decimales se escriben con **punto**, no con coma: `3.14`.

Para saber el tipo de algo usa `type()`:

```python
print(type(7))        # <class 'int'>
print(type(7.0))      # <class 'float'>
print(type("7"))      # <class 'str'>
print(type(True))     # <class 'bool'>
```

`"7"` y `7` **no son lo mismo**: el primero es texto y el segundo un número.

```python
print("7" + "7")   # 77  (une textos)
print(7 + 7)       # 14  (suma números)
```

## Pedir datos al usuario: `input()`

`input()` muestra un mensaje, espera a que el usuario escriba algo y pulse Enter, y devuelve lo escrito.

```python
nombre = input("¿Cómo te llamas? ")
print("Encantado,", nombre)
```

⚠️ **`input()` siempre devuelve texto (`str`)**, aunque el usuario escriba un número.

```python
edad = input("¿Cuántos años tienes? ")
print(edad + 1)   # ❌ TypeError: can only concatenate str (not "int") to str
```

## Convertir entre tipos

| Función | Convierte a | Ejemplo |
|---------|-------------|---------|
| `int()` | entero | `int("42")` → `42` |
| `float()` | decimal | `float("3.5")` → `3.5` |
| `str()` | texto | `str(42)` → `"42"` |
| `bool()` | booleano | `bool(0)` → `False` |

Ahora sí:

```python
edad = int(input("¿Cuántos años tienes? "))
print("El año que viene tendrás", edad + 1)
```

## 🏋️ Ejercicios

1. Crea variables con tu nombre, tu edad y tu altura en metros. Muéstralas con `print` y comprueba su tipo con `type()`.
2. Pide al usuario dos números y muestra su suma. (Recuerda convertirlos).
3. Pide el año de nacimiento y calcula la edad aproximada que tendrá en 2030.
4. Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: `F = C * 9 / 5 + 32`.
5. **Intercambio:** tienes `a = 5` y `b = 8`. Consigue que `a` valga 8 y `b` valga 5 sin escribir los números otra vez.

💡 Solución: [`soluciones/02_variables_y_tipos.py`](../soluciones/02_variables_y_tipos.py)

➡️ Siguiente: [Módulo 03 · Operadores](03-operadores.md)
