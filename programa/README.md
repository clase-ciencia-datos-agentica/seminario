# Programa del seminario

Seminario · 5 clases de 120 minutos · 10 horas de trabajo en clase

El seminario trata sobre agentes de inteligencia artificial aplicados a un caso de uso concreto: el análisis de datos para tomar decisiones. Los estudiantes construyen, evalúan y supervisan un agente de análisis con Python y SQL. Cerca del 60% del trabajo se dedica al agente (arquitectura, herramientas, trazas, evaluación y supervisión) y el 40% a lo que el caso de uso exige para aceptar un resultado: datos correctos y conclusiones estadística y causalmente defendibles. El eje es la confiabilidad: resultados cuya medición, código, supuestos, incertidumbre y evidencia puedan revisarse.

**Contexto académico:** estudiantes avanzados de Ciencia de Datos y aplicaciones de IA, en el contexto de Universidad de Montevideo. Se presupone manejo introductorio de Python, SQL, probabilidad y regresión. No se requiere experiencia previa en agentes ni inferencia bayesiana computacional.

## Resultados de aprendizaje

- Diseñar un agente de análisis con contrato de tarea, herramientas, límites, registros de ejecución y criterios de aceptación.

- Equipar al agente con herramientas que verifican datos, consultas y cálculos, y protegerlo de instrucciones maliciosas dentro de los datos.

- Evaluar agentes con tareas reservadas, corridas repetidas, presupuestos comunes y revisores calibrados.

- Supervisar las conclusiones del agente: detectar afirmaciones que exceden la evidencia estadística o causal y defender su uso, sus límites o una abstención justificada.

## Recorrido del seminario

| **Clase** | **Foco**                     | **Producto acumulativo**            |
|:---------:|:-----------------------------|:------------------------------------|
|     1     | Agente y contrato de tarea   | Contrato de tarea y arquitectura    |
|     2     | Herramientas y datos         | Herramientas con controles y trazas |
|     3     | Confiabilidad entre corridas | Corridas repetidas y sensibilidad   |
|     4     | Supervisión y causalidad     | Protocolo de revisión y abstención  |
|     5     | Evaluación independiente     | Informe y defensa final             |

La enseñanza combina explicación conceptual, demostraciones y talleres guiados. Cada agenda suma exactamente 120 minutos. Las lecturas sugeridas son preparación opcional fuera de esas diez horas; las ideas necesarias se enseñan en clase.

CLASE 1 \| 120 MINUTOS

# De un prompt a un agente auditable

¿Qué evidencia necesitamos para confiar en un resultado?

**Al finalizar:** Distinguir modelo, herramienta, workflow y agente; describir el bucle del agente (estado, herramientas, observaciones, presupuesto y condición de parada); especificar el caso de uso como un contrato de tarea; reconocer que una explicación convincente no demuestra corrección.

| **Minutos** | **Actividad** | **Contenido y aplicación** |
|:--:|:---|:---|
| 00–15 | Caso inicial | Revisar un informe convincente producido por un agente, con errores sembrados, y formular criterios de aceptación. |
| 15–40 | Anatomía del agente | Explicar estado, herramientas, observaciones, control del bucle, presupuesto y condición de parada; comparar un workflow fijo con un agente. |
| 40–60 | Demostración guiada | Seguir una ejecución que consulta datos y ejecuta Python; leer la traza como registro de lo que el agente hizo. |
| 60–95 | Contrato de tarea | Escribir el contrato del caso de uso: pregunta, población, período, métrica, herramientas permitidas, límites, artefactos y cuándo detenerse o escalar. |
| 95–110 | Discusión de evidencia | Separar lo que el agente afirma de lo que ejecutó; distinguir corrección, trazabilidad, estabilidad y utilidad para la decisión. |
| 110–120 | Comprobación de aprendizaje | Clasificar fallas y defender una condición de aceptación verificable. |

**Ejercicio central:** El agente debe responder una pregunta de retención. El grupo escribe el contrato de tarea, dibuja la arquitectura marcando qué pasos resuelve el código y cuáles el modelo, y define qué inferencias están permitidas y qué hallazgo obliga a detenerse o pedir ayuda.

**Entrega:** Contrato de tarea y diagrama del agente con entradas, herramientas permitidas, límites, registros y criterios de aceptación.

**Criterio de aprendizaje:** El estudiante identifica al menos dos afirmaciones que no pueden aceptarse solo porque el agente las explica con claridad.

