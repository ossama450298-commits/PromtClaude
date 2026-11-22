# Módulo 04 · Cadenas de texto (strings)

## Unir y repetir

```python
nombre = "Ana"
saludo = "Hola, " + nombre + "!"   # concatenar con +
print(saludo)                       # Hola, Ana!
print("ja" * 3)                     # jajaja
```

## f-strings: la mejor forma de mezclar texto y variables

Pon una `f` antes de las comillas y mete las variables entre `{llaves}`:

```python
nombre = "Ana"
edad = 30
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"El año que viene tendré {edad + 1}")    # puedes poner expresiones
precio = 19.98765
print(f"Precio: {precio:.2f} €")                # 2 decimales → 19.99 €
```

No necesitas convertir números con `str()`. Usarás f-strings constantemente.

## Longitud: `len()`

```python
print(len("Python"))   # 6
```

## Índices: acceder a cada letra

Cada carácter tiene una posición, **empezando en 0**:

```
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
palabra = "Python"
print(palabra[0])    # P
print(palabra[3])    # h
print(palabra[-1])   # n  (los negativos cuentan desde el final)
```

## Slicing: trocear un texto

`texto[inicio:fin]` coge desde `inicio` **hasta `fin` sin incluirlo**.

```python
palabra = "Python"
print(palabra[0:3])    # Pyt
print(palabra[2:])     # thon   (hasta el final)
print(palabra[:4])     # Pyth   (desde el principio)
print(palabra[::-1])   # nohtyP (al revés)
```

## Métodos útiles

Un **método** es una función que pertenece a un dato. Se usa con un punto: `texto.metodo()`.

```python
frase = "  Hola Mundo  "

frase.upper()           # "  HOLA MUNDO  "
frase.lower()           # "  hola mundo  "
frase.strip()           # "Hola Mundo"       quita espacios de los extremos
"hola mundo".title()    # "Hola Mundo"
"hola".capitalize()     # "Hola"
"Hola Mundo".replace("Mundo", "Python")   # "Hola Python"
"banana".count("a")     # 3
"banana".find("n")      # 2   (posición; -1 si no está)
"a,b,c".split(",")      # ['a', 'b', 'c']   (lo trocea en una lista)
"-".join(["a", "b"])    # "a-b"
"hola".startswith("ho") # True
"123".isdigit()         # True
```

⚠️ Los textos **no se modifican**: los métodos devuelven un texto nuevo. Si quieres conservarlo, guárdalo:

```python
nombre = "ana"
nombre.upper()          # no cambia 'nombre'
nombre = nombre.upper() # ahora sí: "ANA"
```

## Comprobar si algo está dentro: `in`

```python
print("mundo" in "hola mundo")   # True
print("x" not in "hola")         # True
```

## 🏋️ Ejercicios

1. Pide nombre y apellido, y muestra: `Bienvenido/a, APELLIDO, Nombre` (apellido en mayúsculas, nombre con la primera en mayúscula).
2. Pide una palabra y muestra su primera letra, su última letra y cuántas letras tiene.
3. Pide una frase y muéstrala al revés.
4. Pide una frase y cuenta cuántas veces aparece la letra "a" (en mayúsculas o minúsculas).
5. Pide un email y muestra el usuario (lo que va antes de `@`) y el dominio (lo que va después).
6. Pide una palabra y muestra `True` si es un palíndromo (se lee igual al revés, como "reconocer").

💡 Solución: [`soluciones/04_cadenas.py`](../soluciones/04_cadenas.py)

➡️ Siguiente: [Módulo 05 · Condicionales](05-condicionales.md)
