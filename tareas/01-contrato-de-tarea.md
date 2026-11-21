# Entrega 1 · Contrato de tarea y diagrama del agente

Para antes de la clase 2 · en equipos de 3 · 10% de la nota

La pregunta: **marketing quiere saber si la promoción funcionó y si conviene dársela a todos los
usuarios**, con los datos y las herramientas del [Agente Vainilla](../ejemplos/agente-vainilla/).

## Qué entregar

1. **El contrato de tarea**, en la plantilla
   [`ejemplos/agente-vainilla/contrato.md`](../ejemplos/agente-vainilla/contrato.md): pregunta, población y
   período, métrica, herramientas permitidas, límites y presupuesto, artefactos, inferencias permitidas,
   cuándo detenerse o escalar, criterios de aceptación y arquitectura.
2. **El diagrama del agente**: entradas, herramientas, ciclo, registros y salida. Marquen qué pasos hace el
   código y cuáles decide el modelo. Una foto del dibujo alcanza.

## Cómo se evalúa

- **Verificable:** cada sección se puede comprobar mirando el registro de una corrida (`runs/*.json`).
  "Que el análisis esté bien" no se puede comprobar; "cada número de la respuesta aparece en un resultado
  del registro", sí.
- **Completo:** cubre las diez piezas de la plantilla, incluidas las inferencias permitidas y cuándo
  detenerse.
- **Honesto con los datos:** no promete lo que los datos no pueden dar.
- **Arquitectura clara:** se distingue qué hace el código y qué decide el modelo.
