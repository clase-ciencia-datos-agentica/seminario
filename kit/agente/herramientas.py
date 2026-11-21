"""Herramientas verificadas para estimar el efecto del programa sobre los participantes (ATT).

Sesión 4: se le dan al agente para que no reinvente diagnósticos (práctica "equipar").
También las usa el docente para calcular los resultados de referencia.

Todas las funciones reciben un DataFrame con las columnas de datos/programa_x.csv.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LogisticRegression

INSTRUCCIONES = """
HERRAMIENTAS: tenés disponible el módulo `h` (ya importado) con funciones verificadas:
  h.dif_medias(df), h.mco(df), h.emparejamiento(df), h.ipw(df), h.doble_robusto(df) -> número
  h.intervalo_bootstrap(df, h.doble_robusto, B=200) -> (inferior, superior)
  h.solapamiento(df), h.balance(df), h.placebo(df), h.valor_robustez(df), h.recortar(df)
Usalas en lugar de reescribir esos cálculos.
REGLAS DE CALIBRACIÓN:
- Reportá siempre un intervalo de 95%.
- Corré solapamiento, balance, placebo y sensibilidad, y decí qué mostró cada uno.
- Si el intervalo del placebo no contiene 0, decilo en las afirmaciones y bajá tu confianza.
- Abstenete si el tamaño efectivo de controles es menor que 30.
"""

T, Y = "participa", "ingreso_post"
BASE = ["edad", "anios_educ", "afro", "hispano", "casado", "sin_titulo", "ingreso_t1", "ingreso_t2"]


def covariables(df: pd.DataFrame, excluir: tuple[str, ...] = ()) -> pd.DataFrame:
    """Covariables estándar: las de base, edad al cuadrado e indicadores de ingreso cero."""
    X = df[[c for c in BASE if c not in excluir]].astype(float).copy()
    X["edad2"] = X["edad"] ** 2
    for c in ("ingreso_t1", "ingreso_t2"):
        if c in X:
            X[f"{c}_cero"] = (X[c] == 0).astype(float)
    return X


def propension(df, excluir=()) -> np.ndarray:
    X = covariables(df, excluir)
    X = (X - X.mean()) / X.std().replace(0, 1)
    m = LogisticRegression(C=1e4, max_iter=5000).fit(X, df[T])
    return m.predict_proba(X)[:, 1]


# ---------- estimadores (todos devuelven un float: efecto sobre los participantes) ----------

def dif_medias(df, y=Y, excluir=()):
    return df.loc[df[T] == 1, y].mean() - df.loc[df[T] == 0, y].mean()


def mco(df, y=Y, excluir=()):
    X = sm.add_constant(pd.concat([df[[T]].astype(float), covariables(df, excluir)], axis=1))
    return sm.OLS(df[y].astype(float), X).fit().params[T]


def emparejamiento(df, y=Y, excluir=()):
    """1 a 1, vecino más cercano en el logit de la propensión, con reemplazo."""
    e = np.clip(propension(df, excluir), 1e-6, 1 - 1e-6)
    lg = np.log(e / (1 - e))
    t = df[T].values == 1
    lt, lc = lg[t], lg[~t]
    orden = np.argsort(lc)
    pos = np.clip(np.searchsorted(lc[orden], lt), 1, len(lc) - 1)
    izq, der = orden[pos - 1], orden[pos]
    elegido = np.where(np.abs(lc[izq] - lt) <= np.abs(lc[der] - lt), izq, der)
    yv = df[y].values.astype(float)
    return (yv[t] - yv[~t][elegido]).mean()


def ipw(df, y=Y, excluir=()):
    e = np.clip(propension(df, excluir), 1e-6, 1 - 1e-6)
    t = df[T].values == 1
    w = e[~t] / (1 - e[~t])
    yv = df[y].values.astype(float)
    return yv[t].mean() - np.sum(w * yv[~t]) / w.sum()


def doble_robusto(df, y=Y, excluir=()):
    """AIPW para el efecto sobre los tratados: regresión en controles + pesos de propensión."""
    e = np.clip(propension(df, excluir), 1e-6, 1 - 1e-6)
    t = df[T].values == 1
    X = sm.add_constant(covariables(df, excluir))
    yv = df[y].values.astype(float)
    m0 = sm.OLS(yv[~t], X[~t]).fit().predict(X)
    w = e[~t] / (1 - e[~t])
    return (yv[t] - m0[t]).mean() - np.sum(w * (yv[~t] - m0[~t])) / w.sum()


ESTIMADORES = {
    "dif_medias": dif_medias, "mco": mco, "emparejamiento": emparejamiento,
    "ipw": ipw, "doble_robusto": doble_robusto,
}


def intervalo_bootstrap(df, estimador, B=200, nivel=0.95, semilla=0, **kw):
    """Intervalo percentil por bootstrap, remuestreando tratados y controles por separado."""
    rng = np.random.default_rng(semilla)
    tr, co = df[df[T] == 1], df[df[T] == 0]
    est = []
    for _ in range(B):
        b = pd.concat([tr.sample(len(tr), replace=True, random_state=rng.integers(1e9)),
                       co.sample(len(co), replace=True, random_state=rng.integers(1e9))])
        est.append(estimador(b, **kw))
    a = (1 - nivel) / 2
    return float(np.quantile(est, a)), float(np.quantile(est, 1 - a))


# ---------- diagnósticos ----------

def solapamiento(df, excluir=()) -> dict:
    """Resumen de la propensión: cuánto se parecen tratados y controles."""
    e = propension(df, excluir)
    t = df[T].values == 1
    return {
        "propension_tratados_p10_p50_p90": np.round(np.quantile(e[t], [.1, .5, .9]), 3).tolist(),
        "propension_controles_p10_p50_p90": np.round(np.quantile(e[~t], [.1, .5, .9]), 3).tolist(),
        "controles_con_propension_mayor_0.1": int((e[~t] > 0.1).sum()),
        "tratados_por_encima_del_max_control": int((e[t] > e[~t].max()).sum()),
        "tamano_efectivo_controles_ipw": float(_n_efectivo(e[~t] / (1 - e[~t]))),
    }


def _n_efectivo(w):
    return w.sum() ** 2 / (w ** 2).sum()


def balance(df, excluir=()) -> pd.DataFrame:
    """Diferencias de medias estandarizadas, antes y después de ponderar por IPW."""
    X = covariables(df, excluir)
    e = np.clip(propension(df, excluir), 1e-6, 1 - 1e-6)
    t = df[T].values == 1
    w = e[~t] / (1 - e[~t])
    filas = []
    for c in X:
        xt, xc = X[c].values[t], X[c].values[~t]
        sd = np.sqrt((xt.var() + xc.var()) / 2) or 1.0
        filas.append({"variable": c,
                      "dme_antes": (xt.mean() - xc.mean()) / sd,
                      "dme_despues": (xt.mean() - np.sum(w * xc) / w.sum()) / sd})
    return pd.DataFrame(filas).round(3)


def placebo(df, estimador=doble_robusto) -> float:
    """Efecto 'del programa' sobre el ingreso previo t2, que no pudo haber afectado.

    Se excluye ingreso_t2 de las covariables. Un valor lejos de cero es una alarma.
    """
    return estimador(df, y="ingreso_t2", excluir=("ingreso_t2",))


def valor_robustez(df, q=1.0, alfa=None) -> dict:
    """Cinelli & Hazlett (2020): qué tan fuerte tendría que ser un confusor oculto
    (en R² parcial con tratamiento y resultado) para reducir la estimación MCO en 100·q %."""
    X = sm.add_constant(pd.concat([df[[T]].astype(float), covariables(df)], axis=1))
    fit = sm.OLS(df[Y].astype(float), X).fit()
    tval, gl = fit.tvalues[T], fit.df_resid
    f = q * abs(tval) / np.sqrt(gl)
    rv = 0.5 * (np.sqrt(f ** 4 + 4 * f ** 2) - f ** 2)
    r2_parcial = tval ** 2 / (tval ** 2 + gl)
    return {"estimacion_mco": float(fit.params[T]), "t": float(tval),
            "valor_robustez": float(rv), "r2_parcial_tratamiento": float(r2_parcial)}


def recortar(df, bajo=0.05, alto=0.95, excluir=()) -> pd.DataFrame:
    """Deja solo la región de soporte común. Cambia la población: decilo en el reporte."""
    e = propension(df, excluir)
    return df[(e >= bajo) & (e <= alto)]
