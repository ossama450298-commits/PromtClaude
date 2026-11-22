# Módulo 01 · Primeros pasos

## `print()`: mostrar cosas en pantalla

`print()` es una **función**: una orden con nombre que hace algo. Lo que pones entre paréntesis es lo que mostrará.

```python
print("Hola")
print("Me llamo Ana")
print(42)
print(3 + 4)
```

Salida:
```
Hola
Me llamo Ana
42
7
```

- El **texto** va entre comillas, dobles `"..."` o simples `'...'`.
- Los **números** van sin comillas, y Python puede hacer cuentas con ellos.
- Fíjate en la diferencia: `print("3 + 4")` muestra `3 + 4`, pero `print(3 + 4)` muestra `7`.

Puedes mostrar varias cosas separadas por comas; Python pone un espacio entre ellas:

```python
print("Tengo", 25, "años")   # Tengo 25 años
```

## Comentarios

Todo lo que va detrás de `#` es un **comentario**: Python lo ignora. Sirve para explicar tu código.

```python
# Este programa saluda
print("Hola")  # esto también es un comentario
```

## El orden importa

Python ejecuta las líneas **de arriba abajo**, una a una:

```python
print("Primero")
print("Segundo")
print("Tercero")
```

## Caracteres especiales

- `\n` es un salto de línea: `print("Línea 1\nLínea 2")`
- `\t` es una tabulación.
- Si tu texto lleva comillas, usa el otro tipo por fuera: `print('Dijo "hola"')`

## Tus primeros errores (y cómo leerlos)

Los errores no son malos: son Python diciéndote qué no entiende. Lee siempre **la última línea** del mensaje.

```python
print("Hola)
```
```
SyntaxError: unterminated string literal
```
→ Falta cerrar las comillas.

```python
Print("Hola")
```
```
NameError: name 'Print' is not defined
```
→ Python distingue mayúsculas y minúsculas: es `print`, no `Print`.

```python
    print("Hola")
```
```
IndentationError: unexpected indent
```
→ Hay espacios al principio de la línea que no deberían estar. En Python los espacios iniciales **tienen significado** (lo veremos en el módulo 05).

## 🏋️ Ejercicios

1. Muestra tu nombre, tu ciudad y tu comida favorita, cada uno en una línea.
2. Muestra el resultado de `365 * 24` (horas que tiene un año) con un texto que lo explique.
3. Dibuja este cuadrado usando solo `print`:
   ```
   *****
   *   *
   *   *
   *****
   ```
4. Con un **solo** `print` y usando `\n`, muestra tres líneas: `Uno`, `Dos`, `Tres`.
5. Escribe a propósito tres errores distintos y lee los mensajes que te da Python.

💡 Solución: [`soluciones/01_primeros_pasos.py`](../soluciones/01_primeros_pasos.py)

➡️ Siguiente: [Módulo 02 · Variables y tipos de datos](02-variables-y-tipos.md)