## Referencias académicas

Yao et al. (2023) \[A01\]; Kapoor et al. (2025) \[E01\]; Yu y Kumbier (2020) \[S03\].

ReAct: introducción y patrón de interacción. AI Agents That Matter: problemas de evaluación. Veridical data science: marco PCS. Extractos sugeridos, 25–35 minutos.

**Ampliación y material práctico:** Anthropic (2024) \[R01\]; Bowne-Anderson y Fiaschi (2026) \[R05\]; Turpin et al. (2023) \[X06\].

CLASE 2 \| 120 MINUTOS

# Herramientas, datos y límites del agente

¿Qué puede hacer el agente con los datos y cómo sabemos que lo hizo bien?

**Al finalizar:** Diseñar herramientas de consulta y cálculo con controles incorporados; detectar joins incorrectos y leakage desde las herramientas; limitar lo que el agente puede ejecutar; tratar las instrucciones dentro de los datos como contenido no autorizado.

| **Minutos** | **Actividad** | **Contenido y aplicación** |
|:--:|:---|:---|
| 00–15 | Auditoría de una herramienta | Detectar una métrica inflada por un join que duplica observaciones en la consulta que ejecutó el agente. |
| 15–40 | Herramientas con contrato | Definir entradas, salidas y comprobaciones de cada herramienta: claves, unidades de análisis, denominadores, ventanas temporales y procedencia. |
| 40–60 | Leakage y acceso | Distinguir la información disponible al momento de decidir de la información futura; dejar los datos de evaluación fuera del alcance del agente. |
| 60–95 | Taller de herramientas | Implementar herramientas en Python y SQL con aserciones sobre filas, claves y fechas; registrar cada llamada y su resultado. |
| 95–110 | Límites y seguridad | Ejecutar el código del agente con tiempo máximo y en un espacio aislado; probar una instrucción maliciosa dentro de los datos. |
| 110–120 | Comprobación de aprendizaje | Explicar por qué una herramienta que se ejecuta sin errores puede devolver una métrica incorrecta. |

**Ejercicio central:** Corregir la herramienta que une campañas y pedidos, retirar una variable medida después del resultado y demostrar que las métricas del agente cambian. Un compañero debe poder reproducir la ejecución a partir de la traza.

**Entrega:** Herramientas con controles de integridad y leakage, consultas SQL, registro de llamadas del agente y manifiesto del entorno.

**Criterio de aprendizaje:** Las pruebas deben fallar ante los errores sembrados y pasar tras corregirlos; ejecutar sin errores no basta.

## Referencias académicas

Kapoor y Narayanan (2023) \[S01\]; Wilson et al. (2017) \[S08\]; Gebru et al. (2021) \[G01\].

Kapoor y Narayanan: taxonomía de leakage. Wilson y colegas: organización y reproducción. Datasheets: selección de preguntas sobre origen y uso. 25–35 minutos.

**Ampliación y material práctico:** Huyen (2025) \[R09\]; Debenedetti et al. (2024) \[E03\]; Lei et al. (2025) \[D10\]; Anthropic (2024) \[R01\].

CLASE 3 \| 120 MINUTOS

# Confiabilidad entre corridas

¿El agente llega a la misma conclusión si lo ejecutamos de nuevo?

**Al finalizar:** Medir la variabilidad del agente con corridas repetidas; separar incertidumbre de muestreo, variabilidad del agente y sensibilidad a decisiones analíticas; reportar el conjunto de resultados en lugar de elegir la mejor corrida.

| **Minutos** | **Actividad** | **Contenido y aplicación** |
|:--:|:---|:---|
| 00–15 | Variación entre analistas | Comparar dos respuestas del agente al mismo problema y localizar las decisiones que difieren. |
| 15–40 | Corridas repetidas | Ejecutar el agente varias veces con el mismo presupuesto; medir la tasa de éxito y la consistencia entre corridas. |
| 40–60 | Workflow estadístico | Repasar validación fuera de muestra y diagnósticos con un modelo sencillo preparado por el docente, que sirve de referencia para el agente. |
| 60–95 | Taller de sensibilidad | Variar decisiones declaradas (faltantes, especificación, instrucciones del agente) y registrar el conjunto de resultados. |
| 95–110 | Interpretación | Distinguir explicación predictiva de efecto causal; reconocer que elegir la mejor de varias corridas es seleccionar según el resultado. |
| 110–120 | Comprobación de aprendizaje | Redactar una conclusión con tamaño del efecto, incertidumbre, variabilidad del agente y límites. |

