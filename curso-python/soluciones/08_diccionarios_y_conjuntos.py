# Soluciones · Módulo 08 · Diccionarios y conjuntos


def ejercicio_1():
    libro = {"título": "Cien años de soledad", "autor": "Gabriel García Márquez",
             "año": 1967, "páginas": 471}
    for clave, valor in libro.items():
        print(f"{clave.capitalize()}: {valor}")


def ejercicio_2():
    agenda = {}
    while True:
        print("\n1. Añadir  2. Buscar  3. Borrar  4. Ver todos  5. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre = input("Nombre: ")
            agenda[nombre] = input("Teléfono: ")
        elif opcion == "2":
            nombre = input("Nombre: ")
            print(agenda.get(nombre, "No existe ese contacto"))
        elif opcion == "3":
            nombre = input("Nombre: ")
            if nombre in agenda:
                del agenda[nombre]
                print("Borrado")
            else:
                print("No existe ese contacto")
        elif opcion == "4":
            for nombre, telefono in sorted(agenda.items()):
                print(f"{nombre}: {telefono}")
        elif opcion == "5":
            break


def ejercicio_3():
    frase = input("Frase: ").lower()
    conteo = {}
    for letra in frase:
        if letra != " ":
            conteo[letra] = conteo.get(letra, 0) + 1
    for letra, veces in sorted(conteo.items()):
        print(f"{letra}: {veces}")


def ejercicio_4():
    precios = {"pan": 1.20, "leche": 0.95, "queso": 4.50, "café": 3.25, "agua": 0.60}
    print("Productos de más de 2 €:")
    for producto, precio in precios.items():
        if precio > 2:
            print(f"  {producto}: {precio:.2f} €")
    media = sum(precios.values()) / len(precios)
    print(f"Precio medio: {media:.2f} €")


def ejercicio_5():
    amigos_ana = {"Luis", "Marta", "Pablo", "Sara"}
    amigos_juan = {"Marta", "Pedro", "Sara", "Elena"}
    print("En común:", amigos_ana & amigos_juan)
    print("Solo de Ana:", amigos_ana - amigos_juan)
    print("Solo de Juan:", amigos_juan - amigos_ana)


def ejercicio_6():
    alumnos = [
        {"nombre": "Ana", "nota": 8.5},
        {"nombre": "Luis", "nota": 4.0},
        {"nombre": "Marta", "nota": 9.2},
        {"nombre": "Pablo", "nota": 5.5},
    ]
    media = sum(a["nota"] for a in alumnos) / len(alumnos)
    print(f"Media de la clase: {media:.2f}")
    aprobados = [a["nombre"] for a in alumnos if a["nota"] >= 5]
    print("Aprobados:", ", ".join(aprobados))


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
