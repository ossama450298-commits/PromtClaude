# 🏁 Proyecto final · Gestor de gastos personales

Vas a construir un programa de consola para **apuntar tus gastos**, verlos por categoría y guardarlos en un archivo
para que no se pierdan. Usarás prácticamente todo lo que has aprendido:

| Concepto | Dónde lo usarás |
|----------|-----------------|
| Variables, tipos, `input` | Pedir importe, categoría, descripción |
| Condicionales y bucles | El menú principal |
| Listas y diccionarios | Guardar los gastos y agrupar por categoría |
| Funciones | Una función por cada opción del menú |
| Excepciones | Validar importes y fechas |
| Archivos JSON | Guardar y cargar los datos |
| Módulos (`datetime`) | La fecha de cada gasto |
| Clases | `Gasto` y `GestorGastos` |

## Lo que debe hacer

```
===== GESTOR DE GASTOS =====
1. Añadir gasto
2. Ver todos los gastos
3. Ver resumen por categoría
4. Ver gastos de un mes
5. Eliminar un gasto
6. Salir
```

1. **Añadir gasto:** pide importe (validado, positivo), categoría (comida, transporte, ocio…), descripción
   y fecha (si se deja vacía, la de hoy).
2. **Ver todos:** tabla numerada con fecha, categoría, descripción e importe, y el total.
3. **Resumen por categoría:** total gastado en cada categoría y su porcentaje, de mayor a menor.
4. **Gastos de un mes:** pide mes y año y muestra solo esos gastos y su total.
5. **Eliminar:** muestra la lista y borra el número elegido (con confirmación).
6. **Salir:** guarda en `gastos.json`. Al volver a abrir el programa los gastos siguen ahí.

## Cómo abordarlo (paso a paso)

No intentes hacerlo todo de golpe. Ve por fases y **prueba cada una antes de seguir**:

1. **Fase 1:** el menú con un bucle `while` que solo muestra "Opción X elegida" y sale con 6.
2. **Fase 2:** añadir gastos a una lista de diccionarios y mostrarlos (opciones 1 y 2).
3. **Fase 3:** validación con `try/except` para que un importe mal escrito no rompa el programa.
4. **Fase 4:** guardar y cargar con JSON.
5. **Fase 5:** resumen por categoría y filtro por mes (opciones 3 y 4).
6. **Fase 6:** eliminar gastos.
7. **Fase 7 (opcional):** reorganiza el código en las clases `Gasto` y `GestorGastos`.

## Ideas para ampliarlo

- Establecer un **presupuesto mensual** y avisar cuando se supere.
- **Exportar a CSV** para abrirlo en Excel.
- Añadir **ingresos** además de gastos y mostrar el balance.
- Hacer un **gráfico** de barras con `matplotlib` (`pip install matplotlib`).

## Solución

Intenta hacerlo tú primero. Cuando termines (o si te atascas de verdad) compara con
[`gestor_gastos.py`](gestor_gastos.py). Ejecútalo con:

```
python gestor_gastos.py
```

No pasa nada si tu solución es distinta: en programación hay muchas formas correctas de resolver lo mismo.
