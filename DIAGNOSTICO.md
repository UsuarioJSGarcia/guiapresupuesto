# Diagnóstico financiero y plan de salida de deudas

*Actualizado: 22 de octubre de 2026. Los números salen de `python3 planificador.py`.*

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
| Jensi | $11.000.000 | **pendiente** | | **pendiente** | ? |
| Tarjeta Nubank | $4.000.000 | ~2,12 % (supuesto) | 28,6 % | ~$85.000 | ? |
| **Davivienda (crédito de consumo)** | **$140.000.000** cobrados (capital 80M) | ? | | | **En mora, no se paga nada** |
| **Total** | **$239.000.000** | | | **~$5,7M + Jensi** | |

**Resumen por tipo:**

| Tipo | Deuda |
|---|---|
| Personas (Jonathan 40M, Brandon 40M, persona 4M, Jensi 11M) | **$95.000.000** |
| Tarjeta Nubank | $4.000.000 |
| Davivienda (lo que cobran) | $140.000.000 *(capital: 80M)* |
| **Total** | **$239.000.000**, unos 41 meses de sueldo completo |
| Total si Davivienda se deja en el capital | $179.000.000 |

- Con las personas, la única forma de pagar menos interés es **abonar a capital**. Cada $1.000.000 abonado a la deuda del 5 % ahorra $50.000 al mes.
- La deuda del banco **crece cada mes** sin que se abone nada.

## 3. La conclusión honesta

Con lo que te queda ($2,3M, o $2,7M con el recorte del celular), **ningún escenario funciona sin más ingresos**.

| Escenario | Pago mínimo mensual para no atrasarse con nadie | Con $4,7M/mes | Con $6,7M/mes |
|---|---|---|---|
| 1. Nada cambia | $2,92M (y Davivienda sigue creciendo) | nunca | 5,7 años |
| 2. Davivienda reestructura los **140M** a 84 meses al 1,8 % | **$6,16M** | nunca | 5,6 años |
| 3. Davivienda reestructura solo el **capital de 80M** a 84 meses al 1,8 % | **$4,77M** | 10,2 años | 3,2 años |
| 4. Escenario 3 + ya pagada la deuda de 4M al 5 % | **$4,57M** | 7,5 años | 3,1 años |

*Los $4,7M y $6,7M suponen $2M o $4M de ingreso extra al mes. El 1,8 % y los 84 meses de Davivienda son supuestos.*

**Lo que define todo:**
1. **Que Davivienda vuelva la deuda al capital (80M)**: la cuota baja de $3,2M a $1,85M. Ver `BANCO_RENEGOCIACION.md`.
2. **Abonar a capital a las personas**, empezando por la deuda de 4M al 5 %. Ver `NEGOCIACION.md`.
3. **Subir ingresos al menos $2M al mes.** Ver `INGRESOS_EXTRA.md`.

## 4. Plan por etapas

### Etapa 0. Esta semana
- [ ] **Celular de $500.000 a ~$100.000.**
- [ ] Usar los **$400.000 que sobran del bono**.
- [ ] **No pedir más préstamos** para pagar intereses.
- [ ] Revisar en [Consulta de Procesos](https://consultaprocesos.ramajudicial.gov.co/) si hay **demanda judicial** de Davivienda.
- [ ] Consultar gratis **DataCrédito y TransUnion**: fecha de inicio de la mora y quién figura como acreedor.

### Etapa 1. Próximas 2 semanas: Davivienda
- [ ] Enviar el **derecho de petición** (plantilla en `BANCO_RENEGOCIACION.md`).
- [ ] Si a los 15 días hábiles no hay respuesta útil, enviar la **solicitud de conciliación al Defensor del Consumidor Financiero**.

### Etapa 2. Paralelo: asesoría para Davivienda
- [ ] Ir a un **consultorio jurídico universitario (gratis)** con la respuesta de Davivienda y el reporte de las centrales. Allí revisan:
  - La **liquidación de Davivienda** y una posible **prescripción**, si lleva más de 3 años sin demanda.
  - Si aplica la **insolvencia de persona natural**.

### Etapa 3. Ingresos
- [ ] Ver `INGRESOS_EXTRA.md`. Meta: **+$2M al mes**.

## 5. Datos que faltan
- **¿Desde qué fecha está en mora con Davivienda?** ¿Ha llegado alguna **notificación de juzgado**?
- **¿Qué tipo de crédito es?** ¿Libre inversión, rotativo, libranza? ¿Hay **codeudor**?
- **Jensi (11M):** ¿qué tasa mensual te cobra y cuánto le pagas al mes?
- **Tarjeta Nubank:** ¿está al día? ¿Cuál es el pago mínimo?
- ¿Cómo estás cubriendo hoy los ~$532.000 que faltan cada mes?
- Los documentos útiles están en `DOCUMENTOS.md`.
