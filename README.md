# Ciencia de Datos Agéntica y Defendible

Seminario · Universidad de Montevideo · Juan Franceschini

Construimos, evaluamos y supervisamos un agente de IA que analiza datos, y aprendemos a decidir cuándo
confiar en lo que devuelve. El eje es la confiabilidad: resultados cuya medición, código, supuestos,
incertidumbre y evidencia otra persona pueda revisar. Todo corre gratis, con modelos abiertos en tu
computadora.

## Clases

| | Clase | Pregunta | Para trabajar |
|---|---|---|---|
| 01 | [De un prompt a un agente auditable](clases/01-agente-y-contrato/) | ¿Qué evidencia necesitamos para confiar en un resultado? | [Agente Vainilla](ejemplos/agente-vainilla/) · [entrega 1](tareas/01-contrato-de-tarea.md) |
| 02 | [Herramientas, datos y límites del agente](clases/02-herramientas-y-datos/) | ¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien? | [kit](kit/) |
| 03 | [Confiabilidad entre corridas](clases/03-confiabilidad/) | ¿El agente llega a la misma conclusión si lo ejecutamos de nuevo? | [kit](kit/) |
| 04 | [Supervisión humana y afirmaciones causales](clases/04-supervision-y-causalidad/) | ¿La recomendación corresponde a un efecto identificado? | [kit](kit/) |
| 05 | [Evaluar y defender un agente confiable](clases/05-evaluacion-y-defensa/) | ¿El sistema resiste una evaluación independiente? | [kit](kit/) |

Las diapositivas de cada clase se publican en su carpeta después de la clase.

## Antes de la clase 1

1. Instalá el Agente Vainilla siguiendo [su guía](ejemplos/agente-vainilla/LEEME.md): Ollama, un modelo
   abierto y Python. Unos 20 minutos, casi todos esperando la descarga.
2. Comprobá que `python3 agent.py --check` termine en **Todo listo**.
3. ¿Tu computadora no alcanza? Usalo sin instalar nada, en el navegador: [Codespaces](instalacion/codespaces.md).

## Qué hay en este repositorio

| Carpeta | Contenido |
|---|---|
| [`programa/`](programa/) | El programa del seminario |
| [`clases/`](clases/) | Una carpeta por clase: pregunta, objetivos, agenda, lecturas y, después de la clase, las diapositivas |
| [`ejemplos/`](ejemplos/) | Código y datos que corremos en clase. `agente-vainilla/` es el agente de la clase 1 |
| [`kit/`](kit/) | El kit de las clases 2 a 5: el agente que escribe su propio código, los notebooks y los datos |
| [`tareas/`](tareas/) | Las entregas, sus plantillas y cómo se evalúan |
| [`instalacion/`](instalacion/) | Qué instalar para cada clase, y la opción sin instalar nada |
| [`referencias/`](referencias/) | Las lecturas, con enlaces a su fuente |

## Cómo usarlo

- **Descargar:** botón verde *Code* → *Download ZIP*. Con git: `git clone` y la dirección de este repositorio.
- **Actualizar:** antes de cada clase, `git pull` (o volvé a descargar el ZIP). Si cambiaste archivos del
  repositorio, guardá tu trabajo en otra carpeta antes de actualizar.
- **Sin instalar nada:** *Code* → *Codespaces* → *Create codespace on main*. Ver [instalacion/codespaces.md](instalacion/codespaces.md).

## Evaluación

Entregas de las clases 1 a 4 (10% cada una), participación en talleres y discusiones (20%) e informe y
defensa final en la clase 5 (40%). Detalle, rúbrica y condiciones de aceptación en [`tareas/`](tareas/).

## Créditos

Las diapositivas usan imágenes e ideas de Pepe Alonso, *From Zero to AI Agents* (Berkeley Haas), con su
permiso. El modelo de las clases es Qwen3.5 (Alibaba, licencia Apache 2.0), servido con
[Ollama](https://ollama.com). Los datos del Agente Vainilla son sintéticos; los del kit vienen de un
programa de empleo y están disfrazados para el curso.
