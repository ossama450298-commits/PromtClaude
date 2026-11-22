# Módulo de ejemplo para el ejercicio 4 del Módulo 12.
# Se importa desde 12_modulos.py con:  import geometria
import math


def area_rectangulo(base, altura):
    return base * altura


def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)


def area_circulo(radio):
    return math.pi * radio ** 2


def perimetro_circulo(radio):
    return 2 * math.pi * radio


def area_triangulo(base, altura):
    return base * altura / 2


if __name__ == "__main__":
    # Solo se ejecuta si lanzas "python geometria.py", no al importarlo.
    print("Prueba: área de un círculo de radio 1 =", area_circulo(1))
