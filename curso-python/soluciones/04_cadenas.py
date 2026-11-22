# Soluciones · Módulo 04 · Cadenas de texto


def ejercicio_1():
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    print(f"Bienvenido/a, {apellido.upper()}, {nombre.capitalize()}")


def ejercicio_2():
    palabra = input("Palabra: ")
    print(f"Primera letra: {palabra[0]}")
    print(f"Última letra: {palabra[-1]}")
    print(f"Número de letras: {len(palabra)}")


def ejercicio_3():
    frase = input("Frase: ")
    print(frase[::-1])


def ejercicio_4():
    frase = input("Frase: ")
    print("La letra 'a' aparece", frase.lower().count("a"), "veces")


def ejercicio_5():
    email = input("Email: ")
    posicion = email.find("@")
    print("Usuario:", email[:posicion])
    print("Dominio:", email[posicion + 1:])
    # Alternativa: usuario, dominio = email.split("@")


def ejercicio_6():
    palabra = input("Palabra: ").lower().replace(" ", "")
    print(palabra == palabra[::-1])


if __name__ == "__main__":
    ejercicios = [ejercicio_1, ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_6]
    n = int(input(f"¿Qué ejercicio quieres ejecutar? (1-{len(ejercicios)}): "))
    ejercicios[n - 1]()
