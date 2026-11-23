# Clase 2 · Herramientas, datos y límites del agente

> ¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien?

**Al terminar vas a poder:** diseñar herramientas de consulta y cálculo con controles incorporados;
detectar joins incorrectos y leakage desde las herramientas; limitar lo que el agente puede ejecutar;
tratar las instrucciones dentro de los datos como contenido no autorizado.

## Antes de la clase

La [entrega 1](../../tareas/01-instalar-y-leer.md): Ollama, el modelo y una pregunta, con la captura de la respuesta,
y una lectura. Lo demás que haga falta instalar se publica acá antes de la
clase.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Auditoría de una herramienta | Detectar una métrica inflada por un join que duplica observaciones en la consulta que ejecutó el agente |
| 15–40 | Herramientas con contrato | Entradas, salidas y comprobaciones de cada herramienta: claves, unidades de análisis, denominadores, ventanas temporales y procedencia |
| 40–60 | Leakage y acceso | La información disponible al momento de decidir frente a la información futura; los datos de evaluación, fuera del alcance del agente |
| 60–95 | Taller de herramientas | Herramientas en Python y SQL con aserciones sobre filas, claves y fechas; registrar cada llamada y su resultado |
| 95–110 | Límites y seguridad | Ejecutar el código del agente con tiempo máximo y en un espacio aislado; probar una instrucción maliciosa dentro de los datos |
| 110–120 | Comprobación | Por qué una herramienta que se ejecuta sin errores puede devolver una métrica incorrecta |

**Ejercicio central:** corregir la herramienta que une campañas y pedidos, retirar una variable medida
después del resultado y demostrar que las métricas del agente cambian. Un compañero tiene que poder
reproducir la ejecución a partir de la traza.

## Entrega

Corta, en equipos de 3, sobre las herramientas del agente. Se publica con la clase.

## Lecturas

- Sayash Kapoor y Arvind Narayanan (2023). [Leakage and the reproducibility crisis in machine-learning-based science](https://pmc.ncbi.nlm.nih.gov/articles/PMC10499856/). *Patterns 4*. La taxonomía de leakage.
- Greg Wilson et al. (2017). [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1005510). *PLOS Computational Biology 13(6)*. Organización y reproducción.
- Timnit Gebru et al. (2021). [Datasheets for Datasets](https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/). *Communications of the ACM 64(12)*. Preguntas sobre origen y uso.

Para ampliar:

- Chip Huyen (2025). [Agents](https://huyenchip.com/2025/01/07/agents.html).
- Edoardo Debenedetti et al. (2024). [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://agentdojo.spylab.ai/). *NeurIPS Datasets and Benchmarks*.
- Fangyu Lei et al. (2025). [Spider 2.0: Evaluating Language Models on Real-World Enterprise Text-to-SQL Workflows](https://proceedings.iclr.cc/paper_files/paper/2025/hash/46c10f6c8ea5aa6f267bcdabcb123f97-Abstract-Conference.html). *ICLR*.
- Anthropic (2024). [Building effective agents](https://www.anthropic.com/research/building-effective-agents).

## Materiales

Se publican en esta carpeta.
