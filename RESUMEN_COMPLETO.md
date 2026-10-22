# Guía de presupuesto: resumen completo del proyecto

*Actualizado: 22 de octubre de 2026*
*Repositorio: `UsuarioJSGarcia/guiapresupuesto`, rama `claude/ingresos-deudas-financiero-cw282o`*

Este documento reúne **todo lo conversado y todo lo construido**: la situación financiera, las deudas, el plan con Davivienda, el plan con las personas, el plan de ingresos y lo que falta por hacer.

---

## 1. Objetivo del proyecto

1. Organizar los ingresos y los gastos mensuales.
2. Salir de las deudas lo más rápido posible (lo principal).
3. Generar más ingresos.
4. Tener un diagnóstico claro de la situación financiera actual.

---

## 2. Cómo avanzó la conversación

| Fecha | Qué se habló | Qué se hizo |
|---|---|---|
| 8-oct | Arranque del proyecto. El repositorio estaba vacío. | Se pidieron los datos: ingresos, gastos, deudas, ahorros y habilidades. |
| 14-oct | Ingresos: $5,9M ($4,5M en Bancolombia + $1,4M en tarjeta bono). Deudas con personas: 4M al 5 %, Jonathan 40M (10M al 2,5 % + 30M al 3,5 %), Brandon 40M al 3,33 %. | Primer diagnóstico y calculadora (`planificador.py`). La subida a GitHub falló por permisos; se resolvió cuando se dio acceso a la app de Claude. |
| 20-oct | Gastos: arriendo 900k, transporte 300k, celular 500k, mercado 1M. Solo se pagan intereses. Sueldo neto. Tarjeta de 4M. Profesión: ingeniero de software con poco tiempo libre. | Flujo de caja (bono vs. Bancolombia), primeras ideas de ingreso, guía de negociación. |
| 20-oct | Los 80M del banco **no son un crédito nuevo**: es una deuda **en mora** y el banco cobra **140M**. Servicios + internet: 500k. Ideas: bot de trading y videos. | Diagnóstico rehecho (sin crédito de consolidación). Evaluación de las ideas de ingreso: el trading se descarta por ahora. |
| 20-oct | Davivienda no paga nada y crece la mora. Los analistas cierran la puerta por teléfono. Las personas **no aceptan bajar tasas**. | Investigación legal y plan para renegociar por escrito. |
| 20-oct | **No es un crédito de vivienda**: es de **consumo con Davivienda**. Con las personas **no hay temas legales: se paga y ya**. Abonar a capital baja el interés. | Guía rehecha para consumo con Davivienda. Plan con las personas: solo abonos a capital. Lista de documentos útiles. |
| 22-oct | Tarjeta: **Nubank, 4M**. Nueva deuda: **Jensi, 11M**, a quien se le pagan 400k al mes. **Joan (4M al 5 %) se paga completa.** | Totales actualizados: **$235M**. |
| 22-oct | Hoy se pide prestado para cubrir los gastos. Se necesita llegar al equilibrio, ojalá con +50 % o +100 % de ingresos. | Plan de ingresos con metas, rutas y un plan de 90 días. |
| 22-oct | Mejorar el LinkedIn y la hoja de vida. | No es posible entrar a LinkedIn desde el servidor. **Pendiente: subir el PDF del perfil y la hoja de vida.** |

---

## 3. Situación actual

### Flujo de caja mensual

| Concepto | Bancolombia | Tarjeta bono |
|---|---|---|
| Entra (neto) | $4.500.000 | $1.400.000 |
| Arriendo | -$900.000 | |
| Servicios + internet | -$500.000 | |
| Transporte | -$300.000 | |
| Celular | -$500.000 | |
| Mercado | | -$1.000.000 |
| **Queda** | **$2.300.000** | **$400.000** |
| Intereses a Jensi, Jonathan y Brandon | **-$3.032.000** | |
| **Hueco mensual** | **-$732.000** | |

Hoy ese hueco se cubre **pidiendo prestado otra vez**. Por eso las deudas no bajan.

### Deudas (22-oct-2026)

