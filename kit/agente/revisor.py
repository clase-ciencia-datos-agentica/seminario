"""Revisor independiente (sesión 5): otro agente que NO ve la traza del primero.

Recibe solo los datos, la especificación y el informe final, y trata de reproducirlo.
Lo que no puede reproducir lo marca como problema.
"""
from __future__ import annotations

import json

from agente.harness import SISTEMA_BASE, ejecutar_agente

SISTEMA_REVISOR = SISTEMA_BASE + """

Sos un REVISOR independiente. No confiás en el informe que te pasan: lo verificás.
1. Reproducí la estimación principal con tu propio código.
2. Para cada afirmación con un número, decidí si la podés reproducir.
3. Corré los diagnósticos que pide la especificación si el informe no los muestra.
En "afirmaciones" del JSON final, listá SOLO los problemas encontrados (o "No encontré problemas.")."""


def revisar(informe: dict, especificacion: str, df, llm, **kw):
    pregunta = (f"Especificación del análisis:\n{especificacion}\n\n"
                f"Informe a revisar:\n```json\n{json.dumps(informe, ensure_ascii=False, indent=1)}\n```")
    return ejecutar_agente(pregunta, df, llm, sistema=SISTEMA_REVISOR, etiqueta="revision", **kw)
