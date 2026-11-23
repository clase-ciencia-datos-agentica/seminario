# Clase 1 · De un prompt a un agente auditable

> ¿Qué evidencia necesitamos para confiar en un resultado?

**Al terminar vas a poder:** distinguir modelo, herramienta, workflow y agente; describir el bucle de un
agente (estado, herramientas, observaciones, presupuesto y condición de parada); escribir un caso de uso
como contrato de tarea; reconocer que una explicación convincente no demuestra que un resultado sea
correcto.

## Antes de la clase

Nada que instalar: en esta clase el docente maneja el agente en su pantalla. Tené el chat a mano: lo
usamos para votar, predecir y desafiar al agente.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Bienvenida | Presentaciones y expectativas; cómo trabajamos, las cinco clases, la evaluación y este repositorio |
| 15–27 | Caso inicial | Un informe convincente sobre una promoción. ¿Lo firmarías? |
| 27–47 | Anatomía del agente | Chat, workflow y agente: ¿quién decide el próximo paso? El bucle y sus piezas |
| 47–65 | Demostración guiada | Una corrida del agente y su registro. **Desafío 1**, en el chat |
| 65–97 | Contrato de tarea | Un manual, una regla en el código y un taller para escribir el contrato, en equipos de 3 |
| 97–110 | Discusión de evidencia | Lo que el agente afirmó frente a lo que ejecutó |
| 110–120 | Comprobación de aprendizaje | Clasificar fallas, defender una condición de aceptación, y la entrega 1 |

## En clase

- **[Desafío 1](../../tareas/desafios/desafio-01.md):** individual, en el chat, durante la primera corrida.
- **Taller del contrato:** en equipos de 3, con la [plantilla](plantilla-contrato.md). Es práctica: no se
  entrega.

## Entrega 1 · para la clase 2

[Instalar y leer](../../tareas/01-instalar-y-leer.md): instalar el modelo, hacerle una pregunta y leer un
extracto. Individual, una hora, hasta la noche anterior a la clase 2.

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
