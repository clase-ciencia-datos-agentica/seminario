# Entrega 1 · Instalar y leer

Individual · para la clase 2 · una hora, casi toda de descarga y lectura · 10%

1. **Instalá Ollama** desde [ollama.com/download](https://ollama.com/download) y abrilo.
2. **Bajá el modelo** (3 a 4 GB, con buena conexión):

   ```bash
   ollama pull qwen3.5:4b
   ```

3. **Hacele una pregunta.** Abrí el modelo, apagá el razonamiento visible y preguntale:

   ```bash
   ollama run qwen3.5:4b
   ```

   ```text
   /set nothink
   Quiero lavar el auto. El lavadero está a 100 metros. ¿Voy caminando o en auto?
   ```

   `/bye` para salir.
4. **Leé un extracto** de una de las [lecturas de la clase 1](../clases/01-agente-y-contrato/#lecturas)
   (25 a 35 minutos).

## Qué mandar

Hasta la noche anterior a la clase 2, por el canal que indique el docente:

- La **captura** de la respuesta del modelo, con una línea tuya: ¿está bien? ¿Por qué?
- Una línea sobre la lectura: **una idea que te llevás**.

¿Tu computadora no puede correr el modelo? Avisale al docente; también podés usar
[Codespaces](../instalacion/codespaces.md).
