"""Verificá tu instalación antes de la clase 1. Con el entorno activado, en la carpeta del kit:

    python verificar.py            # Python, paquetes, datos, Ollama y el modelo
    python verificar.py --agente   # además, el agente responde una pregunta de respuesta conocida

Usa el modelo de LLM_MODELO (por defecto qwen3.5:0.8b). Los pasos de instalación están en INSTALACION.md.
"""
from __future__ import annotations

import importlib
import json
import os
import shutil
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
sys.path.insert(0, str(RAIZ))
MODELO = os.environ.get("LLM_MODELO", "qwen3.5:0.8b")
URL = (os.environ.get("LLM_BASE_URL") or "http://localhost:11434").rstrip("/")
URL = URL[:-3] if URL.endswith("/v1") else URL
faltan: list[str] = []


def ok(texto: str) -> None:
    print(f"  [OK]    {texto}")


def ojo(texto: str) -> None:
    print(f"  [OJO]   {texto}")


def falta(texto: str, arreglo: str) -> None:
    faltan.append(texto)
    print(f"  [FALTA] {texto}\n          -> {arreglo}")


def ram_gb() -> float | None:
    try:
        if sys.platform == "win32":
            import ctypes

            class Memoria(ctypes.Structure):
                _fields_ = [("largo", ctypes.c_ulong), ("carga", ctypes.c_ulong), ("total", ctypes.c_ulonglong),
                            ("libre", ctypes.c_ulonglong), ("resto", ctypes.c_ulonglong * 5)]
            m = Memoria()
            m.largo = ctypes.sizeof(Memoria)
            ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
            return m.total / 2**30
        if sys.platform == "darwin":
            import subprocess
            return int(subprocess.check_output(["sysctl", "-n", "hw.memsize"])) / 2**30
        return os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2**30
    except Exception:
        return None


def pedir(ruta: str) -> dict:
    with urllib.request.urlopen(URL + ruta, timeout=5) as r:
        return json.load(r)


def computadora_y_python() -> None:
    print("\n1. Tu computadora y Python")
    ram = ram_gb()
    if ram is None:
        ojo("no pude medir la memoria; con menos de 8 GB, cerrá programas pesados")
    elif ram < 7.5:
        ojo(f"memoria: {ram:.0f} GB, menos de lo recomendado; cerrá programas pesados o usá Codespaces")
    else:
        ok(f"memoria: {ram:.0f} GB" + (" (te alcanza también para qwen3.5:4b)" if ram >= 15.5 else ""))
    libre = shutil.disk_usage(Path.home()).free / 2**30
    (ok if libre >= 3 else ojo)(f"disco libre: {libre:.0f} GB" + ("" if libre >= 3 else " (el modelo ocupa 1 GB)"))
    v = sys.version_info
    if v >= (3, 9):
        ok(f"Python {v.major}.{v.minor}.{v.micro}")
    else:
        falta(f"Python {v.major}.{v.minor} es muy viejo", "instalá Python 3.12 de python.org y recreá el entorno")
    for modulo, paquete in [("pandas", "pandas"), ("numpy", "numpy"), ("statsmodels", "statsmodels"),
                            ("sklearn", "scikit-learn"), ("matplotlib", "matplotlib"), ("jupyterlab", "jupyter")]:
        try:
            ok(f"{paquete} {getattr(importlib.import_module(modulo), '__version__', '')}")
        except ImportError:
            falta(f"falta {paquete}", "activá el entorno (.venv) y corré: pip install -r requirements.txt")
    if (RAIZ / "datos" / "programa_x.csv").exists():
        ok("datos del kit")
    else:
        falta("no encuentro datos/programa_x.csv", "este archivo tiene que estar en la carpeta del kit, junto a README.md")


