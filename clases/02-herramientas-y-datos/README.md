# Clase 2 · Herramientas, datos y límites del agente

> ¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien?

**Al terminar vas a poder:** diseñar herramientas de consulta y cálculo con controles incorporados;
detectar joins incorrectos y leakage desde las herramientas; limitar lo que el agente puede ejecutar;
tratar las instrucciones dentro de los datos como contenido no autorizado.

## Antes de la clase

La [entrega 1](../../tareas/01-instalar-y-leer.md) y el desafío 1: Ollama, el modelo y una pregunta, con la captura
de la respuesta, y una lectura. Para la clase no hace falta instalar nada más: las demos van en la pantalla del docente.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Auditoría de una herramienta | Un informe que pasa la auditoría de la clase 1 y está mal: una métrica inflada por un join que duplica observaciones |
| 15–30 | Herramientas con contrato | Claves, unidades de análisis, denominadores, ventanas temporales y procedencia, comprobadas en cada llamada |
| 30–45 | Leakage y acceso | La información disponible al momento de decidir frente a la información futura; los datos de evaluación, fuera del alcance del agente |
| 45–100 | Taller y límites | Las dos versiones de las herramientas, en vivo: el agente con cada una, el registro de cada llamada, el tiempo máximo, el acceso a archivos y una instrucción maliciosa dentro de los datos |
| 100–120 | Comprobación | Por qué una herramienta que se ejecuta sin errores puede devolver una métrica incorrecta |

**Ejercicio central:** corregir la herramienta que une campañas y pedidos, retirar una variable medida
después del resultado y demostrar que las métricas del agente cambian. Un compañero tiene que poder
reproducir la ejecución a partir de la traza.

## Entrega

[Repetir la demo y leer](../../tareas/02-repetir-la-demo-y-leer.md): instalar DuckDB, repetir en tu
computadora los pasos de la demo, en el mismo orden, y leer un extracto de una de las lecturas. Mandás una
captura del último paso y una línea sobre la lectura. Individual, una hora, antes de la clase 3, por el portal UM.

## Lecturas

Para la entrega 2, elegí una y leé el extracto indicado (25 a 35 minutos).

- Sayash Kapoor y Arvind Narayanan (2023). [Leakage and the reproducibility crisis in machine-learning-based science](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/). *Patterns 4*. Introducción y la taxonomía de leakage.
- Greg Wilson et al. (2017). [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1005510). *PLOS Computational Biology 13(6)*. Introducción y las secciones sobre manejo de datos y organización del proyecto.
- Timnit Gebru et al. (2021). [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/). *Communications of the ACM 64(12)*. Introducción y las preguntas sobre motivación, composición y recolección.

Para ampliar:

- Chip Huyen (2025). [Agents](https://huyenchip.com/2025/01/07/agents.html).
- Edoardo Debenedetti et al. (2024). [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://agentdojo.spylab.ai/). *NeurIPS Datasets and Benchmarks*.
- Fangyu Lei et al. (2025). [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html). *ICLR*.
- Anthropic (2024). [Building effective agents](https://www.anthropic.com/research/building-effective-agents).

## Materiales

- **Las diapositivas:** [en PDF](diapositivas.pdf), para leerlas acá mismo, o [en HTML](diapositivas.html),
  para bajarlas (botón *Download raw file*) y abrirlas en el navegador.
- **El caso inicial:** [el informe](caso-inicial/informe.md) que auditamos en clase y
  [su registro](caso-inicial/registro.json), con la consulta de cada herramienta.
- **El Agente Vainilla SQL**, el de la demostración: [`ejemplos/agente-vainilla-sql`](../../ejemplos/agente-vainilla-sql/).
  Instalarlo y repetir la demo es la [entrega 2](../../tareas/02-repetir-la-demo-y-leer.md); las instrucciones están en su
  [LEEME](../../ejemplos/agente-vainilla-sql/LEEME.md).
