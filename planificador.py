"""Diagnóstico financiero y plan de pago de deudas.

Uso:
    python3 planificador.py             # diagnóstico + escenarios
    python3 planificador.py 3500000     # simula destinar 3,5M/mes a deudas

Edita datos.json con tus números reales y vuelve a correrlo.
"""
import json
import sys
from pathlib import Path

DATOS = json.loads((Path(__file__).parent / "datos.json").read_text(encoding="utf-8"))


def cop(x):
    return ("-" if x < 0 else "") + "$" + f"{abs(x):,.0f}".replace(",", ".")


def tasa_ea(mensual):
    return (1 + mensual) ** 12 - 1


def cuota_credito(monto, tasa_mensual, meses):
    return monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -meses)


def simular(deudas, pago_mensual, orden="avalancha", max_meses=600):
    """Mes a mes: se causan intereses; cada deuda recibe su mínimo (la cuota
    fija si es un crédito, o el interés si es préstamo de persona); lo que sobra
    va completo a la deuda objetivo (avalancha = mayor tasa, bola = menor saldo).
    Devuelve (meses_hasta_cero o None, interes_total, {deuda: mes_pagada})."""
    saldo = {d["nombre"]: float(d["saldo"]) for d in deudas}
    tasa = {d["nombre"]: d["tasa_mensual"] for d in deudas}
    cuota = {d["nombre"]: d.get("cuota_fija") for d in deudas}
    interes_total = 0.0
    salida = {}
    for mes in range(1, max_meses + 1):
        disponible = pago_mensual
        intereses_mes = {}
        for n in saldo:
            i = saldo[n] * tasa[n] if saldo[n] > 0 else 0.0
            intereses_mes[n] = i
            saldo[n] += i
            interes_total += i
        vivas = [n for n in saldo if saldo[n] > 0.5]
        vivas.sort(key=(lambda n: -tasa[n]) if orden == "avalancha" else (lambda n: saldo[n]))
        for n in vivas:
            minimo = cuota[n] if cuota[n] else intereses_mes[n]
            pago = min(minimo, saldo[n], disponible)
            saldo[n] -= pago
            disponible -= pago
        for n in vivas:
            pago = min(saldo[n], disponible)
            saldo[n] -= pago
            disponible -= pago
        for n in vivas:
            if saldo[n] <= 0.5 and n not in salida:
                salida[n] = mes
        if all(s <= 0.5 for s in saldo.values()):
            return mes, interes_total, salida
    return None, interes_total, salida


def flujo_caja(recortes=False):
    libre = sum(i["monto"] for i in DATOS["ingresos"] if i["libre_uso"])
    bono = sum(i["monto"] for i in DATOS["ingresos"] if not i["libre_uso"])
    g_efectivo = sum(g["monto"] for g in DATOS["gastos_fijos"] if g["medio"] == "efectivo")
    g_bono = sum(g["monto"] for g in DATOS["gastos_fijos"] if g["medio"] == "bono")
    ahorro = sum(r["ahorro"] for r in DATOS.get("recortes_posibles", [])) if recortes else 0
    return libre, bono, g_efectivo - ahorro, g_bono


def deudas_con_banco(monto, tasa, plazo):
    """Usa el crédito para pagar primero las deudas con personas más caras.
    La tarjeta no se recoge (se paga aparte con el flujo libre)."""
    personas = sorted([d for d in DATOS["deudas"] if "Tarjeta" not in d["nombre"]],
                      key=lambda d: -d["tasa_mensual"])
    resto = monto
    nuevas = []
    for d in personas:
        usado = min(resto, d["saldo"])
        resto -= usado
        if d["saldo"] - usado > 0:
            nuevas.append({**d, "saldo": d["saldo"] - usado})
    nuevas += [d for d in DATOS["deudas"] if "Tarjeta" in d["nombre"]]
    c = cuota_credito(monto, tasa, plazo)
    nuevas.append({"nombre": f"Banco {monto / 1e6:.0f}M", "saldo": monto,
                   "tasa_mensual": tasa, "cuota_fija": c})
    return nuevas, c


