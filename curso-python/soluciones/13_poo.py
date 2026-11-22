# Soluciones · Módulo 13 · Programación orientada a objetos
import random


# Ejercicio 1
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura


# Ejercicio 2
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad

    def __str__(self):
        return f"{self.nombre} — {self.cantidad} uds x {self.precio:.2f} € = {self.valor_total():.2f} €"


# Ejercicio 3
class Inventario:
    def __init__(self):
        self.productos = []

    def anadir(self, producto):
        self.productos.append(producto)

    def buscar(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    def eliminar(self, nombre):
        producto = self.buscar(nombre)
        if producto:
            self.productos.remove(producto)
            return True
        return False

    def valor_total(self):
        return sum(p.valor_total() for p in self.productos)

    def mostrar(self):
        for p in self.productos:
            print(" ", p)
        print(f"  Valor total del inventario: {self.valor_total():.2f} €")


# Ejercicio 4
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def transferir(self, otra_cuenta, cantidad):
        self.retirar(cantidad)        # si no hay saldo, lanza el error y no sigue
        otra_cuenta.ingresar(cantidad)

    def __str__(self):
        return f"Cuenta de {self.titular}: {self.saldo:.2f} €"


# Ejercicio 5
class Personaje:
    def __init__(self, nombre, vida=100, ataque=10):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def esta_vivo(self):
        return self.vida > 0

    def calcular_danio(self):
        return self.ataque

    def atacar(self, otro):
        danio = self.calcular_danio()
        otro.vida = max(0, otro.vida - danio)
        print(f"{self.nombre} ataca a {otro.nombre} y le quita {danio}. "
              f"{otro.nombre} queda con {otro.vida} de vida.")


class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=150, ataque=12)


class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=90, ataque=0)

    def calcular_danio(self):
        return random.randint(5, 30)


def combate(a, b):
    turno = 1
    atacante, defensor = a, b
    while a.esta_vivo() and b.esta_vivo():
        print(f"--- Turno {turno} ---")
        atacante.atacar(defensor)
        atacante, defensor = defensor, atacante
        turno += 1
    ganador = a if a.esta_vivo() else b
    print(f"\n🏆 ¡{ganador.nombre} gana el combate!")


def main():
    r = Rectangulo(4, 4)
    print("Rectángulo:", r.area(), r.perimetro(), "¿cuadrado?", r.es_cuadrado())

    inv = Inventario()
    inv.anadir(Producto("Teclado", 25.0, 4))
    inv.anadir(Producto("Ratón", 12.5, 10))
    inv.anadir(Producto("Monitor", 150.0, 2))
    inv.eliminar("ratón")
    print("Inventario:")
    inv.mostrar()

    ana = CuentaBancaria("Ana", 100)
    luis = CuentaBancaria("Luis", 20)
    ana.transferir(luis, 30)
    print(ana, "|", luis)
    try:
        luis.transferir(ana, 1000)
    except ValueError as e:
        print("Transferencia rechazada:", e)

    print()
    combate(Guerrero("Brunilda"), Mago("Merlín"))


if __name__ == "__main__":
    main()