def ollama() -> bool:
    print("\n2. Ollama y el modelo")
    try:
        ok(f"Ollama {pedir('/api/version')['version']} responde en {URL}")
    except Exception:
        falta(f"Ollama no responde en {URL}",
              "abrí la app de Ollama (o corré `ollama serve` en otra terminal); si no la instalaste, ver INSTALACION.md")
        return False
    nombres = [m["name"] for m in pedir("/api/tags").get("models", [])]
    if MODELO in nombres or f"{MODELO}:latest" in nombres:
        ok(f"modelo {MODELO} descargado")
        return True
    tenes = f" (tenés: {', '.join(nombres)})" if nombres else ""
    falta(f"el modelo {MODELO} no está descargado{tenes}", f"ollama pull {MODELO}")
    return False


def primer_prompt() -> None:
    print("\n3. Primer prompt")
    from agente.llm import Ollama
    llm = Ollama(MODELO)
    try:
        t = time.time()
        texto = llm.completar("Respondé con una sola palabra.", [{"role": "user", "content": "¿Cuál es la capital de Uruguay?"}])
        ok(f"respondió «{texto.strip()[:60]}» en {time.time() - t:.0f} s (la primera vez incluye cargar el modelo)")
        t, antes = time.time(), llm.tokens["salida"]
        llm.completar("Respondé en tres oraciones.", [{"role": "user", "content": "¿Qué es un agente de IA?"}])
        velocidad = (llm.tokens["salida"] - antes) / (time.time() - t)
    except RuntimeError as e:
        falta("el modelo no respondió", str(e))
        return
    if velocidad >= 5:
        ok(f"velocidad: {velocidad:.0f} tokens por segundo")
    else:
        ojo(f"velocidad: {velocidad:.1f} tokens por segundo, lento para clase: cerrá programas pesados")


def agente() -> None:
    print("\n4. El agente completo: pensar, ejecutar, observar")
    try:
        import pandas as pd
    except ImportError:
        falta("sin pandas no puedo correr el agente", "pip install -r requirements.txt")
        return
    from agente.harness import ejecutar_agente, leer_traza
    from agente.llm import Ollama
    df = pd.read_csv(RAIZ / "datos" / "programa_x.csv")
    esperado = int((df["participa"] == 1).sum())
    pregunta = ("¿Cuántas personas del archivo participaron del programa (participa == 1)? "
                "Contalas con código y reportá ese número en 'estimacion'.")
    try:
        c = ejecutar_agente(pregunta, df, Ollama(MODELO), max_pasos=6,
                            carpeta_trazas=RAIZ / "trazas" / "verificacion", etiqueta="verificacion")
    except RuntimeError as e:
        falta("el agente no pudo correr", str(e))
        return
    codigos = [e for e in leer_traza(c.traza) if e["tipo"] == "codigo"]
    try:
        correcto = float((c.respuesta or {}).get("estimacion")) == esperado
    except (TypeError, ValueError):
        correcto = False
    resumen = f"{len(codigos)} bloque(s) de código, {c.pasos} paso(s), {c.segundos:.0f} s"
    if correcto:
        ok(f"respondió {esperado}, que es lo correcto ({resumen})")
    elif c.respuesta is None:
        falta(f"el agente no terminó ({resumen})", "corré de nuevo; si se repite, probá otro modelo y avisale al docente")
    else:
        ojo(f"respondió {c.respuesta.get('estimacion')!r} y lo correcto es {esperado} ({resumen}): "
            "el ciclo funciona, pero el modelo se equivocó")
    print(f"          la traza quedó en {c.traza.relative_to(RAIZ)}: abrila y mirá qué ejecutó")


if __name__ == "__main__":
    print(f"Verificando el kit en {RAIZ}")
    computadora_y_python()
    if ollama():
        primer_prompt()
        if "--agente" in sys.argv:
            agente()
    if faltan:
        print(f"\nFalta resolver {len(faltan)} cosa(s). Seguí las indicaciones de cada [FALTA] y volvé a correr esto.")
    else:
        print("\nTodo listo." + ("" if "--agente" in sys.argv else " Para probar el agente completo: python verificar.py --agente"))
    sys.exit(1 if faltan else 0)
