# Módulo 05 · Condicionales

Hasta ahora tus programas hacían siempre lo mismo. Con los condicionales pueden **tomar decisiones**.

## `if`

```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar")

print("Fin del programa")   # esto se ejecuta siempre
```

Fíjate en dos cosas **obligatorias**:
1. Los **dos puntos** `:` al final de la línea del `if`.
2. La **sangría** (indentación): las líneas de dentro del `if` empiezan con **4 espacios**. Así sabe Python qué está "dentro". VS Code lo hace automáticamente al pulsar Enter tras los `:`.

## `else`: si no…

```python
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
```

## `elif`: varias opciones

`elif` significa "si no, si…". Python comprueba las condiciones **en orden** y ejecuta **solo la primera** que sea verdadera.

```python
nota = float(input("Nota (0-10): "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

## Combinar condiciones

```python
hora = 14
es_festivo = False

if hora >= 9 and hora < 18 and not es_festivo:
    print("La tienda está abierta")
else:
    print("La tienda está cerrada")
```

## Condicionales anidados

Un `if` puede ir dentro de otro (con más sangría):

```python
tiene_entrada = True
edad = 16

if tiene_entrada:
    if edad >= 18:
        print("Adelante")
    else:
        print("Necesitas ir acompañado")
else:
    print("Compra una entrada primero")
```

## Valores "verdaderos" y "falsos"

En un `if`, Python considera **falsos**: `0`, `0.0`, `""` (texto vacío), `[]` (lista vacía), `None` y `False`. Todo lo demás es verdadero.

```python
nombre = input("Nombre: ")
if nombre:
    print(f"Hola, {nombre}")
else:
    print("No has escrito nada")
```

## 🏋️ Ejercicios

1. Pide un número y di si es positivo, negativo o cero.
2. Pide un número y di si es par o impar.
3. Pide tres números y muestra el mayor (sin usar `max()`).
4. Pide un año y di si es bisiesto. Regla: divisible entre 4, excepto los divisibles entre 100, salvo que también lo sean entre 400. (2024 sí, 1900 no, 2000 sí).
5. **Calculadora:** pide dos números y una operación (`+`, `-`, `*`, `/`) y muestra el resultado. Si es una división entre 0, muestra un aviso.
6. **Login simple:** guarda un usuario y contraseña en variables. Pide ambos al usuario y di si son correctos, si falla el usuario o si falla la contraseña.

💡 Solución: [`soluciones/05_condicionales.py`](../soluciones/05_condicionales.py)

➡️ Siguiente: [Módulo 06 · Bucles](06-bucles.md)
