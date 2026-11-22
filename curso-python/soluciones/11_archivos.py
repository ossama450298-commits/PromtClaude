# Soluciones · Módulo 11 · Archivos
# Los archivos se crean en la carpeta desde la que ejecutes el programa.
import csv
import json


def ejercicio_1():
    with open("frases.txt", "w", encoding="utf-8") as f:
        for i in range(3):
            f.write(input(f"Frase {i + 1}: ") + "\n")
    with open("frases.txt", encoding="utf-8") as f:
        for numero, linea in enumerate(f, start=1):
            print(f"{numero}. {linea.strip()}")


def contar(nombre_archivo):
    """Ejercicio 2: devuelve (líneas, palabras, caracteres) de un archivo."""
    with open(nombre_archivo, encoding="utf-8") as f:
        texto = f.read()
    return len(texto.splitlines()), len(texto.split()), len(texto)


def ejercicio_2():
    nombre = input("Nombre del archivo: ")
    try:
        lineas, palabras, caracteres = contar(nombre)
        print(f"Líneas: {lineas}  Palabras: {palabras}  Caracteres: {caracteres}")
    except FileNotFoundError:
        print("No existe ese archivo")


def ejercicio_3():
    from datetime import datetime
    entrada = input("¿Qué tal ha ido el día? ")
    with open("diario.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now():%d/%m/%Y %H:%M}] {entrada}\n")
    print("\n--- Tu diario ---")
    with open("diario.txt", encoding="utf-8") as f:
        print(f.read())


ARCHIVO_AGENDA = "agenda.json"


def cargar_agenda():
    try:
        with open(ARCHIVO_AGENDA, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def guardar_agenda(agenda):
    with open(ARCHIVO_AGENDA, "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=2, ensure_ascii=False)


def ejercicio_4():
    agenda = cargar_agenda()
    print(f"Agenda cargada con {len(agenda)} contactos")
    while True:
        print("\n1. Añadir  2. Buscar  3. Borrar  4. Ver todos  5. Guardar y salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            agenda[nombre] = input("Teléfono: ")
        elif opcion == "2":
            print(agenda.get(input("Nombre: "), "No existe ese contacto"))
        elif opcion == "3":
            agenda.pop(input("Nombre: "), None)
        elif opcion == "4":
            for nombre, tel in sorted(agenda.items()):
                print(f"{nombre}: {tel}")
        elif opcion == "5":
            guardar_agenda(agenda)
            print("Guardado.")
            break


def ejercicio_5():
    productos = [("pan", 1.20), ("leche", 0.95), ("queso", 4.50)]
    with open("productos.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["producto", "precio"])
        escritor.writerows(productos)

    total = 0
    with open("productos.csv", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            print(f"{fila['producto']}: {float(fila['precio']):.2f} €")
            total += float(fila["precio"])
    print(f"Total: {total:.2f} €")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
