# Clase 4 · Supervisión humana y afirmaciones causales

> ¿La recomendación corresponde a un efecto identificado?

**Al terminar vas a poder:** definir los roles de principal, actor y crítico; establecer cuándo el agente
debe escalar a una persona; definir un estimando causal y usar un DAG como artefacto de revisión;
reconocer cuándo la respuesta correcta es abstenerse.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Caso de Simpson y selección | Cómo cambia una asociación agregada al distinguir grupos; explicaciones alternativas |
| 15–40 | Diseño antes de estimación | Tratamiento, resultado, población y tiempo cero; un DAG; intercambiabilidad y positividad |
| 40–60 | Roles y escalamiento | Responsabilidades del principal, el actor y el crítico; en código, las condiciones que obligan al agente a pedir revisión |
| 60–95 | Taller de crítica causal | Revisar una recomendación del agente junto con su traza: selección de controles, balance, sensibilidad y diagnósticos |
| 95–110 | Abstención | Formular una respuesta de no identificación y decidir qué dato o diseño haría falta para responder |
| 110–120 | Comprobación | Defender por qué el diseño permite o no la afirmación causal pedida |

**Ejercicio central:** con datos simulados de una intervención con confusión conocida, el agente propone
una recomendación; el equipo, en el rol de crítico, la revisa con el DAG y prepara un caso donde la
respuesta correcta sea abstenerse.

## Entrega

Protocolo de revisión con roles, condiciones de escalamiento, DAG, estimando, supuestos y decisión de uso
o abstención. Ajustar muchas variables, obtener buen balance o pasar un placebo no se presenta como prueba
de ausencia de confusión no observada.

## Lecturas

- Miguel A. Hernán y James M. Robins (2020). [Causal Inference: What If](https://miguelhernan.org/whatifbook). *Chapman & Hall/CRC*. Una selección de la Parte I.
- Amit Sharma y Emre Kiciman (2020). [DoWhy: An End-to-End Library for Causal Inference](https://arxiv.org/abs/2011.04216). *arXiv*. Las cuatro etapas.
- Matej Zečević et al. (2023). [Causal Parrots: Large Language Models May Talk Causality But Are Not Causal](https://arxiv.org/abs/2308.13067). *Transactions on Machine Learning Research*. Hablar de causalidad no es razonar causalmente.

Para ampliar:

- Winston Chou et al. (2026). [A Human-Augmenting Agentic Workflow for Causal Inference](https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af). *Netflix TechBlog*.
- Nick Huntington-Klein (2025). [The Effect: An Introduction to Research Design and Causality](https://theeffectbook.net/). *Chapman & Hall/CRC*.
- Emre Kıcıman et al. (2024). [Causal Reasoning and Large Language Models: Opening a New Frontier for Causality](https://arxiv.org/abs/2305.00050). *Transactions on Machine Learning Research*.
- Andrej Leban et al. (2026). [CausalDS: Benchmarking Causal Reasoning in Data-Science Agents](https://arxiv.org/abs/2607.08093). *arXiv*.

## Materiales

Se publican en esta carpeta.
