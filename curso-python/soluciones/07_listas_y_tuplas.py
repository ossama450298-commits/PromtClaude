# Soluciones · Módulo 07 · Listas y tuplas


def ejercicio_1():
    notas = [7.5, 9.0, 5.5, 6.8, 8.2]
    print("Nota más alta:", max(notas))
    print("Nota más baja:", min(notas))
    print("Media:", round(sum(notas) / len(notas), 2))


def ejercicio_2():
    palabras = []
    while True:
        p = input("Palabra (o 'fin'): ")
        if p == "fin":
            break
        palabras.append(p)
    print(sorted(palabras))


def ejercicio_3():
    numeros = [3, 8, 1, 9, 4, 7, 2]
    # Con bucle
    mayores = []
    for n in numeros:
        if n > 4:
            mayores.append(n)
    print(mayores)
    # Con list comprehension
    print([n for n in numeros if n > 4])


def ejercicio_4():
    numeros = [1, 2, 2, 3, 4, 4, 4, 5]
    sin_repetir = []
    for n in numeros:
        if n not in sin_repetir:
            sin_repetir.append(n)
    print(sin_repetir)


def ejercicio_5():
    compra = []
    while True:
        print("\n1. Añadir  2. Eliminar  3. Ver lista  4. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            compra.append(input("Producto: "))
        elif opcion == "2":
            producto = input("Producto a eliminar: ")
            if producto in compra:
                compra.remove(producto)
            else:
                print("Ese producto no está en la lista")
        elif opcion == "3":
            if not compra:
                print("La lista está vacía")
            for i, producto in enumerate(compra, start=1):
                print(f"{i}. {producto}")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")


def ejercicio_6():
    personas = [("Ana", 25), ("Luis", 15), ("Marta", 40), ("Pablo", 17)]
    for nombre, edad in personas:
        if edad >= 18:
            print(nombre)


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
