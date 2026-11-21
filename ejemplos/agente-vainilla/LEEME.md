# Agente Vainilla

Un agente de IA que corre en tu computadora, gratis: un modelo abierto (Qwen3.5, de Alibaba) que sirve
Ollama, dos herramientas de Python y un ciclo. Lo vemos en vivo en la clase 1 de Ciencia de Datos
Agéntica y Defendible, y lo instalás antes de la clase 2. No necesitás cuenta, tarjeta ni clave, y los datos no salen de tu computadora.

## Instalación (antes de la clase 2)

Unos 20 minutos, casi todos esperando la descarga del modelo. Hacelo en tu casa, con buena conexión.

1. **Ollama.** Bajalo de [ollama.com/download](https://ollama.com/download): en macOS y Windows es una app;
   en Linux, `curl -fsSL https://ollama.com/install.sh | sh`. Instalalo y abrilo.
2. **El modelo** (3,3 a 4 GB). En una terminal:

   ```bash
   ollama pull qwen3.5:4b
   ```

3. **Python 3.9 o más nuevo.** Probá `python3 --version` (en Windows, `py --version`). Si no aparece una
   versión, instalalo de [python.org](https://www.python.org/downloads/).
4. **Este agente.** Descomprimí la carpeta, abrí una terminal adentro (ver abajo) y corré:

   ```bash
   python3 agent.py --check
   ```

   En Windows: `py agent.py --check`. Tiene que terminar en **Todo listo**.

No hay nada más que instalar: el agente usa solo la biblioteca estándar de Python.

**Abrir una terminal en la carpeta.** En macOS, abrí Terminal, escribí `cd ` (con espacio), arrastrá la
carpeta a la ventana y apretá Enter. En Windows, abrí la carpeta, hacé clic derecho en un espacio vacío y
elegí *Abrir en Terminal*.

## Cómo se usa

```bash
python3 agent.py                       # modo básico: la pregunta y dos herramientas
python3 agent.py --mode informed       # el mismo modelo, con el manual del curso
python3 agent.py --mode checked --data data/retention_duplicates.csv   # controles en Python
python3 agent.py --inspect             # las mismas cuentas, sin modelo
```

Cada corrida deja su registro completo en `runs/`: qué pidió el modelo, qué le devolvió Python, qué respondió.

## Qué hace y qué no

El modelo puede pedir solo dos cosas: `inspect_data()`, que revisa los datos, y
`summarize_retention(breakdown)`, que cuenta la retención por promoción, en total o dentro de los grupos
de una columna: ciudad, plataforma o frecuencia previa. Python hace las cuentas y le devuelve el resultado; el modelo decide qué pedir y cómo
contarlo. No ejecuta código propio ni sale a internet.

Que el programa diga `completed` quiere decir que terminó con una respuesta, no que la respuesta sea
correcta. Eso lo evaluamos en clase.

Los datos (`data/`) son sintéticos: 1.000 usuarios construidos para el ejercicio.

## Si tu computadora es más lenta

Con 8 GB de RAM, `qwen3.5:4b` funciona si cerrás el navegador y otros programas pesados. Si igual va muy
lento: `ollama pull qwen3.5:2b` y agregá `--model qwen3.5:2b` a cada comando.

## Si algo falla

| Lo que ves | Qué hacer |
| --- | --- |
| `python3: command not found`, o Windows abre la Microsoft Store | Instalá Python de python.org. En Windows usá `py` en lugar de `python3`. |
| `ollama: command not found` | Abrí la app de Ollama una vez y después una terminal nueva. |
| `No se pudo contactar Ollama` | Ollama no está abierto: abrí la app (en Linux, `ollama serve` en otra terminal). |
| `Modelo no descargado` | `ollama pull qwen3.5:4b` |
| `can't open file 'agent.py'` | La terminal no está en la carpeta del agente: ver arriba cómo abrirla ahí. |
| Cada turno tarda más de un minuto | Cerrá programas pesados o usá `qwen3.5:2b`. |

## Opcional

- `local_only.py` activa el modo solo local de Ollama (desactiva sus modelos en la nube). Cambia la
  configuración de Ollama de tu usuario y después hay que reiniciar Ollama.
- `python3 -m unittest discover -s tests` corre las pruebas del programa (no evalúan al modelo).
