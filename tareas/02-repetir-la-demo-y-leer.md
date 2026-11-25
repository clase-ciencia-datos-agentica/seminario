# Entrega 2 · Repetir la demo y leer

Individual · para la clase 3 · una hora como máximo

Dos partes, como la entrega 1: repetís en tu computadora lo que vimos en la clase 2 y leés un extracto de
una de las lecturas.

## Primero: dejá todo listo

El agente de la clase 2 usa una herramienta nueva, **DuckDB**: una base de datos que corre dentro de Python, en
tu computadora, sin servidor ni cuenta. Cada vez que arranca, el agente carga ahí las tres tablas (clientes,
campaña y pedidos), y sus herramientas le hacen consultas en SQL. No hace falta saber SQL: los comandos de
abajo están listos para copiar.

1. **Bajá el agente.** Bajá este repositorio (botón verde *Code* → *Download ZIP*, o `git pull` si lo
   clonaste) y abrí una terminal en la carpeta `ejemplos/agente-vainilla-sql`.
2. **Instalá DuckDB** y verificá el agente, siguiendo su [LEEME](../ejemplos/agente-vainilla-sql/LEEME.md):

   ```bash
   python3 -m pip install duckdb
   python3 agent.py --check
   ```

   Tiene que terminar en **Todo listo**. Ollama tiene que estar abierto, como en la entrega 1.

En Windows, escribí `py` donde dice `python3`.

## Después: los pasos de la demo, en el mismo orden

Copiá cada comando, pegalo en la terminal y compará con lo que vimos en clase. Los pasos 1 a 3 y 7 responden
al instante; los pasos 4 y 6 usan el modelo y tardan unos minutos.

1. **La herramienta como vino.** Cuenta 1.585 + 3.030 = 4.615 «usuarios», en una campaña de 1.000.

   ```bash
   python3 agent.py --inspect overall --tools v1
   ```

2. **La consulta de control.** Cuántas filas y cuántos clientes distintos deja la unión con los pedidos:
   11.146 filas, 979 clientes. Una fila por pedido.

   ```bash
   python3 agent.py --sql "SELECT COUNT(*) AS filas, COUNT(DISTINCT c.user_id) AS usuarios FROM campaigns c JOIN orders o ON o.user_id = c.user_id"
   ```

3. **La herramienta con contrato.** 500 y 500, 32 % y 68 %, con su control: los números de la clase 1.

   ```bash
   python3 agent.py --inspect overall
   ```

4. **El agente, con la versión que vino.** Mirá si nota los 4.615.

   ```bash
   python3 agent.py --tools v1
   ```

5. **Su registro.** Abrí en tu editor el archivo más nuevo de la carpeta `runs/` (su nombre lleva `_v1_`) y
   buscá `"sql"`, `4615` y `U0414`.
6. **El agente, con contrato.** La misma pregunta, con otras herramientas.

   ```bash
   python3 agent.py
   ```

7. **Los límites.** Uno atrás del otro:

   ```bash
   python3 agent.py --tools v1 --sql "SELECT * FROM 'reservado/october_campaign.csv' LIMIT 5"
   python3 agent.py --sql "SELECT * FROM 'reservado/october_campaign.csv' LIMIT 5"
   python3 agent.py --tools v1 --sql "COPY customers TO 'fuga.csv'"
   rm fuga.csv
   python3 agent.py --sql "COPY customers TO 'fuga.csv'"
   python3 agent.py --sql "SELECT SUM(a.amount * b.amount * c.amount) FROM orders a, orders b, orders c"
   ```

   El `rm fuga.csv` borra la copia que hizo la versión que vino (en Windows, `del fuga.csv`). La última
   consulta se corta a los 5 segundos: **sacale una captura**.

Si con el modelo te sale una redacción distinta a la de clase, está bien: lo vemos en la clase 3.

## Leé un extracto

Uno de los de las [lecturas de la clase 2](../clases/02-herramientas-y-datos/#lecturas): Kapoor y
Narayanan sobre leakage [S01], Wilson et al. sobre buenas prácticas [S08] o Gebru et al. sobre fichas de
datos [G01]. Entre 25 y 35 minutos.

## Qué mandar

Antes de la clase 3, por el portal UM:

- La **captura del paso 7**: la consulta que se corta a los 5 segundos.
- **Una línea sobre la lectura:** una idea que te llevás.

Es la entrega 2 (10%).

¿Algo no anda? Escribile al docente con la captura del error; también podés usar
[Codespaces](../instalacion/codespaces.md).
