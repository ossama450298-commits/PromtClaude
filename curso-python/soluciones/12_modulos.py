# Soluciones · Módulo 12 · Módulos y librerías
import random
import string
from datetime import datetime, date

import geometria  # nuestro propio módulo (geometria.py, en esta misma carpeta)


def ejercicio_1():
    opciones = ["piedra", "papel", "tijera"]
    gana_a = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}
    yo = ordenador = 0
    while yo < 3 and ordenador < 3:          # al mejor de 5 = el primero que gane 3
        jugada = input("piedra, papel o tijera: ").lower().strip()
        if jugada not in opciones:
            print("Jugada no válida")
            continue
        rival = random.choice(opciones)
        print("El ordenador elige", rival)
        if jugada == rival:
            print("Empate")
        elif gana_a[jugada] == rival:
            print("¡Ganas la ronda!")
            yo += 1
        else:
            print("Pierdes la ronda")
            ordenador += 1
        print(f"Marcador: tú {yo} - {ordenador} ordenador\n")
    print("🏆 ¡Has ganado!" if yo == 3 else "💻 Gana el ordenador")


def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))


def ejercicio_2():
    longitud = int(input("Longitud de la contraseña: "))
    print(generar_contrasena(longitud))


def ejercicio_3():
    texto = input("Fecha de nacimiento (dd/mm/aaaa): ")
    nacimiento = datetime.strptime(texto, "%d/%m/%Y").date()
    dias = (date.today() - nacimiento).days
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    print(f"Has vivido {dias} días")
    print(f"Naciste en {dias_semana[nacimiento.weekday()]}")


def ejercicio_4():
    print("Área rectángulo 3x4:", geometria.area_rectangulo(3, 4))
    print("Perímetro rectángulo 3x4:", geometria.perimetro_rectangulo(3, 4))
    print("Área círculo r=2:", round(geometria.area_circulo(2), 2))
    print("Área triángulo b=6 h=3:", geometria.area_triangulo(6, 3))


def ejercicio_5():
    resultados = {suma: 0 for suma in range(2, 13)}
    for _ in range(10_000):
        suma = random.randint(1, 6) + random.randint(1, 6)
        resultados[suma] += 1
    for suma, veces in resultados.items():
        barra = "█" * (veces // 50)
        print(f"{suma:>2}: {veces:>5} {barra}")


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
