"""Simulador de analista. NO es un modelo de lenguaje.

Sirve para dos cosas: correr los notebooks sin clave de API, y ver la mecánica del ciclo
antes de gastar en un modelo real. Imita conductas típicas de un agente:
  - sin instrucciones, elige un método al azar (a veces la diferencia de medias)
  - sigue la especificación que encuentra en el mensaje de sistema (diagnósticos, intervalos)
  - a veces agrega una afirmación que nunca calculó (para que la auditoría tenga algo que encontrar)
Las reglas están a la vista en este archivo: no hay nada que "aprenda".
"""
from __future__ import annotations

import json
import random
import re

NOMBRES = {"dif_medias": "diferencia de medias", "mco": "regresión MCO con covariables",
           "emparejamiento": "emparejamiento por propensión 1 a 1", "ipw": "ponderación por propensión inversa",
           "doble_robusto": "doble robusto (AIPW)"}


class Simulador:
    nombre = "simulador"

    def __init__(self, semilla: int | None = None, prob_invento: float = 0.35, B: int = 50, **_):
        self.rng = random.Random(semilla)
        self.prob_invento, self.B = prob_invento, B
        self.tokens = {"entrada": 0, "salida": 0}
        self.plan: dict = {}

    # ------------------------------------------------------------------ ciclo
    def completar(self, sistema: str, mensajes: list[dict]) -> str:
        if len(mensajes) == 1:
            self.plan = self._planear(sistema, mensajes[0]["content"])
            return "Voy a estimar el efecto.\n```python\n" + self._codigo() + "\n```"
        m = re.search(r"RESULTADO (\{.*\})", mensajes[-1]["content"])
        if not m:
            return "```json\n" + json.dumps({"estimacion": None, "abstiene": True, "metodo": "error",
                                              "diagnosticos": [], "afirmaciones": ["El código falló."],
                                              "ic_inferior": None, "ic_superior": None,
                                              "justificacion": mensajes[-1]["content"][-300:]}) + "\n```"
        res = json.loads(m.group(1))
        final = self._revision(res) if self.plan["revisor"] else self._final(res)
        return "```json\n" + json.dumps(final, ensure_ascii=False, indent=1) + "\n```"

    # ------------------------------------------------------------------ plan
    def _planear(self, sistema: str, pregunta: str) -> dict:
        s = sistema.lower()
        if "revisor" in s:
            inf = re.search(r"```json\s*\n(.*?)```", pregunta, re.S)
            return {"revisor": True, "informe": json.loads(inf.group(1)) if inf else {},
                    "metodo": "doble_robusto", "diag": {"intervalo", "placebo", "solapamiento"}}
        forzado = re.search(r"m[eé]todo obligatorio:\s*(\w+)", s)
        if forzado:
            metodo = forzado.group(1)
        elif "especificaci" in s:
            metodo = self.rng.choices(["doble_robusto", "ipw", "emparejamiento", "mco"], [.4, .25, .2, .15])[0]
        else:
            metodo = self.rng.choices(["dif_medias", "mco", "emparejamiento", "ipw"], [.35, .35, .15, .15])[0]
        diag = {d for d in ("solapamiento", "balance", "placebo", "sensibilidad") if d in s}
        if "intervalo" in s or metodo == "mco" or self.rng.random() < 0.3:
            diag.add("intervalo")
        estricto = "trazable" in s or "cada número" in s
        return {"revisor": False, "metodo": metodo, "diag": diag,
                "abstener": "absten" in s,
                "invento": self.rng.random() < (0.05 if estricto else self.prob_invento)}

    def _codigo(self) -> str:
        p, B = self.plan, self.B
        L = ["# (simulador) código equivalente al que escribiría un analista",
             "import json", "from agente import herramientas as h", "res = {}",
             f"res['estimacion'] = float(h.{p['metodo']}(df))",
             "print(f\"Estimación: {res['estimacion']:,.0f}\")"]
        if "intervalo" in p["diag"]:
            L += [f"res['ic'] = h.intervalo_bootstrap(df, h.{p['metodo']}, B={B})",
                  "print(f\"IC 95%: [{res['ic'][0]:,.0f}, {res['ic'][1]:,.0f}]\")"]
        if "solapamiento" in p["diag"]:
            L += ["res['solapamiento'] = h.solapamiento(df)", "print(res['solapamiento'])"]
        if "balance" in p["diag"]:
            L += ["b = h.balance(df)", "print(b.to_string())",
                  "res['max_dme_despues'] = float(b.dme_despues.abs().max())"]
        if "placebo" in p["diag"]:
            L += ["res['placebo'] = float(h.placebo(df))",
                  f"res['placebo_ic'] = h.intervalo_bootstrap(df, h.doble_robusto, B={B}, y='ingreso_t2', excluir=('ingreso_t2',))",
                  "print(f\"Placebo: {res['placebo']:,.0f} IC [{res['placebo_ic'][0]:,.0f}, {res['placebo_ic'][1]:,.0f}]\")"]
        if "sensibilidad" in p["diag"]:
            L += ["res['robustez'] = h.valor_robustez(df)", "print(res['robustez'])"]
        L.append("print('RESULTADO', json.dumps(res))")
        return "\n".join(L)

    # ------------------------------------------------------------------ respuestas
    def _final(self, res: dict) -> dict:
        p, est = self.plan, res["estimacion"]
        ic = res.get("ic") or [None, None]
        verbo = "aumentó" if est >= 0 else "redujo"
        af = [f"El programa {verbo} el ingreso posterior de los participantes en {abs(est):,.0f} en promedio."]
        if ic[0] is not None:
            af.append(f"Intervalo de 95%: [{ic[0]:,.0f}, {ic[1]:,.0f}].")
        if "placebo" in res:
            lo, hi = res["placebo_ic"]
            ok = lo <= 0 <= hi
            af.append(f"Placebo sobre ingreso_t2: {res['placebo']:,.0f} [{lo:,.0f}, {hi:,.0f}]; "
                      + ("no hay señal de confusión." if ok else "falla: hay señal de confusión."))
        if "robustez" in res:
            af.append(f"Valor de robustez: {res['robustez']['valor_robustez']:.3f}.")
        diag = sorted(p["diag"] - {"intervalo"})
        if p["invento"]:  # conducta a detectar en la sesión 5
            af.append(self.rng.choice(["El efecto es estadísticamente significativo (p = 0.003).",
                                       "Esto equivale a un aumento de 47% sobre el ingreso de los no participantes."]))
            diag = sorted(set(diag) | {"balance"})
        n_ef = res.get("solapamiento", {}).get("tamano_efectivo_controles_ipw", 1e9)
        abstiene = p["abstener"] and n_ef < 30
        if abstiene:
            af.append(f"Me abstengo: la ponderación descansa en {n_ef:,.1f} controles efectivos.")
        return {"estimacion": est, "ic_inferior": ic[0], "ic_superior": ic[1],
                "metodo": NOMBRES.get(p["metodo"], p["metodo"]), "diagnosticos": diag,
                "afirmaciones": af, "abstiene": abstiene,
                "justificacion": "Elegí el método y reporto lo que calculé."}

    def _revision(self, res: dict) -> dict:
        inf, est = self.plan["informe"], res["estimacion"]
        problemas = []
        rep = inf.get("estimacion")
        if rep is None:
            problemas.append("El informe no trae una estimación.")
        elif abs(rep - est) > 0.25 * abs(est):
            problemas.append(f"No reproduzco la estimación: el informe dice {rep:,.0f}, yo obtengo {est:,.0f} con doble robusto.")
        if inf.get("ic_inferior") is None:
            problemas.append("El informe no reporta incertidumbre.")
        lo, hi = res["placebo_ic"]
        texto = " ".join(inf.get("afirmaciones", [])).lower()
        if not (lo <= 0 <= hi) and "placebo" not in texto:
            problemas.append("La prueba placebo falla y el informe no lo menciona.")
        for a in inf.get("afirmaciones", []):
            if re.search(r"p\s*[=<]|\b(?!9[059]\b)\d+(?:[.,]\d+)?\s*%", a):
                problemas.append(f"Afirmación sin respaldo visible en el informe: «{a}»")
        return {"estimacion": est, "ic_inferior": res["ic"][0], "ic_superior": res["ic"][1],
                "metodo": "revisión independiente (doble robusto)", "diagnosticos": ["placebo", "solapamiento"],
                "afirmaciones": problemas or ["No encontré problemas."], "abstiene": False,
                "justificacion": f"{len(problemas)} problema(s) encontrados."}
