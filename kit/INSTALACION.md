# Instalación: el agente, gratis y en tu computadora

Para la clase 2 necesitás tres cosas: **el kit con Python**, **Ollama** (el programa que corre modelos
de lenguaje en tu computadora) y **un modelo abierto**. Todo es gratis: no hace falta cuenta, tarjeta
ni clave, y los datos nunca salen de tu computadora.

**¿Ya instalaste el Agente Vainilla?** Entonces Ollama y el modelo ya están: hacé los pasos 1, 5 y 6.

**Hacelo antes de la clase, con buena conexión:** el modelo pesa 1 GB. Calculá 15 minutos.
Si algo no funciona, mandale al docente la salida de `python verificar.py`.

## Qué necesitás

|  | Mínimo | Ideal |
| --- | --- | --- |
| Memoria (RAM) | 8 GB | 16 GB o más |
| Disco libre | 5 GB | 10 GB |
| Sistema | macOS 14 (Sonoma), Windows 10 22H2 o Linux | |

Si tu computadora no llega al mínimo, usá el curso desde el navegador con GitHub Codespaces (ver
`instalacion/codespaces.md` en el repositorio del curso), o el simulador del kit.

## 1. Python y el kit

Necesitás Python 3.10 o más nuevo (recomendado: 3.12, de [python.org](https://www.python.org/downloads/)).
Descomprimí el kit, abrí una terminal en esa carpeta y creá un entorno con los paquetes:

```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```powershell
# Windows (PowerShell)
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Cada vez que abras una terminal nueva para el curso, activá el entorno de nuevo (la segunda línea).

## 2. Ollama

- **macOS:** descargá [Ollama.dmg](https://ollama.com/download/Ollama.dmg), arrastrá Ollama a Aplicaciones
  y abrilo. Si te pide permiso para instalar el comando `ollama`, aceptá.
- **Windows:** descargá [OllamaSetup.exe](https://ollama.com/download/OllamaSetup.exe) e instalalo. No necesita
  permisos de administrador.
- **Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

Abrí una terminal **nueva** y comprobá: `ollama --version`

## 3. El modelo

En clase usamos **Qwen3.5 de 800 millones de parámetros**, el más chico de la familia, un modelo abierto (licencia Apache 2.0):

```bash
ollama pull qwen3.5:0.8b
```

| Tu computadora | Modelo | Descarga |
| --- | --- | --- |
| Cualquiera (el de la clase) | `qwen3.5:0.8b` | 1 a 1,3 GB |
| 16 GB de RAM o más (opcional, se equivoca menos) | `qwen3.5:4b` | 3,3 a 4 GB |

No uses modelos con `cloud` en el nombre: esos corren en los servidores de Ollama, no en tu computadora.

## 4. Tu primer prompt

```bash
ollama run qwen3.5:0.8b
```

Escribí una pregunta y apretá Enter. Primero vas a ver el razonamiento del modelo y después la respuesta.
Para salir, escribí `/bye`. Para que conteste sin razonar (más rápido): `ollama run qwen3.5:0.8b --think=false`.
También podés chatear desde la app de Ollama: elegí `qwen3.5:0.8b` en el selector de modelos.

## 5. Verificá todo

Con el entorno activado, en la carpeta del kit:

```bash
python verificar.py --agente
```

Revisa Python, los paquetes, Ollama y el modelo, y le hace al agente una pregunta con respuesta conocida.
Tiene que terminar en **Todo listo**. Cada `[FALTA]` dice cómo arreglarlo. Si usás otro modelo,
indicalo antes: `LLM_MODELO=qwen3.5:4b python verificar.py --agente` (en PowerShell:
`$env:LLM_MODELO="qwen3.5:4b"` y después el comando).

## 6. En los notebooks

En la primera celda de cada notebook, sacale el `#` del principio a estas dos líneas:

```python
os.environ["LLM_PROVEEDOR"] = "ollama"
os.environ["LLM_MODELO"] = "qwen3.5:0.8b"
```

Sin ellas, el notebook usa el simulador. Ollama no usa clave: no hay nada secreto en esas líneas.

## Problemas frecuentes

| Síntoma | Qué hacer |
| --- | --- |
| `ollama: command not found` | Abrí la app de Ollama una vez y después una terminal nueva. |
| `No encuentro Ollama en http://localhost:11434` | Ollama no está corriendo: abrí la app, o corré `ollama serve` en otra terminal. |
| `Ollama no tiene el modelo …` | `ollama pull` con el nombre exacto. `ollama ls` muestra los que tenés. |
| Muy lento (menos de 5 tokens por segundo) | Cerrá programas pesados (navegador, Teams). `ollama ps` muestra si usa GPU o CPU. |
| La computadora se tranca o el modelo se cierra | Falta memoria: cerrá otros programas o usá Codespaces. |
| PowerShell no deja activar el entorno | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` y probá de nuevo. |
| La descarga no avanza | Probá con otra conexión. Si tu red usa proxy, configurá `HTTPS_PROXY`. |
| Una celda del agente no termina | En Jupyter: *Kernel → Interrupt*. Ver la nota de abajo. |

## Antes de empezar, una advertencia

El agente ejecuta en tu computadora el código que escribe el modelo, con tus permisos y sin límite de
tiempo. Con estos datos y esta tarea el riesgo es bajo, pero no es una buena práctica: en la clase 2
le ponemos tiempo máximo y lo aislamos. Mientras tanto, no le des datos ni carpetas que no quieras exponer.

## Cuando termine el curso

`ollama rm qwen3.5:0.8b` libera el espacio del modelo. Para desinstalar Ollama: en macOS, borrá la app;
en Windows, *Configuración → Aplicaciones*.
