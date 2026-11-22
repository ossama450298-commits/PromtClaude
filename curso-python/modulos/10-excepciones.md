# Módulo 10 · Errores y excepciones

Si el usuario escribe `"hola"` cuando pides un número, `int("hola")` **rompe el programa**:

```
ValueError: invalid literal for int() with base 10: 'hola'
```

Una **excepción** es un error que ocurre mientras el programa se ejecuta. Podemos **capturarla** para que el programa no se detenga.

## `try` / `except`

```python
try:
    edad = int(input("Edad: "))
    print("El año que viene tendrás", edad + 1)
except ValueError:
    print("Eso no es un número válido")
```

- Python intenta ejecutar el bloque `try`.
- Si ocurre un `ValueError`, salta al `except` en lugar de romperse.

## Pedir datos hasta que sean válidos

Combinando con un bucle tienes un patrón que usarás mucho:

```python
while True:
    try:
        numero = int(input("Introduce un número: "))
        break                      # si llega aquí, es válido: salimos
    except ValueError:
        print("No es un número, inténtalo de nuevo.")

print("Has escrito", numero)
```

## Varios tipos de error

```python
try:
    a = int(input("Dividendo: "))
    b = int(input("Divisor: "))
    print(a / b)
except ValueError:
    print("Tienes que escribir números")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

## `else` y `finally`

```python
try:
    n = int(input("Número: "))
except ValueError:
    print("Error")
else:
    print("Todo bien, has escrito", n)       # solo si NO hubo error
finally:
    print("Esto se ejecuta siempre")          # haya error o no
```

## Ver el mensaje del error

```python
try:
    numeros = [1, 2, 3]
    print(numeros[10])
except IndexError as e:
    print("Ha ocurrido un error:", e)    # list index out of range
```

## Excepciones más comunes

| Excepción | Cuándo ocurre |
|-----------|---------------|
| `ValueError` | Valor del tipo correcto pero inválido: `int("abc")` |
| `TypeError` | Operación con tipos incompatibles: `"a" + 1` |
| `ZeroDivisionError` | Dividir entre cero |
| `IndexError` | Índice fuera de la lista |
| `KeyError` | Clave que no existe en un diccionario |
| `NameError` | Variable que no existe |
| `FileNotFoundError` | Archivo que no existe |

## Lanzar tus propios errores: `raise`

```python
def retirar_dinero(saldo, cantidad):
    if cantidad > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - cantidad

try:
    retirar_dinero(100, 500)
except ValueError as e:
    print("No se pudo:", e)
```

> ⚠️ Evita `except:` a secas (sin tipo de error): captura **todo**, incluso errores de programación que deberías ver y corregir.

## 🏋️ Ejercicios

1. Escribe `pedir_float(mensaje)` que pida un número decimal y lo repita hasta que sea válido.
2. Haz una calculadora de división que gestione `ValueError` y `ZeroDivisionError`.
3. Dada la lista `["10", "20", "abc", "30", "", "5"]`, suma solo los valores que se puedan convertir a número e indica cuántos no se pudieron convertir.
4. Escribe `obtener_precio(precios, producto)` que lance un `KeyError` con un mensaje claro si el producto no existe, y captúralo al llamarla.
5. Escribe `crear_usuario(nombre, edad)` que lance `ValueError` si el nombre está vacío o la edad no está entre 0 y 120.

💡 Solución: [`soluciones/10_excepciones.py`](../soluciones/10_excepciones.py)

➡️ Siguiente: [Módulo 11 · Archivos](11-archivos.md)
