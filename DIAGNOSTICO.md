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
| Tarjeta de crédito | $4.000.000 | ~2,12 % (tope de usura) | 28,6 % | ~$85.000 | ? |
| **Banco de vivienda** | **$140.000.000** cobrados (capital 80M) | ? | | | **En mora, no se paga nada** |
| **Total** | **$228.000.000** | | | | |

- La **tasa de usura** de octubre de 2026 es **28,59 % E.A. (~2,12 % mensual)**. **Todas las deudas con personas la superan.** Estás pagando **~$1.050.000 al mes por encima del máximo legal**.
- La deuda del banco **crece cada mes** sin que se abone nada.

## 3. La conclusión honesta

Con lo que te queda ($2,3M, o $2,7M con el recorte del celular), **ningún escenario funciona sin más ingresos**. Aun si el banco reestructura, la cuota del banco más los intereses de las personas superan lo que tienes.

| Escenario | Pago mínimo mensual para no atrasarse con nadie | Con $4,7M/mes | Con $6,7M/mes |
|---|---|---|---|
| 1. Nada cambia | $2,92M (y el banco sigue creciendo) | nunca | 5,7 años |
| 2. Banco reestructura los **140M** a 15 años al 1 % | **$4,60M** | 9,7 años | 4 años |
| 3. Banco reestructura solo el **capital de 80M** a 15 años al 1 % | **$3,88M** | 5,1 años | 2,8 años |
| 4. Escenario 3 + personas al tope legal de usura | **$2,83M** | 4,2 años | 2,6 años |

*Los $4,7M y $6,7M suponen $2M o $4M de ingreso extra al mes.*

**Lo que define todo:**
1. **Que el banco cobre sobre el capital (80M) y no sobre 140M.** La diferencia es de ~$720.000 al mes en la cuota. Ver `BANCO_RENEGOCIACION.md`.
2. **Bajar lo que pagas a las personas al máximo legal.** Son ~$1,05M al mes. Ver `NEGOCIACION.md`.
3. **Subir ingresos al menos $2M al mes.** Ver `INGRESOS_EXTRA.md`.

## 4. Plan por etapas

### Etapa 0. Esta semana
- [ ] **Celular de $500.000 a ~$100.000.**
- [ ] Usar los **$400.000 que sobran del bono**.
- [ ] **No pedir más préstamos** para pagar intereses.
- [ ] Revisar en [Consulta de Procesos](https://consultaprocesos.ramajudicial.gov.co/) si hay **demanda judicial** del banco.
- [ ] Empezar a **guardar todos los comprobantes** de lo que les pagas a las personas.

### Etapa 1. Próximas 2 semanas: el banco
- [ ] Enviar el **derecho de petición** (plantilla en `BANCO_RENEGOCIACION.md`).
- [ ] Si a los 15 días hábiles no hay respuesta útil, enviar la **solicitud de conciliación al Defensor del Consumidor Financiero**.

### Etapa 2. Paralelo: asesoría legal gratuita
- [ ] Ir a un **consultorio jurídico universitario** con: los comprobantes de pago a las personas, la respuesta del banco y la lista de deudas. Hay que evaluar:
  - El reclamo por **usura** a las personas.
  - La revisión de la **liquidación del banco**.
  - Si aplica la **insolvencia de persona natural**.

### Etapa 3. Ingresos
- [ ] Ver `INGRESOS_EXTRA.md`. Meta: **+$2M al mes**.

## 5. Datos que faltan
- **¿Cuál es el banco?** Con eso busco sus canales oficiales exactos (correo de peticiones, Defensor del Consumidor Financiero).
- **¿Es un crédito hipotecario o un leasing habitacional?** ¿De qué año es el crédito?
- **¿Sobre qué inmueble es?** ¿Quién vive ahí? ¿Cuánto vale aproximadamente? (Pagas arriendo aparte.)
- ¿Cuántos meses lleva en mora? ¿Ha llegado alguna **notificación de juzgado**?
- ¿Hay **codeudores**?
- ¿Cómo estás cubriendo hoy los ~$532.000 que faltan cada mes?
- ¿La tarjeta de crédito es del mismo banco? ¿Está al día?
- ¿Desde cuándo les pagas intereses a las personas? (Sirve para calcular cuánto has pagado por encima de la usura.)
