# Agente Vainilla SQL

El agente de la clase 2: el mismo ciclo de la clase 1 y el mismo modelo local, pero ahora sus
herramientas consultan tres tablas con SQL, usando [DuckDB](https://duckdb.org). Son los mismos 1.000
usuarios de la clase 1, en las tablas de las que salió aquel CSV.

## Instalación (la entrega 2)

Unos 15 minutos si ya tenés Ollama y el modelo de la entrega 1.

1. **Python 3.9 o más nuevo.** Probá `python3 --version` (en Windows, `py --version`). Si no aparece una
   versión, instalalo de [python.org](https://www.python.org/downloads/).
2. **DuckDB**, la base de datos que corre las consultas. En una terminal:

   ```bash
   python3 -m pip install duckdb
   ```

   En Windows: `py -m pip install duckdb`.
3. **Esta carpeta.** Bajala, abrí una terminal adentro (ver abajo) y corré:

   ```bash
   python3 agent.py --check
   ```

   Tiene que terminar en **Todo listo**. Revisa Python, DuckDB, las tablas, Ollama y el modelo.

**Abrir una terminal en la carpeta.** En macOS, abrí Terminal, escribí `cd ` (con espacio), arrastrá la
carpeta a la ventana y apretá Enter. En Windows, abrí la carpeta, hacé clic derecho en un espacio vacío y
elegí *Abrir en Terminal*.

## Las tablas

| Tabla | Una fila por | Columnas |
|---|---|---|
| `customers` | usuario | `user_id`, `city`, `platform`, `signup_date`, `support_note` |
| `campaigns` | usuario de la campaña de septiembre | `user_id`, `campaign_id`, `sent_date`, `promo_received`, `coupon_redeemed` |
| `orders` | pedido | `order_id`, `user_id`, `order_date`, `amount` |

La campaña salió el 1 de septiembre de 2026 (t0). El manual del curso, en `context/handbook.md`, dice
cuándo se conoce cada campo y cómo se definen la frecuencia previa y la retención.

## Cómo se usa

Sin modelo, Python y DuckDB solos:

```bash
python3 agent.py --sql "SELECT COUNT(*) FROM orders"       # una consulta tuya
python3 agent.py --inspect                                 # todas las tablas de retención
python3 agent.py --inspect overall --tools v1              # la misma tabla, con las herramientas v1
```

Con el modelo (tarda unos minutos):

```bash
python3 agent.py --tools v1      # las herramientas como vinieron
python3 agent.py                 # las herramientas con contrato (v2)
```

En macOS y Linux, la consulta va entre comillas dobles y el texto dentro de ella, entre comillas
simples: `--sql "SELECT * FROM orders WHERE order_date >= '2026-09-02'"`.

## Las dos versiones de las herramientas

El modelo puede pedir tres cosas: `inspect_data()`, `summarize_retention(breakdown)` y `run_sql(query)`.
Cambia cómo están hechas:

- **v1, como vinieron.** Son las de la clase, con sus errores: corren sin fallar y devuelven otra cosa.
  `run_sql` ejecuta cualquier SQL, sin tiempo máximo y con acceso a los archivos de tu computadora.
- **v2, con contrato.** Cuentan usuarios, no filas, y lo comprueban en cada llamada; solo ofrecen
  variables que se conocen en t0; no le mandan texto libre al modelo. `run_sql` acepta una sola consulta
  de lectura, corta a los 5 segundos, devuelve hasta 20 filas y no puede abrir ni escribir archivos.

Con `--sql`, `--tools` también elige los límites: por defecto, los de v2.

Cada corrida con el modelo deja su registro completo en `runs/`, con el SQL que ejecutó cada herramienta.

La carpeta `reservado/` guarda los datos de otra campaña, para evaluar al agente. El agente no debería
verlos nunca: en la clase vemos por qué con v1 sí puede.

## Si algo falla

- **`No module named 'duckdb'` o «Falta DuckDB».** Instalalo con el mismo Python con el que corrés el
  agente: `python3 -m pip install duckdb`. Si usás conda, activá el entorno antes.
- **`No se pudo contactar Ollama`.** Abrí la app de Ollama y volvé a probar.
- **`Modelo no descargado`.** `ollama pull qwen3.5:4b`.
- **En Windows, `python3` no existe.** Usá `py` en lugar de `python3`.