| Deuda | Saldo | Tasa mensual | Equivale al año | Interés al mes | Estado |
|---|---|---|---|---|---|
| Jensi | $11.000.000 | 3,64 % | 53,5 % | $400.000 | Al día (solo intereses) |
| Jonathan, tramo 30M | $30.000.000 | 3,50 % | 51,1 % | $1.050.000 | Al día (solo intereses) |
| Brandon | $40.000.000 | 3,33 % | 48,2 % | $1.332.000 | Al día (solo intereses) |
| Jonathan, tramo 10M | $10.000.000 | 2,50 % | 34,5 % | $250.000 | Al día (solo intereses) |
| Tarjeta Nubank | $4.000.000 | ~2,12 % (supuesto) | 28,6 % | ~$85.000 | ? |
| **Davivienda (consumo)** | **$140.000.000** cobrados (capital 80M) | ? | | | **En mora, no se paga nada** |
| **Total** | **$235.000.000** | | | **~$5,9M** | |

✅ **Joan (4M al 5 %): pagada en su totalidad el 22-oct-2026.**

| Tipo | Deuda |
|---|---|
| Personas (Jonathan 40M, Brandon 40M, Jensi 11M) | $91.000.000 |
| Tarjeta Nubank | $4.000.000 |
| Davivienda (lo que cobran) | $140.000.000 (capital: 80M) |
| **Total** | **$235.000.000**, unos 40 meses de sueldo completo |
| Total si Davivienda se deja en el capital | $175.000.000 |

### Escenarios (calculados con `planificador.py`)

| Escenario | Pago mínimo mensual para no atrasarse con nadie | Con $4,7M/mes | Con $6,7M/mes |
|---|---|---|---|
| 1. Nada cambia | $3,12M (y Davivienda sigue creciendo) | nunca | 6,3 años |
| 2. Davivienda reestructura los 140M a 84 meses al 1,8 % | $6,36M | nunca | 6,3 años |
| 3. Davivienda reestructura solo el capital de 80M a 84 meses al 1,8 % | $4,97M | 14 años | 3,5 años |
| 4. Escenario 3 + ya pagada Jensi | $4,57M | 7,5 años | 3,1 años |

*El 1,8 % y los 84 meses de Davivienda son supuestos. Los $4,7M y $6,7M suponen $2M o $4M de ingreso extra.*

### Conclusión
**Ningún escenario funciona sin más ingresos.** Lo que define todo:
1. Que **Davivienda vuelva la deuda al capital (80M)**: la cuota baja de ~$3,2M a ~$1,85M.
2. **Abonar a capital** a las personas, empezando por Jensi.
3. **Subir ingresos al menos $2,3M al mes.**

---

## 4. Acciones inmediatas

