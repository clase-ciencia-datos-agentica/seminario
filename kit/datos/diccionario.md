# Diccionario de datos

Un programa de empleo seleccionó participantes y les dio capacitación y trabajo subsidiado.
Queremos saber cuánto cambió su ingreso posterior por haber participado.

Los montos están en **pesos del programa**, una moneda inventada para este curso.

| Columna | Qué es |
| --- | --- |
| `id` | Identificador de la persona |
| `participa` | 1 si participó del programa, 0 si no |
| `edad` | Edad en años |
| `anios_educ` | Años de educación formal |
| `afro` | 1 si la persona se identifica como afrodescendiente |
| `hispano` | 1 si la persona se identifica como hispana |
| `casado` | 1 si está casada |
| `sin_titulo` | 1 si no terminó la secundaria |
| `ingreso_t1` | Ingreso anual dos períodos antes del programa |
| `ingreso_t2` | Ingreso anual un período antes del programa |
| `ingreso_post` | Ingreso anual después del programa (resultado) |

## Archivos

- `programa_x.csv`: participantes + no participantes tomados de una **encuesta A** de hogares.
- `programa_x_b.csv`: los mismos participantes + no participantes de una **encuesta B** (sesión 4).

Los no participantes NO fueron asignados al azar: vienen de encuestas generales.
