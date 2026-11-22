# Soluciones · Módulo 02 · Variables y tipos de datos
# Ejecuta: python 02_variables_y_tipos.py  y elige un ejercicio.


def ejercicio_1():
    nombre = "Ana"
    edad = 30
    altura = 1.68
    print(nombre, type(nombre))
    print(edad, type(edad))
    print(altura, type(altura))


def ejercicio_2():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print("La suma es", a + b)


def ejercicio_3():
    nacimiento = int(input("¿En qué año naciste? "))
    print("En 2030 tendrás unos", 2030 - nacimiento, "años")


def ejercicio_4():
    celsius = float(input("Temperatura en °C: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(celsius, "°C son", fahrenheit, "°F")


def ejercicio_5():
    a = 5
    b = 8
    # Forma clásica, con una variable auxiliar:
    aux = a
    a = b
    b = aux
    print("a =", a, "b =", b)
    # Forma "pythónica" (en una línea):
    a, b = b, a
    print("Otra vez intercambiados: a =", a, "b =", b)


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