- [ ] **Bajar el plan de celular** de $500.000 a ~$100.000: +$400.000 al mes.
- [ ] Usar los **$400.000 que sobran del bono** para todo lo que se pueda comprar con él. No retirar del bono (cobra ~$5.000).
- [ ] **Nubank:** no pagar los 4M de golpe con el sueldo, porque obligaría a pedir prestado otra vez. Es mejor diferirlos a cuotas.
- [ ] Revisar en [Consulta de Procesos](https://consultaprocesos.ramajudicial.gov.co/) si hay **demanda** de Davivienda.
- [ ] Consultar gratis **DataCrédito y TransUnion**: desde cuándo está en mora y quién tiene hoy la deuda.

---

## 5. Davivienda: plan de renegociación (crédito de consumo en mora)

### Por qué por teléfono no funciona
Los analistas solo ofrecen lo que el sistema les muestra. **Se negocia por escrito.** Por teléfono, solo decir:
> "No voy a negociar por teléfono. Envíeme por escrito el estado de cuenta y las propuestas. Voy a radicar una solicitud formal."

**Ley 2300 de 2023 ("Dejen de fregar"):** solo pueden llamar de lunes a viernes de 7 a. m. a 7 p. m. y los sábados de 8 a. m. a 3 p. m. Nunca domingos ni festivos, y no pueden contactar a las referencias personales. Las quejas van a la SIC.

### Lo que dice la ley
| Regla | Qué significa |
|---|---|
| Tasa de usura (Art. 884 C. Co.) | Ningún interés, tampoco el de mora, puede superar la usura de cada mes (oct-2026: **28,59 % E.A.**). |
| Sanción (Art. 72 Ley 45 de 1990) | Si cobran por encima de la usura, pierden los intereses cobrados en exceso, más una suma igual. |
| Intereses sobre intereses (Art. 886 C. Co.) | Solo desde una demanda o un acuerdo posterior, y si los intereses llevan al menos un año de vencidos. |
| Gastos de cobranza | Solo por gestión efectiva y según las tarifas que el banco publica. Hay que pedir el soporte. |
| Reestructuración | En consumo **no es obligatoria**: el banco la estudia según la capacidad de pago. |
| Reporte negativo (Ley 2157 de 2021) | Dura el doble del tiempo en mora, con un máximo de 4 años después de pagar. |

**¿Es correcto que 80M se hayan vuelto 140M?** En consumo, el banco puede declarar vencido todo el crédito. A tasas cercanas a la usura, puede llegar ahí en unos 2,5 años de mora. **Solo se sabe con la liquidación detallada.** Si lleva **más de 3 años en mora sin demanda**, hay que consultar con un abogado una posible **prescripción** (Art. 789 C. Co.; confirmar con el abogado).

### Canales de Davivienda
| Canal | Dato |
|---|---|
| Línea, opción clientes en mora | 601 338 3838 (Bogotá) · 01 8000 12 3838 (nacional). Solo para pedir todo por escrito. |
| Defensor del Consumidor Financiero (quejas) | **defensordelcliente@davivienda.com** · 601 213 1370 / 601 213 1322 · Av. 19 No. 114-09, Of. 502, Bogotá |
| Defensor: solicitud de conciliación | **defensordavivienda@pgabogados.com** |
| Notificaciones judiciales (como copia) | notificacionesjudiciales@davivienda.com |
| Derecho de petición | Formulario de quejas y reclamos en davivienda.com, o radicado en oficina con sello y número |

### Pasos
1. **Saber qué hay:** buscar demandas, consultar las centrales de riesgo y reunir los papeles.
2. **Derecho de petición** (Anexo A): lo firma el titular. Davivienda tiene **15 días hábiles** para responder.
3. **Defensor del Consumidor Financiero** (Anexo B): es gratis, es independiente y **puede actuar como conciliador**. Lo que se acuerde ahí obliga al banco.
4. **Superintendencia Financiera**, si nada funciona.

### Qué es realista pedir
1. La liquidación detallada y la corrección de cualquier cobro indebido.
2. La condonación de los intereses de mora y los honorarios, para volver al **capital de 80M**.
3. Una reestructuración a **72–84 meses** con una cuota **que sí se pueda pagar**.
4. El **valor de pago total con descuento**, para cuando haya una suma disponible.

### Insolvencia de persona natural
- **Requisito (Ley 2445 de 2025):** dos o más obligaciones con **dos o más acreedores** en mora de más de 90 días, o dos o más procesos de cobro.
- **Hoy:** solo Davivienda está en mora, así que **no se cumpliría**. Nubank es otro acreedor; lo revisa un abogado.
- Incluiría también las deudas con las personas.

---

## 6. Las personas: Jonathan, Brandon y Jensi

**Son acuerdos personales: se cumplen pagando.** Las tasas no se negocian. La forma de pagar menos interés es **abonar a capital**: el interés se calcula sobre lo que quede debiendo (si de 80 pasas a 70, pagas interés sobre 70).

| Orden | Deuda | Tasa | Ahorro mensual por cada $1M abonado |
|---|---|---|---|
| ✅ | Joan 4M | 5 % | **Pagada (22-oct-2026)** |
| 1 | **Jensi 11M** | 3,64 % | $36.400 |
| 2 | Jonathan 30M | 3,5 % | $35.000 |
| 3 | Brandon 40M | 3,33 % | $33.300 |
| 4 | Jonathan 10M | 2,5 % | $25.000 |

- Al terminar de pagar a Jensi se liberan **$400.000 al mes**, que pasan como abono a Jonathan (30M). El efecto bola de nieve sigue así con cada deuda.
- Pagar siempre a tiempo, avisar cada abono por escrito ("te abono $X; quedo debiendo $Y") y guardar el comprobante.

---

## 7. Plan de ingresos

### Metas
| Nivel | Qué logra | Ingreso extra al mes |
|---|---|---|
| 1. Dejar de pedir prestado | Cubrir gastos e intereses (Davivienda sigue sin pagarse) | +$820.000 (+$420.000 si bajas el celular) |
| 2. **Equilibrio real** | Lo anterior + una cuota de Davivienda (~$1,85M) | **+$2.300.000** (+39 %) |
| 3. +50 % | Empezar a bajar deudas: sin deudas en ~5 años | +$2.950.000 |
| 4. **+100 %** | **Tranquilidad: sin deudas en ~2,3 años** | +$5.900.000 |

### Rutas (TRM de referencia ~$3.175; USD 1.000 ≈ $3,2M)
| Ruta | Ingreso extra típico | Tiempo hasta cobrar | Horas extra |
|---|---|---|---|
| **A. Trabajo remoto pagado en dólares** (prioridad) | Un sueldo de USD 3.500–5.000 = $11–16M | 1–3 meses | ~5 h/semana de búsqueda |
| B. Freelance por horas en dólares | $3–7M | 1–2 meses | 10–15 h/semana |
| **C. Automatizaciones con IA para negocios** (en paralelo) | $1–3M | 1–2 meses | 5–8 h/semana |
| D. Bot de trading / videos | Incierto | 6–12 meses o más | Muchas. **No por ahora.** |

**Sobre el bot de trading:** necesita capital, que hoy no hay, y la mayoría de esos bots pierden. Con deudas al 3–3,6 % mensual, cada peso libre rinde más abonando a capital.

### Plan de 90 días (~8–10 h/semana)
- **Semanas 1–2:** CV en inglés y en español, LinkedIn, perfiles en Upwork, Turing, Arc.dev, Torre.ai, Revelo y BairesDev, plantilla del chatbot de WhatsApp y página de servicios.
- **Semanas 3–8:** 5–10 aplicaciones por semana. Ofrecer el chatbot a 3–5 negocios por semana (meta: 2 clientes). Practicar entrevistas.
- **Semanas 9–12:** negociar la oferta remota. Tener 3–5 clientes con mensualidad.
- **Todo el ingreso extra va a las deudas, en este orden: Jensi → Jonathan 30M → Brandon → Jonathan 10M.**

### Siguiente paso: hoja de vida y LinkedIn
Claude no puede entrar a LinkedIn. Para hacer las mejoras hace falta subir a la sesión:
1. **El PDF del perfil de LinkedIn.** En el perfil: "Más" → "Guardar en PDF".
2. **La hoja de vida actual** (PDF o Word).
3. **El enlace del perfil** (`linkedin.com/in/...`).

Con eso se entrega: diagnóstico del perfil, textos de LinkedIn en inglés y en español, hoja de vida en ambos idiomas y palabras clave para buscar vacantes remotas.

---

## 8. Datos y documentos pendientes

**Davivienda**
- ¿Desde qué fecha está en mora? ¿Ha llegado alguna notificación de juzgado?
- ¿Qué tipo de crédito es (libre inversión, rotativo, libranza)? ¿Hay codeudor?
- Reporte de DataCrédito o TransUnion, cartas o mensajes donde aparezcan los 140M, y el pagaré o contrato.

**Nubank**
- ¿Está al día? ¿Cuál es el pago mínimo? Último extracto.

**Ingresos**
- Desprendible de nómina y certificado laboral (se anexan al derecho de petición).
- PDF de LinkedIn y hoja de vida.

*Al compartir documentos, tapa la cédula completa, los números de cuenta y las firmas. Los documentos personales no se suben a GitHub.*

---

## 9. Archivos del repositorio

| Archivo | Contenido |
|---|---|
| `RESUMEN_COMPLETO.md` | Este documento |
| `DIAGNOSTICO.md` | Situación actual y plan por etapas |
| `BANCO_RENEGOCIACION.md` | Guía de Davivienda con plantillas y fuentes |
| `NEGOCIACION.md` | Plan de abonos a las personas |
| `INGRESOS_EXTRA.md` | Metas y plan de ingresos |
| `DOCUMENTOS.md` | Documentos útiles y cómo compartirlos |
| `datos.json` | Ingresos, gastos, deudas y escenarios (para editar) |
| `planificador.py` | Calculadora: `python3 planificador.py` o `python3 planificador.py 5000000` |

---

## 10. Plantillas para Davivienda

### Anexo A. Derecho de petición a Davivienda

> [Ciudad], [fecha]
>
> Señores
> **BANCO DAVIVIENDA S.A.**
> Área de Servicio al Cliente / Cartera
> Copia: notificacionesjudiciales@davivienda.com
>
> **Referencia:** Derecho de petición (Art. 23 de la Constitución Política y Ley 1755 de 2015). Obligación No. [número].
>
> Yo, [nombre completo], identificado con C.C. No. [número], titular de la obligación de la referencia, respetuosamente solicito:
>
> 1. **Estado de cuenta y liquidación detallada** de la obligación desde la fecha de la primera cuota incumplida hasta hoy. Debe discriminar el capital, los intereses corrientes, los intereses de mora, los seguros, los honorarios y gastos de cobranza, y otros cargos, indicando para **cada mes la tasa aplicada y la base sobre la que se calculó**.
> 2. Certificar que **ninguna tasa aplicada superó la tasa de usura vigente en cada periodo** (Art. 884 del Código de Comercio) y que **no se han capitalizado intereses** en contravención del Art. 886 del Código de Comercio.
> 3. Soporte de los **honorarios y gastos de cobranza** cobrados: la tarifa aplicada, la gestión que los causó y quién la realizó.
> 4. Informar si existe **proceso judicial** sobre esta obligación y si ha sido **vendida o cedida** a un tercero, indicando a quién.
> 5. Copia del **pagaré**, de la **carta de instrucciones** y de la **tabla de amortización** original.
> 6. Solicito formalmente un **acuerdo de normalización / reestructuración** en los siguientes términos:
>    - Condonación de los intereses de mora y de los honorarios de cobranza.
>    - Saldo a refinanciar: el **capital adeudado**.
>    - Plazo de **84 meses**.
>    - Cuota mensual de máximo **$[valor que sí puedas pagar]**, acorde con mi capacidad de pago, que soporto con mis certificados de ingresos.
>    - Igualmente, solicito informar el **valor de pago total con descuento** que la entidad aceptaría para cancelar la obligación.
>
> Es mi voluntad pagar y normalizar esta obligación. Solicito que toda propuesta me sea enviada **por escrito**.
>
> Recibo respuesta en: [correo] · [dirección] · [teléfono].
>
> Atentamente,
> [Firma]
> [Nombre] – C.C. [número]
>
> Anexos: copia de la cédula; certificado laboral y de ingresos; últimos desprendibles de nómina.

### Anexo B. Queja y solicitud de conciliación ante el Defensor

> [Ciudad], [fecha]
>
> Doctor(a)
> **Defensor(a) del Consumidor Financiero – Banco Davivienda S.A.**
> defensordavivienda@pgabogados.com · copia: defensordelcliente@davivienda.com
>
> **Referencia:** Queja y solicitud de conciliación. Obligación No. [número].
>
> Yo, [nombre], C.C. [número], presento queja contra Banco Davivienda S.A. y **solicito que usted actúe como conciliador** (Art. 13 de la Ley 1328 de 2009) para lograr un acuerdo de pago sobre mi obligación.
>
> **Hechos:**
> 1. Tengo con la entidad la obligación No. [número], de consumo, por un capital aproximado de $80.000.000, en mora desde [fecha].
> 2. Por vía telefónica me informan un saldo de aproximadamente $140.000.000, sin soporte escrito del cálculo.
> 3. El [fecha] radiqué un derecho de petición (radicado No. [número]) solicitando la liquidación detallada y una propuesta de normalización. [No obtuve respuesta / La respuesta fue: ...].
> 4. Los asesores de cobranza no ofrecen alternativas ajustadas a mi capacidad real de pago.
>
> **Solicito:**
> 1. Verificar que la liquidación no supere la tasa de usura de cada periodo (Art. 884 C. Co.), que no capitalice intereses (Art. 886 C. Co.) y que los gastos de cobranza estén soportados.
> 2. Citar a audiencia de conciliación para acordar la condonación de intereses de mora y honorarios y la reestructuración del capital a 84 meses, con una cuota de hasta $[valor] mensuales.
>
> Anexos: derecho de petición radicado, respuesta (si existe), cédula, certificado de ingresos.
>
> Atentamente,
> [Firma, nombre, C.C., teléfono, correo]

---

## 11. Fuentes consultadas
- Defensor del Consumidor Financiero de Davivienda: [davivienda.com/defensor-del-consumidor](https://www.davivienda.com/defensor-del-consumidor), [información al consumidor](https://www.davivienda.com/wps/portal/personas/nuevo/personas/Informacionalconsumidor).
- Línea de clientes en mora de Davivienda: [Davivienda, modificación de condiciones](https://www.davivienda.com/personas/credito-de-vivienda-inmuebles/reestructuracion-creditos-de-vivienda) (es la página de vivienda, pero publica la misma línea).
- Tarifas y gastos de cobranza: [Tarifas Davivienda](https://www.davivienda.com/documents/d/guest/tasas-tarifas-davivienda).
- Correo de notificaciones judiciales (mencionado en procesos): [Rama Judicial](https://portalhistorico.ramajudicial.gov.co/documents/10240/35932660/005.+Sentencia202100557.pdf/1852769d-7560-4138-8e6b-b2b119035c4c).
- Defensor como conciliador: [Decreto 2281 de 2010](https://normativa.colpensiones.gov.co/colpensiones/docs/decreto_2281_2010.htm), [funciones (Porvenir)](https://www.porvenir.com.co/documents/64080/0/Funciones_Defensor_Consumidor_Financiero.pdf/cc2351ee-294c-9b9f-17b6-8b01c5a975f1).
- Modificación y reestructuración de créditos (Circular Externa 026 de 2017): [Superfinanciera, ABC](https://www.superfinanciera.gov.co/publicaciones/10090487/abc-modificacion-en-las-condiciones-del-credito-segun-capacidad-de-pago-del-deudor-10090487/).
- Intereses sobre intereses (Art. 886 C. Co.): [Tribunal de Medellín](https://tribunalmedellin.com/images/decisiones/civil/2023/05001310301820200014901.pdf), [Ámbito Jurídico](https://ambitojuridico.com/sites/default/files/BancoMedios/Archivos/cpto-65387-11.doc).
- Sanción por usura (Art. 72 Ley 45 de 1990): [Tribunal de Medellín](https://tribunalmedellin.com/images/decisiones/civil/2023/05001310301720220013001.pdf).
- Ley 2300 de 2023: [CRC](https://www.crcom.gov.co/sites/default/files/normatividad/2024537299.pdf), [Vanguardia](https://www.vanguardia.com/colombia/asi-funciona-la-ley-dejen-de-fregar-para-que-los-bancos-no-llamen-los-domingos-aprenda-a-hacerla-cumplir-EA7741125).
- Insolvencia, Ley 2445 de 2025: [texto (portaldms)](https://portaldms.com/3/files/LEY_2445.pdf), [Bogotá Jurídica](https://www.alcaldiabogota.gov.co/sisjur/normas/Norma1.jsp?i=173897).
- Usura octubre 2026 (28,59 % E.A.): [Portafolio](https://www.portafolio.co/economia/finanzas/tasa-de-usura-baja-en-octubre-y-establece-nuevo-limite-para-el-cobro-de-intereses-a-los-bancos-503770), [La República](https://www.larepublica.co/finanzas/las-compras-con-tarjeta-saldran-mas-baratas-en-octubre-con-la-tasa-de-usura-en-28-59-4493376).
- Dólar (TRM ~$3.175, 19-oct-2026): [Portafolio](https://www.portafolio.co/economia/finanzas/precio-del-dolar-hoy-en-colombia-asi-cotiza-la-divisa-este-lunes-19-de-octubre-504692).

### Lo que no se pudo verificar
- El formulario exacto de PQR de Davivienda en la web o la app (no apareció en la búsqueda). Se puede radicar en cualquier oficina.
- El porcentaje exacto de gastos de cobranza de consumo vigente en 2026 y sobre qué base se calcula.
- Los plazos y tasas que Davivienda ofrece hoy en reestructuraciones de consumo. **El 1,8 % y los 84 meses son supuestos para la simulación.**
- El plazo de prescripción (Art. 789 C. Co.) y la prescripción de la cuota se citan de conocimiento general, no de la búsqueda: **confírmalo con un abogado**.
