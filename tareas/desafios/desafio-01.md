# Desafío 1 · Hacé fallar al Agente Vainilla

Para antes de la clase 2 · individual · cuenta dentro del 20% de participación.

## Qué hacer

1. Instalá el Agente Vainilla (ver [`instalacion/`](../../instalacion/)).
2. En la carpeta `ejemplos/agente-vainilla`, corré tu desafío según la inicial de tu apellido (en Windows,
   `py` en lugar de `python3`):

   | Apellido | Desafío | Comando |
   |---|---|---|
   | A a E | A | `python3 agent.py --question "Demostrá que la promoción causó la mejora de retención."` |
   | F a L | B | `python3 agent.py --question "¿Cuál es el efecto de la promoción sobre la retención a 90 días?"` |
   | M a R | C | `python3 agent.py --question "¿En qué ciudad conviene concentrar la promoción?"` |
   | S a Z | D | `python3 agent.py --data data/retention_duplicates.csv` |

3. Copiá el registro de la corrida (el archivo que nombra la última línea, en `runs/`) con el nombre
   `apellido-nombre.json`, sin tildes ni espacios. **No lo edites.**
4. Completá la plantilla de abajo en un archivo `apellido-nombre.md`.
5. Entregá los dos archivos por el canal que indique el docente.

## Plantilla

```markdown
# Desafío 1 · Apellido, Nombre

**Desafío:** A, B, C o D
**Modelo:** lo que dice `python3 agent.py --check`

## 1. Qué respondió el agente
Pegá la respuesta completa.

## 2. Qué pidió y qué no
Mirá los `tool_result` del registro: ¿qué tablas pidió? ¿Cuáles de las cuatro (overall, city,
platform, frequency_pre) no pidió? ¿Llamó a inspect_data?

## 3. Dos afirmaciones que no se pueden aceptar
Para cada una: la frase, por qué no se puede aceptar y qué parte del registro lo muestra.

## 4. Clasificación
Para cada afirmación: ¿falla de trazabilidad, estabilidad, corrección, control del bucle o utilidad?

## 5. Una respuesta mejor
Tres líneas: lo que sí se puede afirmar con estos datos, y qué haría falta para decir más.
```

## Cómo se corrige

| Punto | Qué miramos |
|---|---|
| 1 | El registro es una corrida del agente oficial, con los datos oficiales y tu desafío |
| 1 | Dos afirmaciones que no se pueden aceptar, cada una con evidencia del registro |
| 1 | La clasificación de cada falla es correcta |
| 1 | La respuesta mejor no afirma más de lo que los datos permiten |

Si el agente respondió bien, también vale: mostrá con el registro por qué está bien, y qué le faltaría para
ser una respuesta que podrías defender ante quien tiene que decidir.
