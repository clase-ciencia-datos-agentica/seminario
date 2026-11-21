# Entregas y evaluación

| Clase | Entrega | Peso |
|---|---|---|
| 1 | [Contrato de tarea y diagrama del agente](01-contrato-de-tarea.md) | 10% |
| 2 | Herramientas con controles de integridad y leakage, consultas SQL, registro de llamadas del agente y manifiesto del entorno | 10% |
| 3 | Tablero de corridas repetidas con baseline, tasa de éxito, diagnósticos y tabla de sensibilidad | 10% |
| 4 | Protocolo de revisión con roles, condiciones de escalamiento, DAG, estimando, supuestos y decisión de uso o abstención | 10% |
| 5 | Informe final y defensa, con una respuesta individual breve | 40% |

Clase: 20%, con los [desafíos](desafios/) (uno por clase, individuales) y la participación en talleres y discusiones. Las entregas son en equipo, salvo la respuesta individual
de la clase 5. El docente indica en cada clase el canal y el plazo de entrega.

## El proyecto

Un agente para un caso de uso concreto, el mismo durante las cinco clases. Cada equipo conserva su agente
inicial y lo compara con su versión final usando el mismo modelo, datos, presupuesto y criterios. Las
corridas fallidas también se registran y se entregan. Cuando la evidencia no identifica un efecto,
abstenerse es un resultado correcto.

## Condiciones de aceptación

Un resultado inventado, una fuga del conjunto reservado o una afirmación causal sin identificación
obliga a corregir esa parte antes de aceptar el trabajo. Una puntuación alta en otras dimensiones no
compensa esa falla. Se evalúa la calidad del juicio y de la evidencia, además del rendimiento numérico.

## Rúbrica del informe final

| Dimensión | Puntos | Evidencia esperada |
|---|---|---|
| Diseño del agente | 25 | Contrato de tarea, arquitectura, herramientas con controles, límites y trazas completas |
| Evaluación y confiabilidad | 25 | Casos reservados, corridas repetidas, fallas por categoría, costo registrado y comparación con el agente inicial |
| Supervisión y seguridad | 10 | Condiciones de escalamiento, defensa ante instrucciones en los datos y abstención cuando corresponde |
| Validez de datos y estadística | 20 | Población, joins, fechas, denominadores y leakage comprobados; incertidumbre interpretada correctamente |
| Validez causal | 10 | Estimando y supuestos explícitos; identificación defendida o abstención justificada |
| Comunicación y revisión | 10 | Afirmaciones apoyadas por evidencia; límites y decisión de uso claros |
