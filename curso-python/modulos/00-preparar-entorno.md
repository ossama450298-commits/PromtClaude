# Módulo 00 · Preparar tu entorno

## ¿Qué es programar?

Programar es escribir **instrucciones** para que el ordenador las ejecute, una detrás de otra.
Python es un **lenguaje de programación**: una forma de escribir esas instrucciones que es fácil de leer
para las personas y que el ordenador sabe interpretar.

Python se usa para páginas web, análisis de datos, inteligencia artificial, automatizar tareas, videojuegos…
y es uno de los mejores lenguajes para empezar.

## 1. Instalar Python

### Windows
1. Entra en [python.org/downloads](https://www.python.org/downloads/) y descarga la última versión (3.12 o superior).
2. Ejecuta el instalador y **marca la casilla "Add Python to PATH"** antes de pulsar *Install Now*. ⚠️ Es importante.
3. Abre la aplicación **Símbolo del sistema** (busca `cmd`) y escribe:
   ```
   python --version
   ```
   Debería mostrar algo como `Python 3.13.0`.

### macOS
1. Descarga el instalador desde [python.org/downloads](https://www.python.org/downloads/).
2. Abre la app **Terminal** y escribe `python3 --version`.

### Linux
Normalmente ya viene instalado. Comprueba con `python3 --version`.

> 💡 En macOS y Linux el comando suele ser `python3` en lugar de `python`. En este curso escribiremos
> `python`; usa el que funcione en tu sistema.

## 2. Instalar un editor de código

Recomiendo **Visual Studio Code** (gratis): [code.visualstudio.com](https://code.visualstudio.com/)

1. Instálalo y ábrelo.
2. Ve a la pestaña de **Extensiones** (icono de cuadraditos a la izquierda) y busca **Python** (de Microsoft). Instálala.

> ¿No quieres instalar nada todavía? Puedes practicar en el navegador con
> [replit.com](https://replit.com) o [programiz.com/python-programming/online-compiler](https://www.programiz.com/python-programming/online-compiler/).

## 3. Tu primer programa

1. Crea una carpeta llamada `aprendiendo-python`.
2. Ábrela en VS Code (*Archivo → Abrir carpeta*).
3. Crea un archivo llamado `hola.py` (la extensión `.py` indica que es Python).
4. Escribe dentro:
   ```python
   print("¡Hola, mundo!")
   ```
5. Guarda y pulsa el botón ▶️ arriba a la derecha, o en la terminal escribe:
   ```
   python hola.py
   ```

Si ves `¡Hola, mundo!` en pantalla: **enhorabuena, ya eres programador/a.** 🎉

## 4. El modo interactivo

Si en la terminal escribes solo `python` (sin archivo), entras en el **modo interactivo**, que muestra `>>>`.
Ahí puedes probar instrucciones sueltas y ver el resultado al momento:

```python
>>> 2 + 3
5
>>> print("Probando")
Probando
```

Para salir escribe `exit()`. Es muy útil para experimentar.

## ✅ Antes de seguir

- [ ] `python --version` funciona en tu terminal.
- [ ] Has ejecutado `hola.py` y has visto el mensaje.
- [ ] Has probado el modo interactivo.

➡️ Siguiente: [Módulo 01 · Primeros pasos](01-primeros-pasos.md)
