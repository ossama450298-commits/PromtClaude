# Módulo 07 · Listas y tuplas

## Listas

Una lista guarda **varios valores en orden** dentro de una sola variable. Se escriben con corchetes `[]`.

```python
frutas = ["manzana", "pera", "plátano"]
numeros = [4, 8, 15, 16, 23, 42]
mezcla = ["texto", 3, True, 2.5]   # puede mezclar tipos
vacia = []
```

### Acceder a los elementos

Funciona igual que con los strings (índices desde 0, negativos, slicing):

```python
frutas = ["manzana", "pera", "plátano", "kiwi"]
print(frutas[0])      # manzana
print(frutas[-1])     # kiwi
print(frutas[1:3])    # ['pera', 'plátano']
print(len(frutas))    # 4
```

### Las listas SÍ se pueden modificar

```python
frutas[1] = "melón"           # cambia un elemento
frutas.append("uva")          # añade al final
frutas.insert(0, "fresa")     # añade en una posición
frutas.remove("kiwi")         # quita por valor
ultima = frutas.pop()         # quita y devuelve el último
del frutas[0]                 # quita por posición
```

### Otros métodos y funciones útiles

```python
nums = [5, 2, 9, 1, 7]
nums.sort()                 # ordena la lista → [1, 2, 5, 7, 9]
nums.sort(reverse=True)     # de mayor a menor
nums.reverse()              # le da la vuelta
nums.count(5)               # cuántas veces aparece el 5
nums.index(9)               # en qué posición está el 9

sorted(nums)                # devuelve una copia ordenada (no cambia la original)
sum(nums), max(nums), min(nums)
7 in nums                   # True
```

### Recorrer una lista

```python
compra = ["pan", "leche", "huevos"]

for producto in compra:
    print("-", producto)

# Si también necesitas la posición:
for i, producto in enumerate(compra, start=1):
    print(f"{i}. {producto}")
```

### Construir listas en un bucle

```python
cuadrados = []
for n in range(1, 6):
    cuadrados.append(n ** 2)
print(cuadrados)   # [1, 4, 9, 16, 25]
```

### List comprehensions (forma corta)

Lo mismo de arriba en una línea:

```python
cuadrados = [n ** 2 for n in range(1, 6)]
pares = [n for n in range(20) if n % 2 == 0]
mayusculas = [f.upper() for f in ["a", "b", "c"]]
```

### Listas dentro de listas

```python
tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(tablero[1][2])   # fila 1, columna 2 → 6
```

### ⚠️ Cuidado al copiar

```python
a = [1, 2, 3]
b = a          # ¡b NO es una copia! Son la misma lista con dos nombres
b.append(4)
print(a)       # [1, 2, 3, 4]

c = a.copy()   # esto sí es una copia independiente
```

## Tuplas

Una tupla es como una lista pero **no se puede modificar**. Se escribe con paréntesis `()`.
Úsalas para datos que no deben cambiar: coordenadas, fechas, colores RGB…

```python
punto = (3, 5)
print(punto[0])     # 3
# punto[0] = 10     # ❌ TypeError

# Desempaquetar: repartir los valores en variables
x, y = punto
print(x, y)         # 3 5
```

## 🏋️ Ejercicios

1. Crea una lista con 5 notas. Muestra la nota más alta, la más baja y la media.
2. Pide al usuario palabras hasta que escriba `fin` y guárdalas en una lista. Muéstralas ordenadas alfabéticamente.
3. Dada `numeros = [3, 8, 1, 9, 4, 7, 2]`, crea una nueva lista solo con los mayores que 4 (hazlo con un bucle y luego con una *list comprehension*).
4. Elimina los duplicados de `[1, 2, 2, 3, 4, 4, 4, 5]` manteniendo el orden.
5. **Lista de la compra:** haz un menú que permita (1) añadir producto, (2) eliminar producto, (3) ver lista, (4) salir.
6. Dada una lista de tuplas `(nombre, edad)`, muestra solo los nombres de los mayores de edad.

💡 Solución: [`soluciones/07_listas_y_tuplas.py`](../soluciones/07_listas_y_tuplas.py)

➡️ Siguiente: [Módulo 08 · Diccionarios y conjuntos](08-diccionarios-y-conjuntos.md)
