# Kit del seminario · Ciencia de datos agéntica confiable

Cinco sesiones, una pregunta: **¿cuánto aumentó un programa de empleo los ingresos de sus participantes?**
Le damos la pregunta a un agente de IA y lo hacemos, sesión a sesión, lo más confiable posible.

## Instalación

Paso a paso, con el modelo local y los problemas frecuentes: **`INSTALACION.md`**. En corto:

```bash
python -m venv .venv && source .venv/bin/activate   # en Windows: .venv\Scripts\activate
pip install -r requirements.txt
python verificar.py --agente                        # con Ollama y el modelo ya instalados
jupyter lab notebooks/
```

## Elegir el modelo

Por defecto los notebooks usan el **simulador**: un analista falso, con reglas a la vista en
`agente/simulador.py`. Sirve para entender la mecánica sin gastar.

**Gratis y en tu computadora (lo que usamos en clase):** [Ollama](https://ollama.com) con un modelo
abierto. Instalalo según `INSTALACION.md` y, en la primera celda del notebook:

```python
os.environ["LLM_PROVEEDOR"] = "ollama"
os.environ["LLM_MODELO"] = "qwen3.5:0.8b"
```

No hay clave ni costo, y los datos no salen de tu computadora.

**Con una API** (si el docente lo indica):

```bash
export LLM_PROVEEDOR=anthropic        # o openai
export LLM_MODELO=claude-haiku-5-5    # el modelo que indique el docente
export ANTHROPIC_API_KEY=...          # nunca la pegues en un notebook
```

Para otro servidor compatible con OpenAI (vLLM, etc.): `LLM_PROVEEDOR=openai`,
`LLM_BASE_URL` con su dirección y `LLM_MODELO` con el nombre del modelo.

**Costo y tiempo.** Las sesiones 3 y 4 corren el agente unas 40 veces. Con una API y un modelo
chico son centavos de dólar por corrida; revisá el contador `llm.tokens` antes de lanzar muchas.
Con Ollama no cuesta nada, pero en una laptop cada corrida tarda uno o varios minutos.

## Qué hay en el kit

| Carpeta | Contenido |
| --- | --- |
| `datos/` | Los datos (disfrazados) y su diccionario |
| `agente/harness.py` | El agente: un modelo, una herramienta (ejecutar Python), un ciclo. ~150 líneas |
| `agente/llm.py` | Adaptadores para Ollama (local), Anthropic, OpenAI y el simulador |
| `agente/herramientas.py` | Estimadores y diagnósticos verificados (sesión 4) |
| `agente/evaluacion.py` | La tarjeta de confianza: correcto, robusto, calibrado, auditable |
| `agente/revisor.py` | Un segundo agente que revisa al primero (sesión 5) |
| `especificaciones/` | El contrato de tarea (sesión 1) y la plantilla de especificación (sesión 2) |
| `notebooks/` | Un notebook por sesión |
| `INSTALACION.md`, `verificar.py` | Instalar el modelo local y comprobar que todo funciona |
| `trazas/`, `resultados/` | Se crean solos: cada paso de cada corrida queda registrado |

## Las sesiones

1. **Línea base.** El agente sin instrucciones. ¿Firmarías lo que devuelve?
2. **Correcto.** Definir "correcto" antes de construir: especificación y chequeos automáticos.
3. **Robusto.** Veinte corridas y un multiverso de métodos. ¿La respuesta sobrevive?
4. **Calibrado.** Intervalos, placebo, sensibilidad y saber cuándo abstenerse.
5. **Auditable.** Cada número trazable, un revisor independiente y la evaluación final con datos nuevos.

Al final de la sesión 1 el docente entrega `respuesta.json`: copialo a la raíz del kit.
