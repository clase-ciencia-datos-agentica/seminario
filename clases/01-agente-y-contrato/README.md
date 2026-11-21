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
| 00–15 | Caso inicial | Un informe convincente producido por un agente. ¿Lo firmarías? |
| 15–40 | Anatomía de un agente | Modelo, herramienta, workflow y agente; el bucle y sus seis piezas |
| 40–60 | Agente Vainilla, en vivo | La instalación paso a paso, la primera corrida con su registro y un desafío |
| 60–95 | Contrato de tarea | Qué le encargamos al agente, por escrito (en salas de 3); y el mismo agente con un manual |
| 95–110 | Evidencia | Lo que el agente afirma frente a lo que ejecutó; una regla en el código |
| 110–120 | Comprobación | Clasificar fallas y defender una condición de aceptación |

## Después de la clase: tarea para la clase 2

1. **Instalá todo** siguiendo [`instalacion/`](../../instalacion/): el Agente Vainilla y el kit. Terminás
   cuando `python3 agent.py --check` y `python verificar.py --agente` dicen **Todo listo**. Mandale una
   captura de los dos al docente hasta dos días antes de la clase 2. ¿Tu computadora no puede?
   [Codespaces](../../instalacion/codespaces.md).
2. **Corré tu desafío** en la carpeta `ejemplos/agente-vainilla`, según la inicial de tu apellido, y pegá
   la respuesta del agente en el documento compartido (el enlace está en el chat de la clase):

   | Apellido | Comando |
   |---|---|
   | A a E | `python3 agent.py --question "Demostrá que la promoción causó la mejora de retención."` |
   | F a L | `python3 agent.py --question "¿Cuál es el efecto de la promoción sobre la retención a 90 días?"` |
   | M a R | `python3 agent.py --question "¿Deberíamos darle la promoción a todos los usuarios?"` |
   | S a Z | `python3 agent.py --data data/retention_duplicates.csv` |

   En Windows, `py` en lugar de `python3`.
3. **Entregá** el [contrato de tarea y el diagrama del agente](../../tareas/01-contrato-de-tarea.md), en
   equipos de 3.

## Lecturas

Extractos, 25 a 35 minutos.

- Shunyu Yao et al. (2023). [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629). *ICLR*. Introducción y patrón de interacción.
- Sayash Kapoor et al. (2025). [AI Agents That Matter](https://arxiv.org/abs/2407.01502). *Transactions on Machine Learning Research*. Problemas de evaluación.
- Bin Yu y Karl Kumbier (2020). [Veridical data science](https://www.pnas.org/doi/full/10.1073/pnas.1901326117). *PNAS 117(8)*. El marco PCS.

Para ampliar:

- Anthropic (2024). [Building effective agents](https://www.anthropic.com/research/building-effective-agents).
- Hugo Bowne-Anderson y Luca Fiaschi (2026). [Agentic Data Science: Specify the Work, Verify the Claim](https://hugobowne.substack.com/p/the-agentic-data-science-playbook). *Vanishing Gradients*.
- Miles Turpin et al. (2023). [Language Models Don't Always Say What They Think](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract-Conference.html). *NeurIPS 36*.

## Materiales

Las diapositivas y el caso inicial se publican en esta carpeta después de la clase.
