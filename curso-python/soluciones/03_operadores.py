# Soluciones · Módulo 03 · Operadores


def ejercicio_1():
    total = int(input("Segundos: "))
    horas = total // 3600
    resto = total % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(horas, "h", minutos, "min", segundos, "s")


def ejercicio_2():
    precio = float(input("Precio: "))
    descuento = float(input("Descuento (%): "))
    final = precio - precio * descuento / 100
    print("Precio final:", round(final, 2))


def ejercicio_3():
    n = int(input("Número: "))
    print(n % 2 == 0)


def ejercicio_4():
    edad = int(input("Edad: "))
    print(18 <= edad <= 65)


def ejercicio_5():
    r = float(input("Radio: "))
    area = 3.14159 * r ** 2
    print("Área:", round(area, 2))


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
