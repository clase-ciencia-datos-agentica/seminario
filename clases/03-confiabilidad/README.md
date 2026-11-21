# Clase 3 · Confiabilidad entre corridas

> ¿El agente llega a la misma conclusión si lo ejecutamos de nuevo?

**Al terminar vas a poder:** medir la variabilidad del agente con corridas repetidas; separar
incertidumbre de muestreo, variabilidad del agente y sensibilidad a decisiones analíticas; reportar el
conjunto de resultados en lugar de elegir la mejor corrida.

## Agenda

| Minutos | Bloque | Qué hacemos |
|---|---|---|
| 00–15 | Variación entre analistas | Comparar dos respuestas del agente al mismo problema y localizar las decisiones que difieren |
| 15–40 | Corridas repetidas | Ejecutar el agente varias veces con el mismo presupuesto; medir la tasa de éxito y la consistencia entre corridas |
| 40–60 | Workflow estadístico | Validación fuera de muestra y diagnósticos con un modelo sencillo de referencia |
| 60–95 | Taller de sensibilidad | Variar decisiones declaradas (faltantes, especificación, instrucciones del agente) y registrar el conjunto de resultados |
| 95–110 | Interpretación | Explicación predictiva frente a efecto causal; elegir la mejor de varias corridas es seleccionar según el resultado |
| 110–120 | Comprobación | Redactar una conclusión con tamaño del efecto, incertidumbre, variabilidad del agente y límites |

**Ejercicio central:** ejecutar el agente varias veces y cambiar decisiones defendibles declaradas de
antemano, como el manejo de faltantes o la especificación del modelo. Explicar si la conclusión es
estable y qué incertidumbre no está cuantificada.

## Entrega

Tablero de corridas repetidas con baseline, tasa de éxito, diagnósticos y tabla de sensibilidad; todas
las corridas quedan registradas. La dispersión entre ejecuciones no se presenta como intervalo de
confianza ni como probabilidad de que la conclusión sea verdadera.

## Lecturas

- Martin Bertran et al. (2026). [Many AI analysts, one dataset: Navigating the agentic data science multiverse](https://pmc.ncbi.nlm.nih.gov/articles/PMC13393493/). *PNAS 123(29)*. Diseño y dispersión analítica.
- Stephan Rabanser et al. (2026). [Towards a Science of AI Agent Reliability](https://proceedings.mlr.press/v306/rabanser26a.html). *ICML*. Dimensiones de confiabilidad.
- Andrew Gelman et al. (2020). [Bayesian Workflow](https://arxiv.org/abs/2011.01808). *arXiv*. Comprobación del modelo.

Para ampliar:

- Raphael Silberzahn et al. (2018). [Many Analysts, One Data Set](https://www.psychologicalscience.org/journals/ampps/2515245917747646/). *Advances in Methods and Practices in Psychological Science 1(3)*.
- Jonah Gabry et al. (2019). [Visualization in Bayesian Workflow](https://academic.oup.com/jrsssa/article/182/2/389/7070184). *Journal of the Royal Statistical Society Series A 182(2)*.
- Cynthia Rudin (2019). [Stop explaining black box machine learning models for high stakes decisions and use interpretable models instead](https://www.nature.com/articles/s42256-019-0048-x). *Nature Machine Intelligence 1*.
- Zachary T. Rewolinski et al. (2026). [Sanity Checks for Agentic Data Science](https://arxiv.org/abs/2604.11003). *arXiv*.

## Materiales

Se publican en esta carpeta.
