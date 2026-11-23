# Clase 1 · De un prompt a un agente auditable

> ¿Qué evidencia necesitamos para confiar en un resultado?

**Al terminar vas a poder:** distinguir modelo, herramienta, workflow y agente; describir el bucle de un
agente (estado, herramientas, observaciones, presupuesto y condición de parada); usar el registro para comprobar qué calculó el agente y distinguir una comparación
descriptiva de una afirmación causal.

## Antes de la clase

Nada que instalar: en esta clase el docente maneja el agente en su pantalla. Tené el chat a mano para
comentar o preguntar.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Bienvenida | Presentaciones y expectativas; cómo trabajamos, las cinco clases, la evaluación y este repositorio |
| 15–27 | Caso inicial | Un resultado convincente sobre una promoción. ¿Lo firmarías? |
| 27–47 | Anatomía del agente | Chat, workflow y agente: ¿quién decide el próximo paso? Un turno, el bucle y el registro |
| 47–82 | Demostración guiada | Las opciones del agente y cinco corridas, en la pantalla del docente: básica, su registro, sin modelo, con un manual y con controles |
| 82–105 | Discusión de evidencia | Lo que vimos, y el informe del caso auditado con su registro |
| 105–120 | Comprobación de aprendizaje | Qué le podemos decir a Marketing, lo que sigue y preguntas |

## Para la clase 2

[Instalar, preguntar y leer](../../tareas/01-instalar-y-leer.md): instalar el modelo, hacerle una pregunta y
mandar la captura (el [desafío 1](../../tareas/desafios/desafio-01.md)), y leer un extracto (con la
instalación, la entrega 1). Individual, una hora, hasta la noche anterior a la clase 2.

Para tu proyecto final vas a escribir un contrato de tarea: esta es la [plantilla](plantilla-contrato.md).

## Lecturas

Para la entrega 1, elegí una y leé el extracto indicado (25 a 35 minutos).

- Shunyu Yao et al. (2023). [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629). *ICLR*. Introducción y patrón de interacción.
- Sayash Kapoor et al. (2025). [AI Agents That Matter](https://arxiv.org/abs/2407.01502). *Transactions on Machine Learning Research*. Problemas de evaluación.
- Bin Yu y Karl Kumbier (2020). [Veridical data science](https://www.pnas.org/doi/full/10.1073/pnas.1901326117). *PNAS 117(8)*. El marco PCS.

Para ampliar, opcionales:

- Anthropic (2024). [Building effective agents](https://www.anthropic.com/research/building-effective-agents).
- Hugo Bowne-Anderson y Luca Fiaschi (2026). [Agentic Data Science: Specify the Work, Verify the Claim](https://hugobowne.substack.com/p/the-agentic-data-science-playbook). *Vanishing Gradients*.
- Miles Turpin et al. (2023). [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html). *NeurIPS 36*.

## Materiales

Las diapositivas, el caso inicial y el código del agente se publican en esta carpeta después de la clase.
