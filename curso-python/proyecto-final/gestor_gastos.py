"""
Gestor de gastos personales — Proyecto final del curso de Python.

Ejecuta:  python gestor_gastos.py
Los datos se guardan en gastos.json, en la carpeta desde la que lo ejecutes.
"""
import json
from datetime import date, datetime

ARCHIVO = "gastos.json"
FORMATO_FECHA = "%d/%m/%Y"


class Gasto:
    """Un gasto individual."""

    def __init__(self, importe, categoria, descripcion, fecha):
        self.importe = importe
        self.categoria = categoria
        self.descripcion = descripcion
        self.fecha = fecha  # objeto date

    def a_diccionario(self):
        """Convierte el gasto a un diccionario que se puede guardar en JSON."""
        return {
            "importe": self.importe,
            "categoria": self.categoria,
            "descripcion": self.descripcion,
            "fecha": self.fecha.isoformat(),  # "2026-11-22"
        }

    @staticmethod
    def desde_diccionario(datos):
        """Crea un Gasto a partir de un diccionario leído del JSON."""
        return Gasto(
            datos["importe"],
            datos["categoria"],
            datos["descripcion"],
            date.fromisoformat(datos["fecha"]),
        )

    def __str__(self):
        return (f"{self.fecha.strftime(FORMATO_FECHA)}  {self.categoria:<12} "
                f"{self.descripcion:<25} {self.importe:>9.2f} €")


class GestorGastos:
    """Guarda la lista de gastos y las operaciones sobre ella."""

    def __init__(self, archivo):
        self.archivo = archivo
        self.gastos = []

    # --- Persistencia ---
    def cargar(self):
        try:
            with open(self.archivo, encoding="utf-8") as f:
                self.gastos = [Gasto.desde_diccionario(d) for d in json.load(f)]
        except FileNotFoundError:
            self.gastos = []
        except (json.JSONDecodeError, KeyError, ValueError):
            print(f"⚠️  El archivo {self.archivo} está dañado; se empieza con una lista vacía.")
            self.gastos = []

    def guardar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump([g.a_diccionario() for g in self.gastos], f, indent=2, ensure_ascii=False)

    # --- Operaciones ---
    def anadir(self, gasto):
        self.gastos.append(gasto)
        self.gastos.sort(key=lambda g: g.fecha)

    def eliminar(self, indice):
        return self.gastos.pop(indice)

    def total(self, gastos=None):
        gastos = self.gastos if gastos is None else gastos
        return sum(g.importe for g in gastos)

    def por_categoria(self):
        resumen = {}
        for g in self.gastos:
            resumen[g.categoria] = resumen.get(g.categoria, 0) + g.importe
        return dict(sorted(resumen.items(), key=lambda par: par[1], reverse=True))

    def del_mes(self, mes, anio):
        return [g for g in self.gastos if g.fecha.month == mes and g.fecha.year == anio]


# ---------- Funciones para pedir datos ----------

def pedir_importe():
    while True:
        texto = input("Importe (€): ").replace(",", ".").strip()
        try:
            importe = float(texto)
            if importe <= 0:
                print("El importe debe ser mayor que 0.")
                continue
            return round(importe, 2)
        except ValueError:
            print("Escribe un número, por ejemplo 12.50")


def pedir_fecha():
    while True:
        texto = input(f"Fecha (dd/mm/aaaa, vacío = hoy): ").strip()
        if not texto:
            return date.today()
        try:
            return datetime.strptime(texto, FORMATO_FECHA).date()
        except ValueError:
            print("Fecha no válida. Ejemplo: 05/11/2026")


def pedir_entero(mensaje, minimo, maximo):
    while True:
        try:
            n = int(input(mensaje))
            if minimo <= n <= maximo:
                return n
        except ValueError:
            pass
        print(f"Escribe un número entre {minimo} y {maximo}.")


def mostrar_lista(gastos, total):
    if not gastos:
        print("No hay gastos que mostrar.")
        return
    print(f"\n {'#':>3}  {'Fecha':<10}  {'Categoría':<12} {'Descripción':<25} {'Importe':>11}")
    print(" " + "-" * 68)
    for i, g in enumerate(gastos, start=1):
        print(f" {i:>3}  {g}")
    print(" " + "-" * 68)
    print(f" {'TOTAL':>56} {total:>9.2f} €")


# ---------- Opciones del menú ----------

def opcion_anadir(gestor):
    importe = pedir_importe()
    categoria = input("Categoría (comida, transporte, ocio...): ").strip().lower() or "otros"
    descripcion = input("Descripción: ").strip() or "-"
    fecha = pedir_fecha()
    gestor.anadir(Gasto(importe, categoria, descripcion, fecha))
    gestor.guardar()
    print("✅ Gasto añadido.")


def opcion_ver_todos(gestor):
    mostrar_lista(gestor.gastos, gestor.total())


def opcion_resumen(gestor):
    total = gestor.total()
    if total == 0:
        print("Todavía no hay gastos.")
        return
    print("\nResumen por categoría:")
    for categoria, suma in gestor.por_categoria().items():
        porcentaje = suma / total * 100
        barra = "█" * round(porcentaje / 4)
        print(f"  {categoria:<12} {suma:>9.2f} €  {porcentaje:5.1f}%  {barra}")
    print(f"  {'TOTAL':<12} {total:>9.2f} €")


def opcion_mes(gestor):
    hoy = date.today()
    mes = pedir_entero(f"Mes (1-12): ", 1, 12)
    anio = pedir_entero(f"Año: ", 1900, hoy.year + 1)
    gastos = gestor.del_mes(mes, anio)
    mostrar_lista(gastos, gestor.total(gastos))


def opcion_eliminar(gestor):
    if not gestor.gastos:
        print("No hay gastos que eliminar.")
        return
    opcion_ver_todos(gestor)
    n = pedir_entero("Número del gasto a eliminar (0 = cancelar): ", 0, len(gestor.gastos))
    if n == 0:
        return
    gasto = gestor.gastos[n - 1]
    if input(f"¿Eliminar «{gasto.descripcion}» ({gasto.importe:.2f} €)? (s/n): ").lower() == "s":
        gestor.eliminar(n - 1)
        gestor.guardar()
        print("🗑️  Gasto eliminado.")


def main():
    gestor = GestorGastos(ARCHIVO)
    gestor.cargar()
    print(f"Se han cargado {len(gestor.gastos)} gastos.")

    opciones = {
        "1": opcion_anadir,
        "2": opcion_ver_todos,
        "3": opcion_resumen,
        "4": opcion_mes,
        "5": opcion_eliminar,
    }

    while True:
        print("\n===== GESTOR DE GASTOS =====")
        print("1. Añadir gasto")
        print("2. Ver todos los gastos")
        print("3. Ver resumen por categoría")
        print("4. Ver gastos de un mes")
        print("5. Eliminar un gasto")
        print("6. Salir")
        eleccion = input("Elige una opción: ").strip()

        if eleccion == "6":
            gestor.guardar()
            print("Datos guardados. ¡Hasta pronto! 👋")
            break
        elif eleccion in opciones:
            opciones[eleccion](gestor)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
