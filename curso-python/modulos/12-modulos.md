# Módulo 12 · Módulos y librerías

Un **módulo** es un archivo de Python con funciones (y otras cosas) que puedes reutilizar.
Python trae cientos de módulos ya hechos: es lo que se llama la **biblioteca estándar** ("pilas incluidas").

## Importar

```python
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793

from math import sqrt, pi # importar solo lo que necesitas
print(sqrt(25))

import datetime as dt     # importar con un alias (nombre corto)
```

## Módulos de la biblioteca estándar que te serán útiles

### `random`: azar

```python
import random

random.randint(1, 6)                  # entero entre 1 y 6 (dado)
random.random()                       # decimal entre 0 y 1
random.choice(["piedra", "papel", "tijera"])
random.shuffle(mi_lista)              # desordena una lista
random.sample(range(1, 50), 6)        # 6 números distintos (lotería)
```

### `math`: matemáticas

```python
import math
math.sqrt(2), math.pow(2, 10), math.floor(3.7), math.ceil(3.2), math.pi
```

### `datetime`: fechas y horas

```python
from datetime import datetime, date, timedelta

ahora = datetime.now()
print(ahora.strftime("%d/%m/%Y %H:%M"))   # 22/11/2026 18:30

hoy = date.today()
en_una_semana = hoy + timedelta(days=7)
cumple = date(2027, 3, 15)
print("Faltan", (cumple - hoy).days, "días")
```

### `time`: esperar

```python
import time
time.sleep(2)   # pausa de 2 segundos
```

### `os` y `pathlib`: archivos y carpetas

```python
from pathlib import Path

carpeta = Path(".")
for archivo in carpeta.iterdir():
    print(archivo.name)

Path("nueva_carpeta").mkdir(exist_ok=True)
print(Path("notas.txt").exists())
```

## Crear tus propios módulos

Cualquier archivo `.py` es un módulo. Crea `utilidades.py`:

```python
# utilidades.py
def saludar(nombre):
    return f"Hola, {nombre}"

IVA = 0.21
```

Y en otro archivo **en la misma carpeta**:

```python
# programa.py
import utilidades

print(utilidades.saludar("Ana"))
print(100 * (1 + utilidades.IVA))
```

### ¿Qué es `if __name__ == "__main__":`?

Cuando importas un módulo, Python **ejecuta todo su código**. Esta línea evita que se ejecute la parte "principal"
cuando el archivo se importa, y solo la ejecuta cuando lo lanzas directamente con `python utilidades.py`.

```python
def saludar(nombre):
    return f"Hola, {nombre}"

if __name__ == "__main__":
    print(saludar("prueba"))   # solo al ejecutarlo directamente
```

## Librerías externas con `pip`

Hay más de 500.000 librerías creadas por la comunidad en [pypi.org](https://pypi.org). Se instalan desde la terminal:

```
pip install requests
```

(En macOS/Linux puede ser `pip3` o `python3 -m pip install requests`).

```python
import requests
respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)
```

Algunas librerías famosas: `requests` (internet), `pandas` (datos), `matplotlib` (gráficos),
`flask` (webs), `pygame` (juegos), `openpyxl` (Excel).

### Entornos virtuales (recomendado cuando empieces proyectos)

Un entorno virtual es una carpeta aislada con las librerías de **un** proyecto, para que no se mezclen entre proyectos:

```
python -m venv .venv
# Activar en Windows:
.venv\Scripts\activate
# Activar en macOS/Linux:
source .venv/bin/activate

pip install requests
```

## 🏋️ Ejercicios

1. **Piedra, papel o tijera** contra el ordenador, al mejor de 5 rondas.
2. Genera una contraseña aleatoria de la longitud que pida el usuario, con letras, números y símbolos. (Pista: `import string`, `string.ascii_letters`, `string.digits`, `string.punctuation`).
3. Pide tu fecha de nacimiento (`dd/mm/aaaa`) y muestra cuántos días has vivido y qué día de la semana naciste. (Pista: `datetime.strptime`).
4. Crea un módulo `geometria.py` con funciones de áreas y perímetros, e impórtalo desde otro archivo.
5. Simula 10.000 lanzamientos de dos dados y muestra cuántas veces sale cada suma (2 a 12).

💡 Solución: [`soluciones/12_modulos.py`](../soluciones/12_modulos.py) y [`soluciones/geometria.py`](../soluciones/geometria.py)

➡️ Siguiente: [Módulo 13 · Programación orientada a objetos](13-poo.md)
