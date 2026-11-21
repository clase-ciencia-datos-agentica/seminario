"""Agente mínimo de análisis de datos: un modelo, una herramienta (ejecutar Python) y un ciclo.

Se lee de punta a punta en diez minutos. Eso es parte del punto: si no entendés el ciclo,
no podés decidir cuánto confiar en lo que devuelve.

    from agente.harness import ejecutar_agente
    from agente.llm import desde_entorno
    corrida = ejecutar_agente("¿El programa aumentó los ingresos?", df, desde_entorno())
"""
from __future__ import annotations

import contextlib
import io
import json
import re
import time
import traceback
import uuid
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

SISTEMA_BASE = """Sos un analista de datos. Trabajás en Python con pandas, numpy, statsmodels y scikit-learn.
La variable `df` ya tiene los datos cargados.
Para ejecutar código, escribí UN bloque ```python ... ``` por mensaje. Vas a recibir lo que imprima.
Cuando termines, respondé SOLO con un bloque ```json ... ``` con estas claves:
  "estimacion": número, "ic_inferior": número o null, "ic_superior": número o null,
  "metodo": texto, "diagnosticos": lista de textos, "afirmaciones": lista de frases con los números que reportás,
  "abstiene": true o false, "justificacion": texto breve."""

BLOQUE = re.compile(r"```(python|json)\s*\n(.*?)```", re.S)


@dataclass
class Corrida:
    id: str
    respuesta: dict | None
    pasos: int
    traza: Path
    segundos: float
    error: str | None = None


class Ejecutor:
    """Ejecuta código en un espacio de nombres que persiste entre pasos, como un notebook."""

    def __init__(self, df: pd.DataFrame, extra: dict | None = None):
        import numpy as np
        self.ns = {"df": df.copy(), "pd": pd, "np": np, **(extra or {})}

    def ejecutar(self, codigo: str, limite: int = 4000) -> str:
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                exec(codigo, self.ns)
        except Exception:
            buf.write(traceback.format_exc(limit=2))
        out = buf.getvalue() or "(sin salida: usá print)"
        return out if len(out) <= limite else out[:limite] + f"\n...[recortado: {len(out)} caracteres]"


def _registrar(traza: Path, **evento):
    with traza.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"t": time.time(), **evento}, ensure_ascii=False, default=str) + "\n")


def ejecutar_agente(pregunta: str, df: pd.DataFrame, llm, sistema: str = SISTEMA_BASE,
                    max_pasos: int = 12, herramientas: dict | None = None,
                    carpeta_trazas: str | Path = "trazas", etiqueta: str = "corrida") -> Corrida:
    """Corre el ciclo pensar → ejecutar → observar hasta obtener la respuesta final en JSON."""
    inicio = time.time()
    id_ = f"{etiqueta}-{uuid.uuid4().hex[:8]}"
    traza = Path(carpeta_trazas) / f"{id_}.jsonl"
    traza.parent.mkdir(parents=True, exist_ok=True)
    _registrar(traza, tipo="inicio", pregunta=pregunta, sistema=sistema, modelo=getattr(llm, "nombre", "?"))

    ejecutor = Ejecutor(df, herramientas)
    mensajes = [{"role": "user", "content": pregunta}]
    for paso in range(1, max_pasos + 1):
        texto = llm.completar(sistema, mensajes)
        mensajes.append({"role": "assistant", "content": texto})
        bloques = BLOQUE.findall(texto)
        codigo = [b for tipo, b in bloques if tipo == "python"]
        final = [b for tipo, b in bloques if tipo == "json"]

        if codigo:  # el agente quiere ejecutar algo: lo ejecutamos y le mostramos la salida
            salida = ejecutor.ejecutar(codigo[0])
            _registrar(traza, tipo="codigo", paso=paso, texto=texto, codigo=codigo[0], salida=salida)
            mensajes.append({"role": "user", "content": f"Salida:\n{salida}"})
            continue
        if final:  # el agente terminó: validamos que el JSON se pueda leer
            try:
                respuesta = json.loads(final[-1])
            except json.JSONDecodeError as e:
                _registrar(traza, tipo="json_invalido", paso=paso, texto=texto, error=str(e))
                mensajes.append({"role": "user", "content": f"Ese JSON no es válido ({e}). Devolvelo corregido."})
                continue
            _registrar(traza, tipo="final", paso=paso, texto=texto, respuesta=respuesta)
            return Corrida(id_, respuesta, paso, traza, time.time() - inicio)
        _registrar(traza, tipo="texto", paso=paso, texto=texto)
        mensajes.append({"role": "user", "content": "Seguí: ejecutá un bloque de Python o devolvé el JSON final."})

    _registrar(traza, tipo="sin_final", paso=max_pasos)
    return Corrida(id_, None, max_pasos, traza, time.time() - inicio, error="no terminó")


def correr_varias(n: int, pregunta: str, df: pd.DataFrame, llm, **kw) -> pd.DataFrame:
    """Corre el agente n veces y devuelve una fila por corrida."""
    filas, etiqueta = [], kw.pop("etiqueta", "corrida")
    for i in range(n):
        c = ejecutar_agente(pregunta, df, llm, etiqueta=etiqueta, **kw)
        r = c.respuesta or {}
        filas.append({
            "corrida": c.id, "estimacion": r.get("estimacion"), "ic_inferior": r.get("ic_inferior"),
            "ic_superior": r.get("ic_superior"), "metodo": r.get("metodo"),
            "abstiene": bool(r.get("abstiene", False)), "diagnosticos": r.get("diagnosticos", []),
            "afirmaciones": r.get("afirmaciones", []), "pasos": c.pasos, "segundos": round(c.segundos, 1),
            "error": c.error, "traza": str(c.traza),
        })
        print(f"[{i + 1}/{n}] {filas[-1]['metodo']!s:30.30} estimación={filas[-1]['estimacion']}")
    return pd.DataFrame(filas)


def con_especificacion(espec: str, base: str = SISTEMA_BASE) -> str:
    """Agrega la especificación (sin los comentarios de la plantilla) al mensaje de sistema."""
    espec = re.sub(r"<!--.*?-->", "", espec, flags=re.S).strip()
    return base + "\n\nESPECIFICACIÓN DEL ANÁLISIS (obligatoria):\n" + espec


def leer_traza(ruta: str | Path) -> list[dict]:
    return [json.loads(l) for l in Path(ruta).read_text(encoding="utf-8").splitlines()]
