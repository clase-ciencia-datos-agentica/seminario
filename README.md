# Ciencia de Datos Agéntica y Defendible

Seminario · Universidad de Montevideo · cinco clases de dos horas · Juan Franceschini

Construimos, evaluamos y supervisamos un agente de IA que analiza datos, y aprendemos a decidir cuándo
confiar en lo que devuelve. Todo es gratis y corre en tu computadora.

## Empezá acá

1. **[Clase 2](clases/02-herramientas-y-datos/):** las diapositivas, el caso inicial y el agente de la
   demostración. Lo de la clase 1 sigue en [su carpeta](clases/01-agente-y-contrato/).
2. **[Para la clase 3](tareas/02-repetir-la-demo-y-leer.md):** instalar DuckDB, repetir los pasos de la
   demo de la clase 2 y leer un extracto (la entrega 2). Mandás una captura del último paso y una línea
   sobre la lectura. Una hora, individual, antes de la clase 3, por el portal UM.

## Las cinco clases

| | Clase | Pregunta | Entrega |
|---|---|---|---|
| 1 | [De un prompt a un agente auditable](clases/01-agente-y-contrato/) | ¿Qué evidencia necesitamos para confiar en un resultado? | Instalar y leer (individual) |
| 2 | [Herramientas, datos y límites del agente](clases/02-herramientas-y-datos/) | ¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien? | Instalar DuckDB, consultar y leer (individual) |
| 3 | [Confiabilidad entre corridas](clases/03-confiabilidad/) | ¿El agente llega a la misma conclusión si lo ejecutamos de nuevo? | Corta, sobre corridas repetidas |
| 4 | [Supervisión humana y afirmaciones causales](clases/04-supervision-y-causalidad/) | ¿La recomendación corresponde a un efecto identificado? | Corta, sobre una revisión |
| 5 | [Evaluar y defender un agente confiable](clases/05-evaluacion-y-defensa/) | ¿El sistema resiste una evaluación independiente? | El final: tu propio caso de negocio |

Las diapositivas y el código de cada clase se publican en su carpeta cuando hacen falta.

## Cómo se evalúa

| | Peso |
|---|---|
| Cuatro entregas cortas, de las clases 1 a 4 | 40% (10% cada una) |
| Participación en talleres y discusiones, con un desafío individual por clase | 20% |
| El final: tu propio caso de negocio, como el de la clase 1 pero con tus datos, tus controles y tu auditoría. Informe y defensa en la clase 5 | 40% |

Lo que queda para la casa no pasa de un par de horas por clase. Detalle y rúbrica en [`tareas/`](tareas/).

## Qué hay en este repositorio

| Carpeta | Qué encontrás |
|---|---|
| [`clases/`](clases/) | Una página por clase: agenda, tarea y lecturas |
| [`tareas/`](tareas/) | Las entregas, los desafíos, el final y la rúbrica |
| [`instalacion/`](instalacion/) | Qué instalar, y la opción sin instalar nada |
| [`referencias/`](referencias/) | Las lecturas, con enlace a su fuente |

## Créditos

Algunas ideas de las clases vienen de Pepe Alonso, *From Zero to AI Agents* (Berkeley Haas), con su
permiso. El modelo es Qwen3.5 (Alibaba, licencia Apache 2.0), servido con [Ollama](https://ollama.com).
Las consultas corren en [DuckDB](https://duckdb.org) (licencia MIT). Los datos de las clases son sintéticos.
