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
    """Mes a mes: se causan intereses; cada deuda recibe su interés (o su cuota
    fija si tiene); lo que sobra va completo a la deuda objetivo (avalancha =
    mayor tasa, bola = menor saldo).
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
    if recortes:
        g_efectivo -= sum(r["ahorro"] for r in DATOS.get("recortes_posibles", []))
    return libre, bono, g_efectivo, g_bono


def aplicar_escenario(esc):
    deudas = []
    for d in DATOS["deudas"]:
        nueva = dict(d)
        for clave, cambios in esc["ajustes"].items():
            if d["nombre"].startswith(clave):
                nueva.update(cambios)
        deudas.append(nueva)
    return deudas


def diagnostico():
    deudas = DATOS["deudas"]
    libre, bono, g_ef, g_bono = flujo_caja()
    _, _, g_ef_rec, _ = flujo_caja(recortes=True)
    total_deuda = sum(d["saldo"] for d in deudas)
    interes_mes = sum(d["saldo"] * d["tasa_mensual"] for d in deudas)
    pago_actual = sum(d.get("pago_actual", 0) for d in deudas)
    disponible = libre - g_ef

    print("=" * 76)
    print("DIAGNÓSTICO FINANCIERO")
    print("=" * 76)
    print(f"Ingreso neto mensual:              {cop(libre + bono)}")
    print(f"  Bancolombia (libre uso):         {cop(libre)}")
    print(f"  Tarjeta bono:                    {cop(bono)}")
    print(f"Gastos que salen de Bancolombia:   {cop(g_ef)}")
    print(f"Gastos pagados con bono:           {cop(g_bono)}  (sobra en bono {cop(bono - g_bono)})")
    print(f"Queda en Bancolombia para deudas:  {cop(disponible)}"
          f"   (con recortes: {cop(libre - g_ef_rec)})")
    print(f"Lo que hoy pagas a deudas:         {cop(pago_actual)}")
    print(f"  => hueco mensual:                {cop(disponible - pago_actual)}")
    print()
    print(f"Deuda total:                       {cop(total_deuda)}"
          f"  ({total_deuda / (libre + bono):.0f} meses de sueldo completo)")
    print(f"Intereses que genera al mes:       {cop(interes_mes)}"
          f"  ({interes_mes / (libre + bono):.0%} del ingreso)")
    print()
    print(f"{'Deuda':44} {'Saldo':>13} {'Tasa':>6} {'E.A.':>7} {'Interés/mes':>12}")
    for d in sorted(deudas, key=lambda d: -d["tasa_mensual"]):
        print(f"{d['nombre']:44} {cop(d['saldo']):>13} {d['tasa_mensual']:>6.2%} "
              f"{tasa_ea(d['tasa_mensual']):>7.1%} {cop(d['saldo'] * d['tasa_mensual']):>12}")
    return libre - g_ef_rec


def escenarios(pagos):
    print()
    print("=" * 76)
    print("ESCENARIOS DE NEGOCIACIÓN")
    print("=" * 76)
    for esc in DATOS["escenarios_negociacion"]:
        deudas = aplicar_escenario(esc)
        total = sum(d["saldo"] for d in deudas)
        interes = sum(d["saldo"] * d["tasa_mensual"] for d in deudas)
        print(f"\n{esc['nombre']}")
        print(f"  Deuda {cop(total)}; intereses al mes {cop(interes)}")
        for plazo in (60, 84):
            req = sum(cuota_credito(d["saldo"], d["tasa_mensual"], plazo) for d in deudas)
            print(f"  Para salir en {plazo} meses se necesitan {cop(req)}/mes")
        for p in pagos:
            meses, int_total, _ = simular(deudas, p)
            txt = "NUNCA se paga" if meses is None else \
                f"libre en {meses} meses ({meses / 12:.1f} años), intereses {cop(int_total)}"
            print(f"  Destinando {cop(p)}/mes -> {txt}")


if __name__ == "__main__":
    disponible_rec = diagnostico()
    if len(sys.argv) > 1:
        pagos = [float(a) for a in sys.argv[1:]]
    else:
        pagos = [disponible_rec, disponible_rec + 2_000_000, disponible_rec + 4_000_000]
        print(f"\nEscenarios con {cop(disponible_rec)} (con recortes), +2M y +4M de ingreso extra.")
    escenarios(pagos)
