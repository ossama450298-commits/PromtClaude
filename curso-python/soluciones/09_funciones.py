# Soluciones · Módulo 09 · Funciones
import math


# Ejercicio 1
def area_circulo(radio):
    """Devuelve el área de un círculo."""
    return math.pi * radio ** 2


# Ejercicio 2
def es_primo(n):
    """Devuelve True si n es un número primo."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


# Ejercicio 3
def contar_vocales(texto):
    """Cuenta las vocales (con o sin tilde) de un texto."""
    total = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóú":
            total += 1
    return total


# Ejercicio 4
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


# Ejercicio 5
def estadisticas(lista):
    """Devuelve (media, mínimo, máximo) de una lista de números."""
    return sum(lista) / len(lista), min(lista), max(lista)


# Ejercicio 6
def pedir_entero(mensaje, minimo, maximo):
    """Pide un entero hasta que esté entre minimo y maximo (incluidos)."""
    while True:
        texto = input(mensaje)
        if texto.lstrip("-").isdigit():
            n = int(texto)
            if minimo <= n <= maximo:
                return n
        print(f"Escribe un número entero entre {minimo} y {maximo}.")


# Ejercicio 7
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a / b


def calculadora():
    operaciones = {"+": sumar, "-": restar, "*": multiplicar, "/": dividir}
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    op = input("Operación (+ - * /): ")
    if op in operaciones:
        print("Resultado:", operaciones[op](a, b))
    else:
        print("Operación no válida")


def main():
    print("Área de un círculo de radio 3:", round(area_circulo(3), 2))
    print("Primos del 1 al 50:", [n for n in range(1, 51) if es_primo(n)])
    print("Vocales en 'Programación en Python':", contar_vocales("Programación en Python"))
    print("25 °C =", celsius_a_fahrenheit(25), "°F")
    print("77 °F =", fahrenheit_a_celsius(77), "°C")
    media, minimo, maximo = estadisticas([4, 8, 15, 16, 23, 42])
    print(f"Media: {media:.2f}  Mínimo: {minimo}  Máximo: {maximo}")
    nota = pedir_entero("Pon una nota del 0 al 10: ", 0, 10)
    print("Has puesto un", nota)
    calculadora()


if __name__ == "__main__":
    main()