def diagnostico():
    deudas = DATOS["deudas"]
    libre, bono, g_ef, g_bono = flujo_caja()
    total_deuda = sum(d["saldo"] for d in deudas)
    interes_mes = sum(d["saldo"] * d["tasa_mensual"] for d in deudas)
    disponible = libre - g_ef

    print("=" * 72)
    print("DIAGNÓSTICO FINANCIERO")
    print("=" * 72)
    print(f"Ingreso neto mensual:          {cop(libre + bono)}")
    print(f"  Bancolombia (libre uso):     {cop(libre)}")
    print(f"  Tarjeta bono:                {cop(bono)}")
    print(f"Gastos que salen de Bancolombia: {cop(g_ef)}")
    print(f"Gastos pagados con bono:       {cop(g_bono)}  (sobra en bono: {cop(bono - g_bono)})")
    print(f"Queda en Bancolombia para deudas: {cop(disponible)}")
    print()
    print(f"Deuda total:                   {cop(total_deuda)}")
    print(f"Intereses que genera al mes:   {cop(interes_mes)}  "
          f"({interes_mes / (libre + bono):.0%} del ingreso)")
    print(f"Balance mensual (si solo pagas intereses): {cop(disponible - interes_mes)}")
    print()
    print(f"{'Deuda':40} {'Saldo':>13} {'Tasa mes':>9} {'E.A.':>7} {'Interés/mes':>12}")
    for d in sorted(deudas, key=lambda d: -d["tasa_mensual"]):
        print(f"{d['nombre']:40} {cop(d['saldo']):>13} {d['tasa_mensual']:>9.2%} "
              f"{tasa_ea(d['tasa_mensual']):>7.1%} {cop(d['saldo'] * d['tasa_mensual']):>12}")
    return disponible


def escenarios_sin_banco(pagos):
    print()
    print("=" * 72)
    print("A) SIN CRÉDITO BANCARIO: avalancha con las deudas actuales")
    print("=" * 72)
    for p in pagos:
        meses, interes, _ = simular(DATOS["deudas"], p)
        txt = "NUNCA se paga (la deuda crece o no baja)" if meses is None \
            else f"{meses} meses ({meses / 12:.1f} años), intereses {cop(interes)}"
        print(f"  {cop(p):>12}/mes -> {txt}")


def escenarios_con_banco(pagos):
    cb = DATOS["credito_banco"]
    print()
    print("=" * 72)
    print(f"B) CON CRÉDITO BANCARIO DE {cop(cb['monto'])} a {cb['plazo_meses']} meses")
    print("   (recoge las deudas con personas más caras; lo demás se paga en avalancha")
    print("    y cuando todo lo demás se acaba, el sobrante se abona al banco)")
    print("=" * 72)
    for tasa in cb["tasas_a_evaluar"]:
        deudas, c = deudas_con_banco(cb["monto"], tasa, cb["plazo_meses"])
        print(f"  Tasa {tasa:.2%} m.v. ({tasa_ea(tasa):.1%} E.A.): cuota banco {cop(c)}")
        for p in pagos:
            meses, interes, salida = simular(deudas, p)
            if meses is None:
                print(f"     {cop(p):>12}/mes -> no alcanza")
                continue
            libres = [f"{n} mes {m}" for n, m in sorted(salida.items(), key=lambda x: x[1])
                      if not n.startswith("Banco")]
            print(f"     {cop(p):>12}/mes -> libre en {meses} meses ({meses / 12:.1f} años), "
                  f"intereses {cop(interes)}")
            print(f"{'':22}orden: " + "; ".join(libres))


if __name__ == "__main__":
    disponible = diagnostico()
    _, _, g_ef_rec, _ = flujo_caja(recortes=True)
    libre = flujo_caja()[0]
    disponible_rec = libre - g_ef_rec
    if len(sys.argv) > 1:
        pagos = [float(a) for a in sys.argv[1:]]
    else:
        pagos = sorted({round(disponible), round(disponible_rec)})
        print(f"\nCon recortes ({', '.join(r['nombre'] for r in DATOS['recortes_posibles'])}): "
              f"quedan {cop(disponible_rec)} para deudas.")
    escenarios_sin_banco(pagos)
    escenarios_con_banco(pagos)
