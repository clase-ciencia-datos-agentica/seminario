# Ciencia de Datos Agéntica y Defendible

Seminario · Universidad de Montevideo · cinco clases de dos horas · Juan Franceschini

Construimos, evaluamos y supervisamos un agente de IA que analiza datos, y aprendemos a decidir cuándo
confiar en lo que devuelve. Todo es gratis y corre en tu computadora.

## Empezá acá

1. **[Clase 1](clases/01-agente-y-contrato/):** qué hacemos en clase y la tarea para la clase 2. Para la
   clase 1 no hace falta instalar ni descargar nada.
2. **[La tarea para la clase 2](clases/01-agente-y-contrato/#tarea-para-la-clase-2--unos-30-minutos):**
   instalar un modelo y hacerle una pregunta. Unos 30 minutos.

## Las cinco clases

| | Clase | Pregunta | Entrega (en equipos de 3) |
|---|---|---|---|
| 1 | [De un prompt a un agente auditable](clases/01-agente-y-contrato/) | ¿Qué evidencia necesitamos para confiar en un resultado? | Contrato de tarea y diagrama del agente |
| 2 | [Herramientas, datos y límites del agente](clases/02-herramientas-y-datos/) | ¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien? | Herramientas con controles y trazas |
| 3 | [Confiabilidad entre corridas](clases/03-confiabilidad/) | ¿El agente llega a la misma conclusión si lo ejecutamos de nuevo? | Corridas repetidas y sensibilidad |
| 4 | [Supervisión humana y afirmaciones causales](clases/04-supervision-y-causalidad/) | ¿La recomendación corresponde a un efecto identificado? | Protocolo de revisión y abstención |
| 5 | [Evaluar y defender un agente confiable](clases/05-evaluacion-y-defensa/) | ¿El sistema resiste una evaluación independiente? | Informe y defensa final |

Las diapositivas y el código de cada clase se publican en su carpeta cuando hacen falta.

## Cómo se evalúa

| | Peso |
|---|---|
| Entregas de las clases 1 a 4, en equipos de 3, hechas en clase | 40% (10% cada una) |
| Participación en talleres y discusiones, con un desafío individual por clase | 20% |
| Informe y defensa final en la clase 5, con una respuesta individual | 40% |

Lo que queda para la casa no pasa de un par de horas por clase. Detalle y rúbrica en [`tareas/`](tareas/).

## Qué hay en este repositorio

| Carpeta | Qué encontrás |
|---|---|
| [`clases/`](clases/) | Una página por clase: agenda, tarea y lecturas |
| [`tareas/`](tareas/) | Las entregas, la plantilla del contrato, los desafíos y la rúbrica |
| [`instalacion/`](instalacion/) | Qué instalar, y la opción sin instalar nada |
| [`referencias/`](referencias/) | Las lecturas, con enlace a su fuente |
| [`programa/`](programa/) | El programa del seminario |

## Créditos

Algunas ideas de las clases vienen de Pepe Alonso, *From Zero to AI Agents* (Berkeley Haas), con su
permiso. El modelo es Qwen3.5 (Alibaba, licencia Apache 2.0), servido con [Ollama](https://ollama.com).
Los datos de la clase 1 son sintéticos.
