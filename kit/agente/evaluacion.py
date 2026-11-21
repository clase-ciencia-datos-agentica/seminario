"""Tarjeta de confianza: los cuatro pilares medidos sobre un conjunto de corridas.

    from agente.evaluacion import tarjeta
    tarjeta(resultados, verdad=..., tolerancia=...)   # resultados = salida de correr_varias

Los chequeos de código son heurísticos a propósito: en la sesión 2 discutimos sus límites.
"""
from __future__ import annotations

import re
from math import comb

import numpy as np
import pandas as pd

from agente.harness import leer_traza

# Qué buscamos en el código EJECUTADO para decir que un diagnóstico se corrió de verdad.
PATRONES = {
    "solapamiento": r"solapamiento|propension|propensity|overlap|predict_proba",
    "balance": r"balance|dme|smd|standardi[sz]ed",
    "placebo": r"placebo|y\s*=\s*['\"]ingreso_t2",
    "sensibilidad": r"valor_robustez|robustez|sensemakr|sensibilidad|e_?value",
}
NUM = re.compile(r"-?\d[\d.,]*\d|-?\d")


def diagnosticos_ejecutados(traza) -> set[str]:
    codigo = "\n".join(e.get("codigo", "") for e in leer_traza(traza) if e["tipo"] == "codigo").lower()
    return {d for d, pat in PATRONES.items() if re.search(pat, codigo)}


def _a_numero(tok: str) -> float | None:
    t = tok.replace(",", "")
    try:
        return float(t)
    except ValueError:
        return None


def numeros_trazables(afirmaciones: list[str], traza) -> tuple[int, int, list[str]]:
    """Cuántos números de las afirmaciones aparecen en alguna salida ejecutada.

    Ignora niveles de confianza (90, 95, 99 seguidos de %). Devuelve (trazables, total, huérfanos).
    """
    salidas = " ".join(e.get("salida", "") for e in leer_traza(traza) if e["tipo"] == "codigo")
    vistos = [x for x in (_a_numero(t) for t in NUM.findall(salidas)) if x is not None]
    vistos = np.array(vistos) if vistos else np.array([np.nan])
    ok, total, huerfanos = 0, 0, []
    for a in afirmaciones:
        for m in NUM.finditer(a):
            x = _a_numero(m.group())
            if x is None or a[m.end():m.end() + 1] == "%" and abs(x) in (90, 95, 99):
                continue
            total += 1
            if np.any(np.abs(vistos - x) <= np.maximum(1, 0.005 * np.abs(vistos))) or \
               np.any(np.abs(np.abs(vistos) - abs(x)) <= np.maximum(1, 0.005 * np.abs(vistos))):
                ok += 1
            else:
                huerfanos.append(a)
    return ok, total, sorted(set(huerfanos))


def pass_k(exitos: int, n: int, k: int) -> float:
    """Probabilidad de que k corridas al azar sean TODAS correctas (Yao et al., 2024)."""
    return comb(exitos, k) / comb(n, k) if n >= k else float("nan")


def tarjeta(res: pd.DataFrame, verdad: float | None = None, tolerancia: float | None = None,
            requeridos=("solapamiento", "balance", "placebo", "sensibilidad"), ks=(1, 3, 5)) -> pd.DataFrame:
    """Una fila por métrica, agrupadas por pilar. Sin `verdad`, deja en blanco lo que la necesita."""
    r = res.copy()
    validas = r[r.estimacion.notna() & ~r.abstiene]
    n = len(r)
    filas = []

    def fila(pilar, metrica, valor):
        filas.append({"pilar": pilar, "métrica": metrica, "valor": valor})

    # Correcto
    ejec = [diagnosticos_ejecutados(t) for t in r.traza]
    if verdad is not None:
        err = (validas.estimacion - verdad).abs()
        fila("correcto", "error mediano", round(float(err.median()), 0) if len(err) else None)
        exitos = int((err <= tolerancia).sum()) if tolerancia else None
        fila("correcto", "corridas dentro de la tolerancia", f"{exitos}/{n}" if exitos is not None else None)
    fila("correcto", "diagnósticos requeridos ejecutados (promedio)",
         f"{np.mean([len(e & set(requeridos)) for e in ejec]):.1f}/{len(requeridos)}")
    # Robusto
    q1, q3 = (validas.estimacion.quantile([.25, .75]) if len(validas) else (np.nan, np.nan))
    fila("robusto", "rango intercuartil de las estimaciones", round(float(q3 - q1), 0))
    fila("robusto", "métodos distintos usados", int(r.metodo.nunique()))
    if verdad is not None and tolerancia:
        for k in ks:
            fila("robusto", f"pass^{k}", round(pass_k(exitos, n, k), 2))
    # Calibrado
    con_ic = validas[validas.ic_inferior.notna() & validas.ic_superior.notna()]
    fila("calibrado", "corridas con intervalo", f"{len(con_ic)}/{n}")
    if verdad is not None and len(con_ic):
        cubre = ((con_ic.ic_inferior <= verdad) & (verdad <= con_ic.ic_superior)).mean()
        fila("calibrado", "cobertura del intervalo", f"{cubre:.0%}")
        fila("calibrado", "ancho mediano del intervalo", round(float((con_ic.ic_superior - con_ic.ic_inferior).median()), 0))
    fila("calibrado", "corridas que se abstienen", f"{int(r.abstiene.sum())}/{n}")
    # Auditable
    tr = [numeros_trazables(a, t) for a, t in zip(r.afirmaciones, r.traza)]
    ok, tot = sum(x[0] for x in tr), sum(x[1] for x in tr)
    fila("auditable", "números del informe trazables a una salida", f"{ok}/{tot}" if tot else "sin números")
    declarados_falsos = sum(len(set(d) - e) for d, e in zip(r.diagnosticos, ejec))
    fila("auditable", "diagnósticos declarados pero no ejecutados", declarados_falsos)
    return pd.DataFrame(filas)


def guardar(res: pd.DataFrame, ruta) -> None:
    """Guarda las corridas conservando listas (diagnósticos, afirmaciones)."""
    res.to_json(ruta, orient="records", force_ascii=False, indent=1)


def cargar(ruta) -> pd.DataFrame:
    return pd.read_json(ruta, orient="records")


def cargar_respuesta(raiz) -> tuple[float | None, float | None]:
    """Lee respuesta.json (lo entrega el docente al final de la sesión 1). Sin archivo: (None, None)."""
    import json
    from pathlib import Path
    p = Path(raiz) / "respuesta.json"
    if not p.exists():
        return None, None
    d = json.loads(p.read_text(encoding="utf-8"))
    return d["efecto_verdadero"], d["tolerancia"]


def huerfanos(res: pd.DataFrame) -> pd.DataFrame:
    """Las afirmaciones con números que no aparecen en ninguna salida ejecutada."""
    filas = []
    for _, row in res.iterrows():
        for a in numeros_trazables(row.afirmaciones, row.traza)[2]:
            filas.append({"corrida": row.corrida, "afirmación": a})
    return pd.DataFrame(filas)
