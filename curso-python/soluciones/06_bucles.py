# Soluciones · Módulo 06 · Bucles


def ejercicio_1():
    for i in range(10, 0, -1):
        print(i)
    print("¡Despegue!")


def ejercicio_2():
    n = int(input("Número: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def ejercicio_3():
    total = 0
    for n in range(2, 101, 2):
        total += n
    print("Suma de los pares del 1 al 100:", total)


def ejercicio_4():
    cantidad = 0
    suma = 0
    while True:
        n = float(input("Número (0 para terminar): "))
        if n == 0:
            break
        cantidad += 1
        suma += n
    print("Has escrito", cantidad, "números")
    print("Suma:", suma)
    if cantidad > 0:
        print("Media:", suma / cantidad)


def ejercicio_5():
    secreto = 37
    intentos = 0
    while True:
        n = int(input("Adivina el número (1-100): "))
        intentos += 1
        if n < secreto:
            print("Más alto")
        elif n > secreto:
            print("Más bajo")
        else:
            print(f"¡Correcto! Lo has conseguido en {intentos} intentos")
            break


def ejercicio_6():
    altura = int(input("Altura: "))
    for i in range(1, altura + 1):
        print("*" * i)


def ejercicio_7():
    for n in range(1, 31):
        if n % 15 == 0:          # múltiplo de 3 y de 5 → va primero
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4,
                  ejercicio_5, ejercicio_6, ejercicio_7]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