**Ejercicio central:** El grupo ejecuta el agente varias veces y cambia decisiones defendibles previamente declaradas, como el manejo de faltantes o la especificación del modelo. Debe explicar si la conclusión es estable y qué incertidumbre no está cuantificada.

**Entrega:** Tablero de corridas repetidas con baseline, tasa de éxito, diagnósticos y tabla de sensibilidad; todas las corridas quedan registradas.

**Criterio de aprendizaje:** La dispersión entre ejecuciones no se presenta como intervalo de confianza ni como probabilidad de que la conclusión sea verdadera.

## Referencias académicas

Bertran et al. (2026) \[F04\]; Rabanser et al. (2026) \[F10\]; Gelman et al. (2020) \[S02\].

Bertran y colegas: diseño y dispersión analítica. Rabanser y colegas: dimensiones de confiabilidad. Bayesian Workflow: comprobación del modelo. 30–40 minutos.

**Ampliación y material práctico:** Silberzahn et al. (2018) \[S05\]; Gabry et al. (2019) \[S04\]; Rudin (2019) \[X01\]; Rewolinski et al. (2026) \[F05\].

CLASE 4 \| 120 MINUTOS

# Supervisión humana y afirmaciones causales

¿La recomendación corresponde a un efecto identificado?

**Al finalizar:** Definir los roles de principal, actor y crítico; establecer cuándo el agente debe escalar a una persona; definir un estimando causal y usar un DAG como artefacto de revisión; reconocer cuándo la respuesta correcta es abstenerse.

| **Minutos** | **Actividad** | **Contenido y aplicación** |
|:--:|:---|:---|
| 00–15 | Caso de Simpson y selección | Observar cómo una asociación agregada cambia al distinguir grupos; discutir explicaciones alternativas. |
| 15–40 | Diseño antes de estimación | Definir tratamiento, resultado, población y tiempo cero; dibujar un DAG y discutir intercambiabilidad y positividad. |
| 40–60 | Roles y escalamiento | Asignar responsabilidades al principal, al actor y al crítico; escribir en código las condiciones que obligan al agente a pedir revisión. |
| 60–95 | Taller de crítica causal | Revisar una recomendación del agente junto con su traza: selección de controles, balance, sensibilidad y diagnósticos. |
| 95–110 | Abstención | Formular una respuesta de no identificación y decidir qué dato o diseño haría falta para responder. |
| 110–120 | Comprobación de aprendizaje | Defender por qué el diseño permite o no permite la afirmación causal solicitada. |

**Ejercicio central:** Usar datos simulados de una intervención con confusión conocida. El agente propone una recomendación; el equipo, en el rol de crítico, la revisa con el DAG y prepara un caso donde la respuesta correcta sea abstenerse.

**Entrega:** Protocolo de revisión con roles, condiciones de escalamiento, DAG, estimando, supuestos y decisión de uso o abstención.

**Criterio de aprendizaje:** Ajustar muchas variables, obtener buen balance o pasar un placebo no se presenta como prueba de ausencia de confusión no observada.

## Referencias académicas

Hernán y Robins (2020) \[B06\]; Sharma y Kiciman (2020) \[C01\]; Zečević et al. (2023) \[C04\].

What If: selección de la Parte I. DoWhy: cuatro etapas. Causal Parrots: hablar de causalidad no es razonar causalmente. 30–40 minutos.

**Ampliación y material práctico:** Chou et al. (2026) \[R03\]; Huntington-Klein (2025) \[B08\]; Kıcıman et al. (2024) \[C03\]; Leban et al. (2026) \[F08\].

CLASE 5 \| 120 MINUTOS

# Evaluar y defender un agente confiable

¿El sistema resiste una evaluación independiente?

**Al finalizar:** Diseñar una evaluación de tareas y fallas; comparar agentes bajo presupuestos comunes; calibrar revisores automáticos; entregar un resultado defendible y reproducible.

