# Módulo 09 · Funciones

Una función es un **bloque de código con nombre** que puedes usar (llamar) tantas veces como quieras.
Ya has usado muchas: `print()`, `len()`, `input()`… Ahora crearás las tuyas.

¿Por qué? Para **no repetir código**, para **organizar** el programa en partes pequeñas y para que sea **más fácil de leer y corregir**.

## Definir y llamar una función

```python
def saludar():
    print("¡Hola!")
    print("Bienvenido/a")

saludar()   # la llamamos
saludar()   # y otra vez
```

`def` + nombre + `()` + `:` y el cuerpo con sangría. **Definir** una función no la ejecuta; solo se ejecuta cuando la **llamas**.

## Parámetros: darle datos a la función

```python
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Ana")
saludar("Luis")
```

Varios parámetros:

```python
def presentar(nombre, edad):
    print(f"{nombre} tiene {edad} años")

presentar("Ana", 30)
presentar(edad=25, nombre="Luis")   # por nombre, el orden da igual
```

### Valores por defecto

```python
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}")

saludar("Ana")              # Hola, Ana
saludar("Ana", "Buenas")    # Buenas, Ana
```

## `return`: devolver un resultado

Hasta ahora las funciones mostraban cosas. Lo más útil es que **devuelvan** un valor para usarlo después.

```python
def sumar(a, b):
    return a + b

resultado = sumar(3, 4)
print(resultado)              # 7
print(sumar(10, 20) * 2)      # 60
```

> 🔑 **`print` muestra, `return` devuelve.** Una función con `print` no te da el valor para seguir trabajando con él.
> Cuando se ejecuta `return`, la función **termina** en ese momento.

```python
def es_par(n):
    return n % 2 == 0

if es_par(10):
    print("Es par")
```

Puedes devolver varios valores (en realidad, una tupla):

```python
def min_max(numeros):
    return min(numeros), max(numeros)

menor, mayor = min_max([4, 1, 9])
```

## Ámbito (*scope*) de las variables

Las variables creadas **dentro** de una función solo existen dentro de ella.

```python
def ejemplo():
    x = 10
    print(x)

ejemplo()
print(x)   # ❌ NameError: x no existe fuera
```

Buena práctica: pasa datos con **parámetros** y saca resultados con **`return`**, en vez de depender de variables de fuera.

## Documentar funciones

```python
def area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    return base * altura
```

El texto entre triples comillas (*docstring*) explica qué hace. Puedes verlo con `help(area_rectangulo)`.

## Funciones lambda (funciones de una línea)

```python
doble = lambda x: x * 2
print(doble(5))   # 10

palabras = ["kiwi", "manzana", "pera"]
print(sorted(palabras, key=lambda p: len(p)))   # ordena por longitud
```

Se usan sobre todo como argumento de `sorted`, `max`, `min`…

## La función principal

Los programas bien organizados suelen tener todo dentro de funciones y una función `main()`:

```python
def pedir_numero(mensaje):
    return float(input(mensaje))

def main():
    a = pedir_numero("Primer número: ")
    b = pedir_numero("Segundo número: ")
    print("Suma:", a + b)

if __name__ == "__main__":
    main()
```

La última línea significa "ejecuta `main()` solo si este archivo se ejecuta directamente" (lo entenderás mejor en el módulo 12).

## 🏋️ Ejercicios

1. Escribe `area_circulo(radio)` que devuelva el área.
2. Escribe `es_primo(n)` que devuelva `True` si `n` es primo. Úsala para mostrar los primos del 1 al 50.
3. Escribe `contar_vocales(texto)` que devuelva cuántas vocales tiene un texto.
4. Escribe `celsius_a_fahrenheit(c)` y `fahrenheit_a_celsius(f)`.
5. Escribe `estadisticas(lista)` que devuelva la media, el mínimo y el máximo.
6. Escribe `pedir_entero(mensaje, minimo, maximo)` que pida un número al usuario y lo vuelva a pedir hasta que esté en el rango.
7. Rehaz la calculadora del módulo 05 con una función por operación y un `main()`.

💡 Solución: [`soluciones/09_funciones.py`](../soluciones/09_funciones.py)

➡️ Siguiente: [Módulo 10 · Errores y excepciones](10-excepciones.md)
