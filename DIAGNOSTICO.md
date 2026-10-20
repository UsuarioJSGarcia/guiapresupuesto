# Diagnóstico financiero y plan de salida de deudas

*Actualizado: 20 de octubre de 2026. Los números salen de `python3 planificador.py`.*

## 1. Flujo de caja mensual

| Concepto | Bancolombia | Tarjeta bono |
|---|---|---|
| Entra (neto) | $4.500.000 | $1.400.000 |
| Arriendo | -$900.000 | |
| Servicios + internet | -$500.000 | |
| Transporte | -$300.000 | |
| Celular | -$500.000 | |
| Mercado | | -$1.000.000 |
| **Queda** | **$2.300.000** | **$400.000** |
| Intereses que pagas a las personas | **-$2.832.000** | |
| **Hueco mensual** | **-$532.000** | |

Hoy pagas a las personas más de lo que te queda en la cuenta. Ese hueco de ~$532.000 al mes se está cubriendo con algo (¿tarjeta, préstamos, atrasos?) y hace que la deuda crezca.

## 2. Deudas

| Deuda | Saldo | Tasa mensual | Equivale al año | Interés al mes | Estado |
|---|---|---|---|---|---|
| Persona natural | $4.000.000 | 5,00 % | 79,6 % | $200.000 | Al día (solo intereses) |
| Jonathan, tramo 30M | $30.000.000 | 3,50 % | 51,1 % | $1.050.000 | Al día (solo intereses) |
| Brandon | $40.000.000 | 3,33 % | 48,2 % | $1.332.000 | Al día (solo intereses) |
| Jonathan, tramo 10M | $10.000.000 | 2,50 % | 34,5 % | $250.000 | Al día (solo intereses) |
| Tarjeta de crédito | $4.000.000 | >2 % (se asume 2,3 %) | ~31 % | ~$92.000 | ? |
| **Banco** | **$140.000.000** cobrados (capital 80M) | se asume 2 % | | ~$2.800.000 | **En mora, reportado** |
| **Total** | **$228.000.000** | | | **~$5.700.000** | |

**La deuda equivale a 39 meses de sueldo completo, y los intereses que genera (~$5,7M) son casi todo tu ingreso (97 %).**

## 3. La conclusión honesta

Con las tasas y los saldos actuales, **no hay forma de pagar**, ni siquiera con $2M o $4M más de ingreso al mes. Salir requiere **las dos cosas a la vez**:

1. **Renegociar las deudas** (banco y personas), y
2. **Subir los ingresos** al menos **$1–2M al mes**.

| Escenario | Deuda | Cuota para salir en 7 años | Con $2,7M/mes | Con $4,7M/mes | Con $6,7M/mes |
|---|---|---|---|---|---|
| 1. Nada cambia | $228M | $6,6M | nunca | nunca | 5,7 años |
| 2. Banco acepta solo capital (80M) al 1,5 %; personas bajan al 2 % | $168M | $3,9M | nunca | 4,7 años | 2,8 años |
| 3. Banco 80M al 1,5 %; personas al 1 % | $168M | $3,3M | 9,5 años | **3,9 años** | **2,5 años** |

*$2,7M = lo que queda con el recorte del celular. $4,7M y $6,7M = con $2M o $4M de ingreso extra.*

## 4. Plan por etapas

### Etapa 0. Esta semana: parar el sangrado
- [ ] **Celular de $500.000 a ~$100.000**: +$400.000 al mes.
- [ ] Usar los **$400.000 que sobran en el bono** para todo lo que se pueda comprar con él.
- [ ] **No pedir prestado a nadie más** para pagar intereses. Eso es lo que hace crecer la bola.
- [ ] **Orden de prioridad de pagos**: 1) arriendo, servicios, comida y transporte, porque sin ellos pierdes el trabajo y el ingreso; 2) lo pactado con quien negocies; 3) lo demás.

### Etapa 1. Próximas 2 semanas: el banco
- [ ] **No aceptar cifras por teléfono.** Pedir por escrito el **estado de cuenta detallado**: capital, intereses corrientes, intereses de mora, honorarios de cobranza y seguros.
- [ ] Revisar que **los intereses de mora no superen la tasa de usura** (Art. 884 del Código de Comercio). Lo que se cobre por encima es reclamable.
- [ ] Preguntar si la deuda está **castigada o vendida a una casa de cobranza**. Si lo está, suelen aceptar **descuentos grandes**.
- [ ] Pedir **reestructuración**: condonar intereses de mora, saldo cercano al capital (80M), plazo largo (84–96 meses) y tasa baja. Ver `NEGOCIACION.md`.
- [ ] Preguntar si ya hay una **demanda o proceso judicial**. Si lo hay, pueden **embargar parte del sueldo** (por regla general, una quinta parte de lo que excede el salario mínimo).

### Etapa 2. Paralelo: las personas
Hoy reciben $2,83M al mes solo en intereses, a tasas que parecen estar **por encima de la usura legal**. Hay que proponerles **bajar la tasa** (a 1–2 %) y, si se puede, empezar a abonar a capital. Ver `NEGOCIACION.md`.

### Etapa 3. Si la negociación individual no funciona: insolvencia de persona natural
Existe un procedimiento legal en Colombia (**Ley 1564 de 2012, Código General del Proceso, arts. 531 y siguientes**) para personas naturales **no comerciantes**, como un empleado. Se tramita en un **centro de conciliación o notaría**. Sirve para:
- Negociar **con todos los acreedores a la vez** (banco y personas) un acuerdo de pago con plazos y tasas manejables.
- **Suspender los cobros y procesos** mientras se negocia.

Tiene requisitos: estar en **cesación de pagos**, con varias obligaciones en mora de más de 90 días. **Consultarlo con un abogado o con el consultorio jurídico gratuito de una universidad**. Es una herramienta legítima pensada justo para situaciones así.

### Etapa 4. Más ingresos (obligatorio, no opcional)
Ver `INGRESOS_EXTRA.md`. La meta es **+$2M al mes en 3–6 meses**.

## 5. Datos que faltan
- **¿Cómo estás cubriendo hoy el hueco de ~$532.000 al mes?** (tarjeta, préstamos, atrasos en algo).
- **¿Con qué banco es la deuda de 80M?** Si es **Bancolombia**, donde te llega el sueldo, hay que revisar si el contrato les permite **debitarte la cuenta**.
- ¿Cuántos meses lleva en mora? ¿Te ha llegado alguna **demanda o notificación de juzgado**?
- ¿La tarjeta de crédito está al día o en mora? ¿Cuál es el **pago mínimo**?
- ¿Con las personas firmaste **pagarés o letras**?
- ¿Tu sueldo bruto (antes de descuentos) cuánto es? Sirve para saber cuánto podrían embargar.
