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
| 00–25 | El seminario | Por qué agentes, por qué ahora; el recorrido; cómo se evalúa; a quién seguir |
| 25–40 | Caso inicial | Un informe convincente producido por un agente. ¿Lo firmarías? |
| 40–60 | Anatomía de un agente | Modelo, herramienta, workflow y agente; el bucle y sus seis piezas |
| 60–80 | Agente Vainilla, en vivo | La instalación paso a paso y la primera corrida, con su registro |
| 80–100 | Desafíos | Ustedes eligen cómo hacerlo fallar; el mismo agente con un manual |
| 100–112 | Evidencia | Lo que el agente afirma frente a lo que ejecutó; una regla en el código |
| 112–120 | Cierre | El contrato de tarea y la tarea para la clase 2 |

## Después de la clase: tarea para la clase 2

1. **Instalá todo** siguiendo [`instalacion/`](../../instalacion/): el Agente Vainilla y el kit. Terminás
   cuando `python3 agent.py --check` y `python verificar.py --agente` dicen **Todo listo**. Mandale una
   captura de los dos al docente hasta dos días antes de la clase 2. ¿Tu computadora no puede?
   [Codespaces](../../instalacion/codespaces.md).
2. **Hacé el [desafío 1](../../tareas/desafios/desafio-01.md):** corré tu desafío según la inicial de tu
   apellido y entregá el registro de la corrida y tu crítica. Cuenta dentro del 20% de participación.
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
