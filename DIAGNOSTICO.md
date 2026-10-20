# Diagnóstico financiero y plan de salida de deudas

*Actualizado: 20 de octubre de 2026. Los números salen de `python3 planificador.py`.*

## 1. Flujo de caja mensual

| Concepto | Bancolombia | Tarjeta bono |
|---|---|---|
| Entra (neto) | $4.500.000 | $1.400.000 |
| Arriendo | -$900.000 | |
| Transporte | -$300.000 | |
| Celular | -$500.000 | |
| Mercado | | -$1.000.000 |
| **Queda** | **$2.800.000** | **$400.000** |

## 2. Deudas

| Deuda | Saldo | Tasa mensual | Equivale al año | Interés al mes |
|---|---|---|---|---|
| Persona natural | $4.000.000 | 5,00 % | 79,6 % | $200.000 |
| Jonathan, tramo 30M | $30.000.000 | 3,50 % | 51,1 % | $1.050.000 |
| Brandon | $40.000.000 | 3,33 % | 48,2 % | $1.332.000 |
| Jonathan, tramo 10M | $10.000.000 | 2,50 % | 34,5 % | $250.000 |
| Tarjeta de crédito | $4.000.000 | ~2 % *(supuesto, confirmar)* | ~26,8 % | ~$80.000 |
| **Total** | **$88.000.000** | | | **$2.912.000** |

### El problema central

- Te quedan **$2.800.000** para deudas y los intereses suman **$2.912.000**.
- **Faltan unos $112.000 cada mes solo para cubrir intereses**, sin abonar nada a capital.
- Así como está, la deuda **nunca baja**: crece un poco cada mes.
- Casi la mitad del sueldo (49 %) se va en intereses.

## 3. Plan recomendado

### Paso 1. Recortes inmediatos (esta semana)
- **Celular de $500.000 a ~$100.000**: ahorras **$400.000/mes**. Si el valor incluye la cuota de un equipo, revisar cuánto falta y no renovar. Esto solo pasa el balance de negativo a positivo.
- **Usar los $400.000 que sobran en el bono** para todo lo que se pueda (aseo, farmacia, comidas, ropa), así no sale de Bancolombia.
- No usar más la tarjeta de crédito.

Con el recorte del celular quedan **$3.200.000/mes para deudas**.

### Paso 2. Cerrar el crédito bancario de 80M (lo más importante)

Con los 80M se pagan, en este orden: los 4M al 5 %, los 30M de Jonathan, los 40M de Brandon y 6M del tramo de 10M de Jonathan. Quedan pendientes solo **4M de Jonathan al 2,5 %** y la **tarjeta de 4M**.

| Tasa del banco (mensual) | Cuota 60 meses | Destinando 2,8M/mes | Destinando 3,2M/mes |
|---|---|---|---|
| 1,3 % (16,8 % E.A.) | $1.928.000 | libre en **41 meses**, intereses ~$26M | libre en **35 meses**, ~$22M |
| 1,6 % (21,0 % E.A.) | $2.084.000 | 45 meses, ~$36M | 37 meses, ~$29M |
| 1,9 % (25,3 % E.A.) | $2.246.000 | 49 meses, ~$48M | 40 meses, ~$38M |
| 2,2 % (29,8 % E.A.) | $2.414.000 | 54 meses, ~$63M | 43 meses, ~$48M |
| **Sin crédito** (personas) | — | **nunca** | 68 meses, **~$129M** |

Con el crédito pasas de no salir nunca, o de 5,7 años y $129M en intereses, a **3 años y $22–38M**. Por eso **cada punto de tasa que negocies con el banco vale millones**.

Cómo repartir el dinero una vez desembolsado el crédito:
1. Pagar la cuota del banco cada mes, sin falta.
2. Todo lo que sobre va a **Jonathan, 4M restantes** (2,5 %). Se cierra en 4–7 meses.
3. Después, a la **tarjeta de crédito**. Se cierra entre el mes 7 y el 13.
4. Después, **abonos extra a capital del banco** (pedir que se apliquen a *reducir plazo*).

### Paso 3. Fondo de emergencia
Cuando se cierren Jonathan y la tarjeta, separar **$300.000/mes** hasta juntar ~$2.700.000 (un mes de gastos). Así una emergencia no te devuelve a pedir prestado a personas.

### Paso 4. Más ingresos
Ver `INGRESOS_EXTRA.md`. Cada $1.000.000 extra al mes recorta cerca de un año del plan.

## 4. Si el banco no aprueba los 80M
- Pedir lo que aprueben y recoger primero las deudas más caras: 5 % → 3,5 % → 3,33 %.
- Negociar con Jonathan y Brandon bajar la tasa (ver `NEGOCIACION.md`).
- Sin crédito y sin recortes, **no se puede salir**: el recorte del celular y los ingresos extra serían obligatorios.

## 5. Datos que faltan
- **¿Qué significa "259"?** ¿Le pagas $2.590.000 al mes en total a las personas? Si es así, estás pagando **menos** que los intereses (~$2.832.000) y la diferencia se está sumando a la deuda o quedando atrasada.
- **¿Los 80M del banco son el crédito nuevo que están negociando para pagar a las personas, o es otra deuda que ya tienes con el banco?** Todo este plan asume lo primero. Si es una deuda adicional, el panorama cambia por completo.
- Tasa de interés y pago mínimo de la **tarjeta de crédito** (sale en el extracto).
- **Servicios públicos e internet**: ¿están incluidos en el arriendo?
- Gastos que no son fijos: salidas, ropa, salud, familia, suscripciones.
