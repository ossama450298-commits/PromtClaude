# Soluciones · Módulo 05 · Condicionales


def ejercicio_1():
    n = float(input("Número: "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Cero")


def ejercicio_2():
    n = int(input("Número: "))
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")


def ejercicio_3():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
    if a >= b and a >= c:
        mayor = a
    elif b >= c:
        mayor = b
    else:
        mayor = c
    print("El mayor es", mayor)


def ejercicio_4():
    anio = int(input("Año: "))
    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(anio, "es bisiesto")
    else:
        print(anio, "no es bisiesto")


def ejercicio_5():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+ - * /): ")
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b == 0:
            print("No se puede dividir entre cero")
        else:
            print(a / b)
    else:
        print("Operación no válida")


def ejercicio_6():
    usuario_correcto = "admin"
    clave_correcta = "1234"
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    if usuario != usuario_correcto:
        print("Usuario incorrecto")
    elif clave != clave_correcta:
        print("Contraseña incorrecta")
    else:
        print("Acceso concedido")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
