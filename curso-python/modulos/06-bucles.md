# Módulo 06 · Bucles

Los bucles **repiten** código. Son lo que hace que los ordenadores sean tan potentes.

## `while`: repetir mientras se cumpla una condición

```python
contador = 1
while contador <= 5:
    print("Vuelta", contador)
    contador += 1      # ¡importante! si no, el bucle no acaba nunca
print("Terminado")
```

> ⚠️ Si la condición nunca se vuelve falsa tienes un **bucle infinito**. Para pararlo pulsa `Ctrl + C` en la terminal.

`while` es ideal cuando **no sabes cuántas veces** vas a repetir:

```python
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir'): ")
    print("Has escrito:", respuesta)
```

## `for`: recorrer elementos

`for` coge cada elemento de una secuencia, uno a uno:

```python
for letra in "Hola":
    print(letra)
```

### `range()`: secuencias de números

| Código | Números generados |
|--------|-------------------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 11, 2)` | 0, 2, 4, 6, 8, 10 |
| `range(10, 0, -1)` | 10, 9, … , 1 |

```python
for i in range(1, 6):
    print(f"5 x {i} = {5 * i}")
```

`for` es ideal cuando **sabes cuántas veces** o tienes una colección que recorrer.

## `break` y `continue`

- `break` **sale** del bucle inmediatamente.
- `continue` **salta** al siguiente paso del bucle.

```python
for n in range(1, 11):
    if n == 7:
        break          # al llegar a 7 se acaba
    if n % 2 == 0:
        continue       # los pares se saltan
    print(n)           # muestra 1, 3, 5
```

Patrón muy común: bucle infinito con salida controlada.

```python
while True:
    texto = input("Número (o 'fin'): ")
    if texto == "fin":
        break
    print("El doble es", int(texto) * 2)
```

## Acumuladores y contadores

```python
total = 0
for n in range(1, 101):
    total += n
print("La suma del 1 al 100 es", total)   # 5050
```

## Bucles anidados

```python
for fila in range(1, 4):
    for col in range(1, 4):
        print(fila * col, end="\t")   # end="\t" evita el salto de línea
    print()                            # salto de línea al acabar la fila
```

## 🏋️ Ejercicios

1. Muestra los números del 10 al 1 y luego "¡Despegue!".
2. Pide un número y muestra su tabla de multiplicar del 1 al 10.
3. Suma todos los números pares entre 1 y 100.
4. Pide números al usuario hasta que escriba `0`. Al final muestra cuántos ha escrito, su suma y su media.
5. **Adivina el número:** guarda un número secreto (ej: 37). Pide números al usuario y dile "más alto" o "más bajo" hasta que acierte. Al final dile en cuántos intentos lo consiguió.
6. Dibuja con `*` un triángulo de la altura que pida el usuario:
   ```
   *
   **
   ***
   ****
   ```
7. **FizzBuzz** (clásico de entrevistas): muestra los números del 1 al 30, pero si es múltiplo de 3 escribe `Fizz`, si es múltiplo de 5 `Buzz`, y si lo es de ambos `FizzBuzz`.

💡 Solución: [`soluciones/06_bucles.py`](../soluciones/06_bucles.py)

➡️ Siguiente: [Módulo 07 · Listas y tuplas](07-listas-y-tuplas.md)
