# Diagnóstico financiero y plan de salida de deudas

*Actualizado: 14 de octubre de 2026. Los números salen de `python3 planificador.py`.*

## 1. Situación actual

| Concepto | Valor |
|---|---|
| Ingreso laboral mensual | **$5.900.000** |
| – llega a Bancolombia (libre uso) | $4.500.000 |
| – tarjeta bono (solo compras; retirar cuesta ~$5.000) | $1.400.000 |
| Deuda total | **$84.000.000** (14 meses de sueldo completo) |
| Intereses que se generan cada mes | **$2.832.000** |
| Intereses en un año | **$33.984.000** |

**Casi la mitad del sueldo (48 %) se va solo en intereses**, sin que la deuda baje. Si solo se pagan los intereses, en un año se pagan ~34 millones y se sigue debiendo los mismos 84.

### Deudas, de la más cara a la más barata

| Deuda | Saldo | Tasa mensual | Equivale al año (E.A.) | Interés al mes |
|---|---|---|---|---|
| Persona natural | $4.000.000 | 5,00 % | 79,6 % | $200.000 |
| Jonathan – tramo 30M | $30.000.000 | 3,50 % | 51,1 % | $1.050.000 |
| Brandon | $40.000.000 | 3,33 % | 48,2 % | $1.332.000 |
| Jonathan – tramo 10M | $10.000.000 | 2,50 % | 34,5 % | $250.000 |

Todas estas tasas son mucho más altas que las de un crédito bancario. Además, parecen estar por encima de la **tasa de usura** que publica cada mes la Superintendencia Financiera. Confírmalo con la cifra del mes. Esto no es para dejar de pagar. Es un argumento legítimo para **negociar una tasa más baja** con cada acreedor.

## 2. Estrategia principal: cambiar deuda cara por deuda barata

Esta es la jugada con más impacto. Como tienes **empleo formal**, puedes pedir:

1. **Crédito de libranza** (se descuenta por nómina). Suele ser la tasa más baja, más o menos 1,1 %–1,5 % mensual. Pregunta en Bancolombia, en el banco o cooperativa con convenio con tu empresa y en el fondo de empleados si lo hay.
2. **Crédito de libre inversión** en Bancolombia, más o menos 1,6 %–2,2 % mensual.
3. **Compra de cartera**: algunos bancos lo ofrecen para pasar deudas de otros lados a ellos.

| Opción para los 84M | Cuota mensual | Termina en | Intereses totales |
|---|---|---|---|
| Hoy (solo intereses) | $2.832.000 | **nunca** | infinito |
| Pagando 3,5M/mes a personas (avalancha) | $3.500.000 | 48 meses | ~$82,3M |
| **Libranza 1,3 % a 48 meses** | **$2.363.000** | 48 meses | **~$29,4M** |
| Libranza 1,3 % a 60 meses | $2.025.000 | 60 meses | ~$37,5M |
| Libre inversión 1,8 % a 60 meses | $2.301.000 | 60 meses | ~$54,1M |

👉 Con una libranza a 48 meses **pagas menos cada mes que hoy** ($2,36M frente a $2,83M) **y terminas de pagar en 4 años**. Te ahorras unos **$53 millones** comparado con pagarle 3,5M al mes a las personas.

Si el banco no presta los 84M completos, sirve igual pedir una parte y **reemplazar primero las deudas más caras**: los 4M al 5 %, después los 30M de Jonathan al 3,5 % y después los 40M de Brandon.

## 3. Si se sigue pagando a las personas: método avalancha

El orden de pago es:
1. **Persona natural, 4M al 5 %**
2. **Jonathan, tramo 30M al 3,5 %**
3. **Brandon, 40M al 3,33 %**
4. **Jonathan, tramo 10M al 2,5 %**

Cada mes se paga el interés de todas y **todo el dinero extra va a la primera de la lista**. Cuando esa queda saldada, su cuota pasa a la siguiente.

| Pago total a deudas al mes | Termina en | Intereses totales |
|---|---|---|
| $2.900.000 | 100 meses (8,3 años) | ~$204M |
| $3.200.000 | 61 meses | ~$111M |
| $3.500.000 | 48 meses | ~$82M |
| $4.000.000 | 36 meses | ~$59M |
| $4.500.000 | 30 meses | ~$47M |

Cada $300.000 adicionales al mes recortan años y decenas de millones en intereses.

## 4. Acciones inmediatas

- [ ] **Usar la tarjeta bono para todo el mercado y las compras del día a día.** Así los $4,5M de Bancolombia quedan libres para deudas y gastos que solo se pagan con transferencia. No retirar del bono (cobra ~$5.000).
- [ ] Ir a Bancolombia y al área de nómina o al fondo de empleados a preguntar por **libranza / compra de cartera**: monto máximo, tasa y plazo.
- [ ] Hablar con Jonathan y Brandon: proponer **bajar la tasa** (por ejemplo, al 2 %) a cambio de abonos a capital constantes. Dejar todo **por escrito** con recibos de cada pago.
- [ ] Pagar primero la deuda de **4M al 5 %**. Es la más cara y la más rápida de cerrar.
- [ ] Prima de diciembre, cesantías (si se pueden usar) o cualquier ingreso extra: **directo a la deuda más cara**.

## 5. Ideas para generar más ingresos

*Se ajustan cuando sepa tu profesión y tu tiempo libre.*
- Horas extra, bonificaciones o un ascenso en el trabajo actual.
- Freelance o asesorías en lo que ya sabes hacer.
- Vender cosas que no se usan (es dinero inmediato para la deuda del 5 %).
- Ingresos de fin de semana: domicilios, clases, servicios técnicos, etc.

## 6. Datos que faltan para cerrar el plan

- Gastos mensuales: arriendo, servicios, transporte, celular, colegio, etc. Se llenan en `datos.json`.
- ¿Hoy cuánto les pagas al mes a cada uno? ¿Solo intereses o también capital?
- ¿El sueldo de 5,9M es el bruto o ya es lo que llega en total?
- ¿Tienes ahorros, cesantías o prima?
- ¿Otras deudas (tarjetas de crédito, créditos bancarios, celular)?