| **Minutos** | **Actividad** | **Contenido y aplicación** |
|:--:|:---|:---|
| 00–15 | Definir la evaluación | Separar tareas de desarrollo y test; establecer criterios, presupuesto y fallas críticas antes de ejecutar. |
| 15–35 | Medir confiabilidad | Evaluar consistencia entre corridas, robustez a cambios, gravedad de errores, costo y abstención. |
| 35–55 | Elegir y calibrar revisores | Combinar pruebas determinísticas y revisión humana; contrastar un juez LLM con etiquetas expertas. |
| 55–90 | Taller de evaluación final | Ejecutar baseline y versión mejorada sobre casos reservados; registrar aciertos, fallas y artefactos. |
| 90–110 | Defensa cruzada | Intercambiar informes entre equipos; auditar evidencia, reproducibilidad y una afirmación causal o estadística. |
| 110–120 | Cierre y evaluación individual | Explicar una falla restante, su consecuencia y la siguiente prueba o dato que se necesita. |

**Ejercicio central:** Comparar el agente inicial y el mejorado con el mismo modelo, datos y presupuesto. El equipo revisor verifica al menos un cálculo y un supuesto; los fallos también se entregan.

**Entrega:** Informe final con protocolo de evaluación, resultados por tipo de falla, costos, evidencia reproducible y decisión de uso o abstención.

**Criterio de aprendizaje:** Un reporte persuasivo no compensa una falla crítica; el evaluador no comparte los resultados reservados con el agente durante el desarrollo.

## Referencias académicas

Kapoor et al. (2025) \[E01\]; Rabanser et al. (2026) \[F10\]; Zheng et al. (2023) \[E02\]; Raji et al. (2020) \[G04\].

AI Agents That Matter: evaluación y costos. Rabanser y colegas: dimensiones de confiabilidad. Zheng y colegas: límites de jueces LLM. 25–35 minutos.

**Ampliación y material práctico:** Anthropic (2026) \[R02\]; Huyen (2025) \[R09\]; Buçinca et al. (2021) \[X10\]; Rewolinski et al. (2026) \[F05\].

# Proyecto y evaluación

El proyecto es un agente para un caso de uso concreto: responder una pregunta de retención o de desempeño de una intervención con tablas de clientes, pedidos y campañas. Se recomienda usar datos simulados con un mecanismo generador conocido y errores sembrados. Esto permite comprobar resultados y supuestos sin depender de datos privados.

El mismo caso se utiliza durante las cinco clases. Los equipos conservan el agente inicial y lo comparan con su versión final usando el mismo modelo, datos, presupuesto y criterios. Se registran también las corridas fallidas. Para preguntas causales reales, la posibilidad de abstenerse es un resultado correcto cuando la evidencia no identifica el efecto.

## Evidencia que debe entregar cada equipo

- Contrato de tarea, arquitectura del agente y herramientas con sus controles.

- Código Python, consultas SQL, versiones, configuración, registro de herramientas y trazas de ejecución.

- Protocolo de evaluación con casos reservados, corridas repetidas, resultados por tipo de falla, costos y condiciones de escalamiento.

- Informe breve con afirmaciones verificables, incertidumbre, límites y recomendación de uso o abstención.

**Calificación:** prácticos 40% (las entregas de las clases 1 a 4, 10% cada una), clase 20% (participación en los talleres y discusiones) y evaluación final 40% (informe y defensa de la clase 5, con una respuesta individual breve). La evaluación final se corrige con esta rúbrica:

| **Dimensión** | **Puntos** | **Evidencia esperada** |
|:--:|:---|:---|
| Diseño del agente | 25 | Contrato de tarea, arquitectura, herramientas con controles, límites y trazas completas. |
| Evaluación y confiabilidad | 25 | Casos reservados, corridas repetidas, fallas por categoría, costo registrado y comparación con el agente inicial. |
| Supervisión y seguridad | 10 | Condiciones de escalamiento, defensa ante instrucciones en los datos y abstención cuando corresponde. |
| Validez de datos y estadística | 20 | Población, joins, fechas, denominadores y leakage comprobados; incertidumbre interpretada correctamente. |
| Validez causal | 10 | Estimando y supuestos explícitos; identificación defendida o abstención justificada. |
| Comunicación y revisión | 10 | Afirmaciones apoyadas por evidencia; límites y decisión de uso claros. |

**Condiciones de aceptación:** un resultado inventado, una fuga del conjunto reservado o una afirmación causal sin identificación obliga a corregir esa parte antes de aceptar el trabajo. Una puntuación alta en otras dimensiones no compensa esa falla. Se evalúa la calidad del juicio y de la evidencia, además del rendimiento numérico.

La defensa puede hacerse entre pares durante la última clase, seguida de una respuesta individual breve. No requiere una presentación extensa de cada equipo.

## Lecturas

En [`referencias/`](../referencias/) y en la página de cada clase.
