# Módulo 13 · Programación orientada a objetos (POO)

La POO es una forma de organizar el código agrupando **datos** y **funciones** que van juntos.

Piensa en un molde de galletas:
- La **clase** es el molde: define cómo son las galletas.
- Cada **objeto** (o *instancia*) es una galleta hecha con ese molde.

Ya has usado objetos sin saberlo: cada string es un objeto de la clase `str`, y `.upper()` es uno de sus métodos.

## Crear una clase

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # atributos: los datos del objeto
        self.edad = edad

    def ladrar(self):              # métodos: lo que el objeto sabe hacer
        print(f"{self.nombre} dice: ¡Guau!")

    def cumplir_anios(self):
        self.edad += 1


# Crear objetos
toby = Perro("Toby", 3)
luna = Perro("Luna", 5)

toby.ladrar()            # Toby dice: ¡Guau!
print(luna.edad)         # 5
luna.cumplir_anios()
print(luna.edad)         # 6
```

- `class Perro:` define la clase (por convención, nombre con mayúscula inicial).
- `__init__` es el **constructor**: se ejecuta automáticamente al crear un objeto y prepara sus datos.
- `self` es **el propio objeto**. Todos los métodos lo reciben como primer parámetro, pero al llamarlos no lo escribes.

## Un ejemplo más útil

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []

    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.saldo += cantidad
        self.movimientos.append(("ingreso", cantidad))

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad
        self.movimientos.append(("retirada", cantidad))

    def __str__(self):
        return f"Cuenta de {self.titular}: {self.saldo:.2f} €"


cuenta = CuentaBancaria("Ana", 100)
cuenta.ingresar(50)
cuenta.retirar(30)
print(cuenta)              # Cuenta de Ana: 120.00 €
print(cuenta.movimientos)
```

`__str__` define cómo se ve el objeto cuando lo imprimes con `print`.

La ventaja: los datos (`saldo`) y las reglas para cambiarlos (`retirar` no deja quedarse en negativo) viven juntos.

## Herencia

Una clase puede **heredar** de otra: recibe todo lo suyo y puede añadir o cambiar cosas.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

    def presentarse(self):
        print(f"Soy {self.nombre} y digo {self.hablar()}")


class Gato(Animal):
    def hablar(self):            # sobrescribe el método del padre
        return "¡Miau!"


class Vaca(Animal):
    def hablar(self):
        return "¡Muuu!"


for animal in [Gato("Misi"), Vaca("Lola")]:
    animal.presentarse()
# Soy Misi y digo ¡Miau!
# Soy Lola y digo ¡Muuu!
```

Si la clase hija tiene su propio `__init__`, llama al del padre con `super()`:

```python
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.ingresar(self.saldo * self.interes)
```

## ¿Cuándo usar clases?

Cuando tienes "cosas" con **datos propios** y **comportamientos**: un usuario, un producto, un personaje de un juego,
una tarea… Para scripts pequeños, las funciones suelen bastar. No hace falta usar clases para todo.

## 🏋️ Ejercicios

1. Crea una clase `Rectangulo` con `base` y `altura`, y métodos `area()`, `perimetro()` y `es_cuadrado()`.
2. Crea una clase `Producto` (nombre, precio, cantidad) con un método `valor_total()` y un `__str__`.
3. Crea una clase `Inventario` que guarde una lista de `Producto` y permita añadir, eliminar por nombre, buscar y calcular el valor total del inventario.
4. Usa la `CuentaBancaria` del ejemplo: crea dos cuentas y añade un método `transferir(otra_cuenta, cantidad)`.
5. Crea una clase `Personaje` (nombre, vida, ataque) con un método `atacar(otro)`. Crea las subclases `Guerrero` (más vida) y `Mago` (ataque aleatorio). Simula un combate por turnos hasta que uno llegue a 0 de vida.

💡 Solución: [`soluciones/13_poo.py`](../soluciones/13_poo.py)

➡️ Siguiente: [🏁 Proyecto final](../proyecto-final/README.md)
