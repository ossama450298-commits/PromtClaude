# Módulo 08 · Diccionarios y conjuntos

## Diccionarios

Un diccionario guarda datos en pares **clave → valor**, como un diccionario real (palabra → definición)
o una agenda (nombre → teléfono). Se escriben con llaves `{}`.

```python
persona = {
    "nombre": "Carlos",
    "edad": 28,
    "ciudad": "Sevilla",
}

print(persona["nombre"])   # Carlos
```

En lugar de acceder por posición (como en las listas) accedes **por clave**.

### Añadir, cambiar y borrar

```python
persona["email"] = "carlos@ejemplo.com"   # añade una clave nueva
persona["edad"] = 29                      # cambia un valor existente
del persona["ciudad"]                     # borra una clave
```

### Leer sin errores: `get()`

```python
print(persona["telefono"])                # ❌ KeyError: la clave no existe
print(persona.get("telefono"))            # None
print(persona.get("telefono", "Sin dato")) # Sin dato
print("edad" in persona)                  # True (comprueba si existe la clave)
```

### Recorrer un diccionario

```python
precios = {"pan": 1.20, "leche": 0.95, "huevos": 2.50}

for producto in precios:                  # recorre las claves
    print(producto)

for producto, precio in precios.items():  # claves y valores a la vez
    print(f"{producto}: {precio:.2f} €")

print(list(precios.keys()))     # ['pan', 'leche', 'huevos']
print(list(precios.values()))   # [1.2, 0.95, 2.5]
print(sum(precios.values()))    # 4.65
```

### Contar cosas con un diccionario (patrón muy útil)

```python
texto = "el perro y el gato y el loro"
conteo = {}
for palabra in texto.split():
    conteo[palabra] = conteo.get(palabra, 0) + 1
print(conteo)   # {'el': 3, 'perro': 1, 'y': 2, 'gato': 1, 'loro': 1}
```

### Estructuras combinadas

En programas reales es muy común tener **listas de diccionarios**:

```python
alumnos = [
    {"nombre": "Ana", "nota": 8.5},
    {"nombre": "Luis", "nota": 6.0},
    {"nombre": "Marta", "nota": 9.2},
]

for alumno in alumnos:
    print(f"{alumno['nombre']} sacó un {alumno['nota']}")

mejor = max(alumnos, key=lambda a: a["nota"])
print("La mejor nota es de", mejor["nombre"])
```

> `key=lambda a: a["nota"]` le dice a `max` "compara usando la nota". Veremos `lambda` en el módulo de funciones.

## Conjuntos (`set`)

Un conjunto es una colección **sin orden y sin elementos repetidos**.

```python
colores = {"rojo", "verde", "azul", "rojo"}
print(colores)          # {'rojo', 'verde', 'azul'}  (el repetido desaparece)

colores.add("negro")
colores.discard("verde")

# Quitar duplicados de una lista:
unicos = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}
```

Operaciones de conjuntos:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)   # unión:        {1, 2, 3, 4, 5, 6}
print(a & b)   # intersección: {3, 4}
print(a - b)   # diferencia:   {1, 2}
```

## ¿Qué estructura uso?

| Necesito… | Uso |
|-----------|-----|
| Una colección ordenada que cambia | `list` |
| Datos fijos que no cambian | `tuple` |
| Buscar valores por un nombre/clave | `dict` |
| Elementos únicos o comparar grupos | `set` |

## 🏋️ Ejercicios

1. Crea un diccionario con la información de un libro (título, autor, año, páginas) y muéstrala con un bucle.
2. **Agenda:** un menú que permita añadir contacto (nombre → teléfono), buscar un contacto, borrar uno y mostrar todos.
3. Pide una frase y cuenta cuántas veces aparece cada letra (ignora los espacios).
4. Dado un diccionario de productos y precios, muestra los que cuestan más de 2 € y el precio medio.
5. Dadas dos listas de amigos de dos personas, muestra los amigos en común y los que solo tiene cada uno.
6. Con la lista `alumnos` del ejemplo, muestra la nota media de la clase y los nombres de los que aprobaron (nota ≥ 5).

💡 Solución: [`soluciones/08_diccionarios_y_conjuntos.py`](../soluciones/08_diccionarios_y_conjuntos.py)

➡️ Siguiente: [Módulo 09 · Funciones](09-funciones.md)
