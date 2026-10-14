"""Diagnóstico financiero y plan de pago de deudas.

Uso:
    python3 planificador.py                 # diagnóstico + escenarios
    python3 planificador.py 3500000         # simula pagar 3.5M/mes a deudas

Edita datos.json con tus números reales y vuelve a correrlo.
"""
import json
import sys
from pathlib import Path

DATOS = json.loads((Path(__file__).parent / "datos.json").read_text(encoding="utf-8"))


def cop(x):
    return "$" + f"{x:,.0f}".replace(",", ".")


def tasa_ea(mensual):
    return (1 + mensual) ** 12 - 1


def simular(deudas, pago_mensual, orden="avalancha", max_meses=600):
    """Cada mes: se causan intereses, se paga el interés de todas y el resto
    se lleva completo a una deuda objetivo (avalancha = mayor tasa,
    bola de nieve = menor saldo). Devuelve (meses, interes_total, fechas_salida)."""
    saldos = {d["nombre"]: d["saldo"] for d in deudas}
    tasas = {d["nombre"]: d["tasa_mensual"] for d in deudas}
    interes_total = 0.0
    salida = {}
    for mes in range(1, max_meses + 1):
        disponible = pago_mensual
        for n in saldos:
            if saldos[n] > 0:
                i = saldos[n] * tasas[n]
                saldos[n] += i
                interes_total += i
        vivas = [n for n in saldos if saldos[n] > 0.5]
        if orden == "avalancha":
            vivas.sort(key=lambda n: -tasas[n])
        else:
            vivas.sort(key=lambda n: saldos[n])
        # Primero cubrir intereses de todas (para que ninguna crezca)
        for n in vivas:
            pago = min(saldos[n] * tasas[n] / (1 + tasas[n]), disponible)
            saldos[n] -= pago
            disponible -= pago
        # El sobrante va a la deuda objetivo, en orden
        for n in vivas:
            pago = min(saldos[n], disponible)
            saldos[n] -= pago
            disponible -= pago
            if saldos[n] <= 0.5 and n not in salida:
                salida[n] = mes
        if all(s <= 0.5 for s in saldos.values()):
            return mes, interes_total, salida
    return None, interes_total, salida


def cuota_credito(monto, tasa_mensual, meses):
    return monto * tasa_mensual / (1 - (1 + tasa_mensual) ** -meses)


def diagnostico():
    ing = DATOS["ingresos"]
    deudas = DATOS["deudas"]
    total_ing = sum(i["monto"] for i in ing)
    libre = sum(i["monto"] for i in ing if i["libre_uso"])
    gastos = sum(g["monto"] for g in DATOS["gastos_fijos"])
    total_deuda = sum(d["saldo"] for d in deudas)
    interes_mes = sum(d["saldo"] * d["tasa_mensual"] for d in deudas)

    print("=" * 70)
    print("DIAGNÓSTICO FINANCIERO")
    print("=" * 70)
    print(f"Ingreso total mensual:        {cop(total_ing)}")
    print(f"  de libre uso (Bancolombia): {cop(libre)}")
    print(f"  tarjeta bono:               {cop(total_ing - libre)}")
    print(f"Gastos fijos registrados:     {cop(gastos)}"
          + ("   <-- FALTAN DATOS" if gastos == 0 else ""))
    print(f"Deuda total:                  {cop(total_deuda)}")
    print(f"  = {total_deuda / total_ing:.1f} meses de ingreso completo")
    print(f"Intereses que genera al mes:  {cop(interes_mes)}")
    print(f"  = {interes_mes / total_ing:.0%} del ingreso total, "
          f"{interes_mes / libre:.0%} del dinero de libre uso")
    print(f"  = {cop(interes_mes * 12)} al año solo en intereses")
    print()
    print(f"{'Deuda':32} {'Saldo':>14} {'Tasa mes':>9} {'Tasa E.A.':>10} {'Interés/mes':>13}")
    for d in sorted(deudas, key=lambda d: -d["tasa_mensual"]):
        print(f"{d['nombre']:32} {cop(d['saldo']):>14} {d['tasa_mensual']:>9.2%} "
              f"{tasa_ea(d['tasa_mensual']):>10.1%} {cop(d['saldo'] * d['tasa_mensual']):>13}")
    return total_deuda, interes_mes


def escenarios(pagos):
    deudas = DATOS["deudas"]
    print()
    print("=" * 70)
    print("PLAN DE PAGO (pagando el interés de todas + el extra a una)")
    print("=" * 70)
    print(f"{'Pago mensual':>14} | {'Avalancha (mayor tasa)':^28} | {'Bola de nieve (menor saldo)':^28}")
    for p in pagos:
        fila = []
        for orden in ("avalancha", "bola"):
            meses, interes, _ = simular(deudas, p, orden)
            fila.append("nunca se paga" if meses is None
                        else f"{meses:3d} meses, int {cop(interes)}")
        print(f"{cop(p):>14} | {fila[0]:^28} | {fila[1]:^28}")


def orden_avalancha(pago):
    meses, interes, salida = simular(DATOS["deudas"], pago, "avalancha")
    print()
    print(f"Detalle avalancha pagando {cop(pago)}/mes:")
    for n, m in sorted(salida.items(), key=lambda x: x[1]):
        print(f"  mes {m:3d}: queda pagada -> {n}")
    if meses:
        print(f"  Libre de deudas en {meses} meses ({meses / 12:.1f} años). "
              f"Intereses totales: {cop(interes)}")


def refinanciacion(total_deuda, interes_mes):
    print()
    print("=" * 70)
    print("ESCENARIO: CAMBIAR TODA LA DEUDA POR UN CRÉDITO BANCARIO")
    print("=" * 70)
    print("(tasas de referencia aproximadas; confirmar con el banco)")
    for nombre, tasa in (("Libranza ~1,3% m.v.", 0.013),
                         ("Libre inversión ~1,8% m.v.", 0.018)):
        for plazo in (48, 60, 72):
            c = cuota_credito(total_deuda, tasa, plazo)
            print(f"  {nombre:28} {plazo} meses: cuota {cop(c)}, "
                  f"interés total {cop(c * plazo - total_deuda)}")
    print(f"  Hoy: {cop(interes_mes)}/mes solo de intereses, sin bajar capital.")


if __name__ == "__main__":
    total, interes = diagnostico()
    if len(sys.argv) > 1:
        pagos = [float(a) for a in sys.argv[1:]]
    else:
        pagos = [2_900_000, 3_200_000, 3_500_000, 4_000_000, 4_500_000]
    escenarios(pagos)
    orden_avalancha(pagos[len(pagos) // 2] if len(sys.argv) == 1 else pagos[0])
    refinanciacion(total, interes)
