# Clase 5 · Evaluar y defender un agente confiable

> ¿El sistema resiste una evaluación independiente?

**Al terminar vas a poder:** diseñar una evaluación de tareas y fallas; comparar agentes bajo
presupuestos comunes; calibrar revisores automáticos; entregar un resultado defendible y reproducible.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Definir la evaluación | Separar tareas de desarrollo y de prueba; criterios, presupuesto y fallas críticas antes de ejecutar |
| 15–35 | Medir confiabilidad | Consistencia entre corridas, robustez a cambios, gravedad de errores, costo y abstención |
| 35–55 | Elegir y calibrar revisores | Pruebas determinísticas y revisión humana; un juez LLM contrastado con etiquetas expertas |
| 55–90 | Taller de evaluación final | El agente inicial y el mejorado sobre casos reservados; aciertos, fallas y artefactos |
| 90–110 | Defensa cruzada | Intercambiar informes entre equipos; auditar evidencia, reproducibilidad y una afirmación causal o estadística |
| 110–120 | Cierre y evaluación individual | Una falla restante, su consecuencia y la siguiente prueba o dato que hace falta |

**Ejercicio central:** comparar el agente inicial y el mejorado con el mismo modelo, datos y presupuesto.
El equipo revisor verifica al menos un cálculo y un supuesto; los fallos también se entregan.

## Entrega

El final: su propio caso de negocio, con sus datos, el agente reforzado con contexto y controles, y su
auditoría con el registro, como en la clase 1. Informe y defensa, con una respuesta individual breve.
Detalle y rúbrica en [`tareas/`](../../tareas/#el-final-tu-propio-caso-de-negocio).

## Lecturas

- Sayash Kapoor et al. (2025). [AI Agents That Matter](https://arxiv.org/abs/2407.01502). *Transactions on Machine Learning Research*. Evaluación y costos.
- Stephan Rabanser et al. (2026). [Towards a Science of AI Agent Reliability](https://proceedings.mlr.press/v306/rabanser26a.html). *ICML*. Dimensiones de confiabilidad.
- Lianmin Zheng et al. (2023). [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685). *NeurIPS Datasets and Benchmarks*. Límites de los jueces LLM.
- Inioluwa Deborah Raji et al. (2020). [Closing the AI Accountability Gap](https://arxiv.org/abs/2001.00973). *ACM FAT\**. Auditoría de punta a punta.

Para ampliar:

- Anthropic (2026). [Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents).
- Chip Huyen (2025). [Agents](https://huyenchip.com/2025/01/07/agents.html).
- Zana Buçinca et al. (2021). [To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making](https://doi.org/10.1145/3449287). *Proceedings of the ACM on Human-Computer Interaction 5*.
- Zachary T. Rewolinski et al. (2026). [Sanity Checks for Agentic Data Science](https://arxiv.org/abs/2604.11003). *arXiv*.

## Materiales

Se publican en esta carpeta.
