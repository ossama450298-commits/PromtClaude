# Módulo 11 · Archivos

Cuando un programa termina, sus variables desaparecen. Para **guardar información** de forma permanente
la escribimos en archivos.

## Escribir un archivo

```python
with open("notas.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
```

- `open(nombre, modo)` abre el archivo.
- `with ... as archivo:` lo **cierra automáticamente** al terminar el bloque. Úsalo siempre.
- `encoding="utf-8"` evita problemas con tildes y la ñ.

### Modos de apertura

| Modo | Significado |
|------|-------------|
| `"r"` | Leer (por defecto). Error si no existe. |
| `"w"` | Escribir. **Borra** el contenido anterior o crea el archivo. |
| `"a"` | Añadir al final (*append*). Crea el archivo si no existe. |

## Leer un archivo

```python
# Todo de golpe
with open("notas.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Línea a línea (mejor para archivos grandes)
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())   # strip() quita el \n final
```

## Añadir sin borrar

```python
with open("diario.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Hoy he aprendido a usar archivos\n")
```

## Si el archivo no existe

```python
try:
    with open("no_existe.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")
```

## Archivos CSV (datos en tabla)

Un CSV es texto con valores separados por comas. Se abre con Excel.

```python
import csv

# Escribir
with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["nombre", "nota"])
    escritor.writerow(["Ana", 8.5])
    escritor.writerow(["Luis", 6.0])

# Leer como diccionarios
with open("alumnos.csv", encoding="utf-8") as f:
    for fila in csv.DictReader(f):
        print(fila["nombre"], fila["nota"])
```

## JSON: guardar listas y diccionarios

JSON es el formato estándar para guardar datos estructurados. Python convierte sus listas y diccionarios a JSON y viceversa.

```python
import json

datos = {
    "usuario": "ana",
    "puntos": 150,
    "logros": ["primer nivel", "sin errores"],
}

# Guardar
with open("partida.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

# Cargar
with open("partida.json", encoding="utf-8") as f:
    cargados = json.load(f)

print(cargados["logros"])   # ['primer nivel', 'sin errores']
```

Con esto tus programas ya pueden **recordar** cosas entre ejecuciones.

## 🏋️ Ejercicios

1. Pide al usuario 3 frases y guárdalas en `frases.txt`, una por línea. Luego léelo y muestra cada línea numerada.
2. Escribe un programa que cuente cuántas líneas, palabras y caracteres tiene un archivo de texto.
3. **Diario:** cada vez que ejecutes el programa, pide una entrada y añádela a `diario.txt` (sin borrar las anteriores). Después muestra todo el diario.
4. Guarda la agenda del módulo 08 en `agenda.json` al salir y cárgala al empezar, para que los contactos no se pierdan.
5. Crea un CSV con productos y precios, léelo y muestra el precio total.

💡 Solución: [`soluciones/11_archivos.py`](../soluciones/11_archivos.py)

➡️ Siguiente: [Módulo 12 · Módulos y librerías](12-modulos.md)
