# guiapresupuesto
GUIAPRESUPUESTAL PROCEDIMIENTOS

Herramienta personal para ordenar ingresos y gastos y salir de deudas.

- `DIAGNOSTICO.md`: situación actual y plan recomendado.
- `NEGOCIACION.md`: cómo negociar la deuda en mora con el banco y con las personas.
- `INGRESOS_EXTRA.md`: cómo generar más ingresos como ingeniero de software.
- `datos.json`: ingresos, gastos, deudas y escenarios de negociación. Edítalo con tus números reales.
- `planificador.py`: calcula el flujo de caja y simula el pago de deudas en cada escenario de negociación.

```bash
python3 planificador.py            # escenarios con lo que hoy queda, +2M y +4M
python3 planificador.py 4000000    # ¿qué pasa si destino 4M al mes a deudas?
```
