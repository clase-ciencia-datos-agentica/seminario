"""Adaptadores de modelos. Todos exponen lo mismo: completar(sistema, mensajes) -> texto.

Elegí el proveedor con variables de entorno:
    LLM_PROVEEDOR = ollama | anthropic | openai | simulador
    LLM_MODELO    = nombre del modelo (por ejemplo qwen3.5:4b o claude-haiku-5-5)
    LLM_BASE_URL  = opcional: otra dirección para Ollama, o un servidor compatible con OpenAI (vLLM, etc.)
Las claves van en ANTHROPIC_API_KEY u OPENAI_API_KEY, nunca en el notebook. Ollama no usa clave.
"""
from __future__ import annotations

import json
import os
import socket
import urllib.error
import urllib.request


class Ollama:
    """Un modelo abierto que corre en tu computadora: gratis, sin clave, y los datos no salen de ahí.

    Usa la API propia de Ollama, no la compatible con OpenAI, para poder fijar el contexto: Ollama
    trae 4096 tokens por defecto y el ciclo del agente los pasa en pocos pasos. Con pensar=False,
    los modelos que razonan antes de responder (como qwen3.5) contestan directo: mucho más rápido.
    """

    def __init__(self, modelo: str | None = None, temperatura: float | None = None, contexto: int = 16384,
                 max_tokens: int = 2048, pensar: bool | None = False, base_url: str | None = None):
        url = (base_url or os.environ.get("LLM_BASE_URL") or "http://localhost:11434").rstrip("/")
        self.url = url[:-3] if url.endswith("/v1") else url
        self.nombre = modelo or os.environ.get("LLM_MODELO", "qwen3.5:4b")
        self.temperatura, self.contexto, self.max_tokens, self.pensar = temperatura, contexto, max_tokens, pensar
        self.tokens = {"entrada": 0, "salida": 0}

    def completar(self, sistema: str, mensajes: list[dict]) -> str:
        opciones = {"num_ctx": self.contexto, "num_predict": self.max_tokens}
        if self.temperatura is not None:  # sin temperatura, usa la que recomienda el modelo
            opciones["temperature"] = self.temperatura
        cuerpo = {"model": self.nombre, "stream": False, "options": opciones,
                  "messages": [{"role": "system", "content": sistema}, *mensajes]}
        if self.pensar is not None:
            cuerpo["think"] = self.pensar
        r = self._chat(cuerpo)
        self.tokens["entrada"] += r.get("prompt_eval_count", 0)
        self.tokens["salida"] += r.get("eval_count", 0)
        return r["message"]["content"]

    def _chat(self, cuerpo: dict) -> dict:
        pedido = urllib.request.Request(self.url + "/api/chat", data=json.dumps(cuerpo).encode("utf-8"),
                                        headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(pedido, timeout=600) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            detalle = e.read().decode("utf-8", "replace")
            if e.code == 404:
                raise RuntimeError(f"Ollama no tiene el modelo {self.nombre}. "
                                   f"Descargalo con: ollama pull {self.nombre}") from None
            if "think" in cuerpo and "think" in detalle:  # el modelo no razona: se lo pedimos sin ese campo
                self.pensar = None
                return self._chat({k: v for k, v in cuerpo.items() if k != "think"})
            raise RuntimeError(f"Ollama respondió {e.code}: {detalle}") from None
        except urllib.error.URLError:
            raise RuntimeError(f"No encuentro Ollama en {self.url}. Abrí la app de Ollama "
                               "(o corré `ollama serve` en una terminal) y probá de nuevo.") from None
        except socket.timeout:
            raise RuntimeError(f"{self.nombre} tardó más de 10 minutos en responder. "
                               "Probá con un modelo más chico.") from None


class Anthropic:
    def __init__(self, modelo: str | None = None, temperatura: float = 1.0, max_tokens: int = 4000):
        import anthropic
        self.cliente = anthropic.Anthropic()
        self.nombre = modelo or os.environ.get("LLM_MODELO", "claude-haiku-5-5")
        self.temperatura, self.max_tokens = temperatura, max_tokens
        self.tokens = {"entrada": 0, "salida": 0}

    def completar(self, sistema: str, mensajes: list[dict]) -> str:
        r = self.cliente.messages.create(model=self.nombre, system=sistema, messages=mensajes,
                                         max_tokens=self.max_tokens, temperature=self.temperatura)
        self.tokens["entrada"] += r.usage.input_tokens
        self.tokens["salida"] += r.usage.output_tokens
        return "".join(b.text for b in r.content if b.type == "text")


class OpenAICompatible:
    def __init__(self, modelo: str | None = None, temperatura: float = 1.0, base_url: str | None = None):
        import openai
        self.cliente = openai.OpenAI(base_url=base_url or os.environ.get("LLM_BASE_URL"))
        self.nombre = modelo or os.environ["LLM_MODELO"]
        self.temperatura = temperatura
        self.tokens = {"entrada": 0, "salida": 0}

    def completar(self, sistema: str, mensajes: list[dict]) -> str:
        r = self.cliente.chat.completions.create(
            model=self.nombre, temperature=self.temperatura,
            messages=[{"role": "system", "content": sistema}, *mensajes])
        if r.usage:
            self.tokens["entrada"] += r.usage.prompt_tokens
            self.tokens["salida"] += r.usage.completion_tokens
        return r.choices[0].message.content or ""


def desde_entorno(**kw):
    proveedor = os.environ.get("LLM_PROVEEDOR", "simulador").lower()
    if proveedor == "ollama":
        return Ollama(**kw)
    if proveedor == "anthropic":
        return Anthropic(**kw)
    if proveedor == "openai":
        return OpenAICompatible(**kw)
    from agente.simulador import Simulador
    print("Usando el SIMULADOR (no es un modelo). Configurá LLM_PROVEEDOR para usar uno real.")
    return Simulador(**kw)
