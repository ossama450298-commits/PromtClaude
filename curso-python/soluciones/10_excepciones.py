# Soluciones · Módulo 10 · Errores y excepciones


# Ejercicio 1
def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Eso no es un número válido.")


# Ejercicio 2
def division():
    try:
        a = float(input("Dividendo: "))
        b = float(input("Divisor: "))
        print("Resultado:", a / b)
    except ValueError:
        print("Tienes que escribir números")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")


# Ejercicio 3
def sumar_validos(valores):
    total = 0
    errores = 0
    for v in valores:
        try:
            total += float(v)
        except ValueError:
            errores += 1
    return total, errores


# Ejercicio 4
def obtener_precio(precios, producto):
    if producto not in precios:
        raise KeyError(f"El producto '{producto}' no existe")
    return precios[producto]


# Ejercicio 5
def crear_usuario(nombre, edad):
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    if not 0 <= edad <= 120:
        raise ValueError("La edad debe estar entre 0 y 120")
    return {"nombre": nombre, "edad": edad}


def main():
    n = pedir_float("Escribe un número decimal: ")
    print("Has escrito", n)

    division()

    total, errores = sumar_validos(["10", "20", "abc", "30", "", "5"])
    print(f"Suma: {total}  —  valores no válidos: {errores}")

    precios = {"pan": 1.2, "leche": 0.95}
    try:
        print(obtener_precio(precios, "pan"))
        print(obtener_precio(precios, "chocolate"))
    except KeyError as e:
        print("Error:", e)

    for nombre, edad in [("Ana", 30), ("", 20), ("Luis", 150)]:
        try:
            print("Creado:", crear_usuario(nombre, edad))
        except ValueError as e:
            print("No se pudo crear el usuario:", e)


if __name__ == "__main__":
    main()
