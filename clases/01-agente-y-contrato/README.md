# Clase 1 · De un prompt a un agente auditable

> ¿Qué evidencia necesitamos para confiar en un resultado?

**Al terminar vas a poder:** distinguir modelo, herramienta, workflow y agente; describir el bucle de un
agente (estado, herramientas, observaciones, presupuesto y condición de parada); escribir un caso de uso
como contrato de tarea; reconocer que una explicación convincente no demuestra que un resultado sea
correcto.

## Antes de la clase

Instalá el Agente Vainilla y comprobá que `python3 agent.py --check` termine en **Todo listo**:
[guía de instalación](../../ejemplos/agente-vainilla/LEEME.md), unos 20 minutos. Si tu computadora no
alcanza, usá [Codespaces](../../instalacion/codespaces.md) o trabajá en pareja.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Caso inicial | Un informe convincente producido por un agente. ¿Lo firmarías? |
| 15–40 | Anatomía de un agente | Modelo, herramienta, workflow y agente; el bucle y sus seis piezas |
| 40–60 | Agente Vainilla, en vivo | Primer prompt y primera corrida, con su registro |
| 60–95 | Contrato de tarea | Qué le encargamos al agente, por escrito; y el mismo agente con un manual |
| 95–110 | Evidencia | Lo que el agente afirma frente a lo que ejecutó; una regla en el código |
| 110–120 | Comprobación | Clasificar fallas y defender una condición de aceptación |

## En clase

En la carpeta `ejemplos/agente-vainilla` (en Windows, `py` en lugar de `python3`):

```bash
python3 agent.py --check          # Ollama y el modelo, listos
python3 agent.py                  # modo básico
python3 agent.py --mode informed  # el mismo modelo, con el manual del curso
```

## Entrega

[Contrato de tarea y diagrama del agente](../../tareas/01-contrato-de-tarea.md), en equipos de 3.

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
