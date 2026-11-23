# Entregas y evaluación

| | Qué | Peso |
|---|---|---|
| Entregas | Cuatro entregas cortas, una por clase de la 1 a la 4 | 40% (10% cada una) |
| Clase | Participación en talleres y discusiones, con un [desafío](desafios/) individual por clase | 20% |
| Final | Tu propio caso de negocio, en la clase 5 | 40% |

Con una clase cada dos días, lo que queda para la casa no pasa de un par de horas.

## Las entregas

| Clase | Entrega |
|---|---|
| 1 | [Instalar y leer](01-instalar-y-leer.md): instalar el modelo, hacerle una pregunta y leer un extracto. Individual |
| 2 | Corta, en equipos de 3, sobre las herramientas del agente. Se publica con la clase |
| 3 | Corta, en equipos de 3, sobre corridas repetidas. Se publica con la clase |
| 4 | Corta, en equipos de 3, sobre la revisión de una recomendación del agente. Se publica con la clase |

## El final: tu propio caso de negocio

En equipos de 3. Elijan una pregunta de negocio y unos datos para responderla, y hagan lo mismo que
hacemos en la clase 1 con el caso de marketing:

1. Escriban el contrato de tarea y corran un agente básico.
2. Refuércenlo: contexto (un manual del caso) y controles en el código.
3. Audítenlo con el registro: qué afirmó, qué ejecutó y qué se sostiene.
4. Comparen el agente inicial con el reforzado, con el mismo modelo, los mismos datos y las mismas
   preguntas. Las corridas fallidas también se entregan.

En la clase 5 presentan el informe y lo defienden, con una respuesta individual breve. Si sus datos son
privados, usen una versión sintética, como la de la clase 1. Cuando la evidencia no alcanza para
afirmar un efecto, abstenerse es un resultado correcto.

## Condiciones de aceptación

Un resultado inventado, una fuga del conjunto reservado o una afirmación causal sin identificación
obliga a corregir esa parte antes de aceptar el trabajo. Una puntuación alta en otras dimensiones no
compensa esa falla. Se evalúa la calidad del juicio y de la evidencia, además del rendimiento numérico.

## Rúbrica del final

| Dimensión | Puntos | Evidencia esperada |
|---|---|---|
| Diseño del agente | 25 | Contrato de tarea, arquitectura, herramientas con controles, límites y trazas completas |
| Evaluación y confiabilidad | 25 | Casos reservados, corridas repetidas, fallas por categoría, costo registrado y comparación con el agente inicial |
| Supervisión y seguridad | 10 | Condiciones de escalamiento, defensa ante instrucciones en los datos y abstención cuando corresponde |
| Validez de datos y estadística | 20 | Población, joins, fechas, denominadores y leakage comprobados; incertidumbre interpretada correctamente |
| Validez causal | 10 | Estimando y supuestos explícitos; identificación defendida o abstención justificada |
| Comunicación y revisión | 10 | Afirmaciones apoyadas por evidencia; límites y decisión de uso claros |
