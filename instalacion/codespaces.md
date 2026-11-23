# Sin instalar nada: GitHub Codespaces

Si tu computadora no puede correr el modelo, usalo desde el navegador. Un Codespace es una máquina de
GitHub con este repositorio, Ollama y el modelo ya instalados.

## Cómo abrirlo

1. Iniciá sesión en GitHub (la cuenta es gratis).
2. En la página de este repositorio: botón verde *Code* → pestaña *Codespaces* → *Create codespace on main*.
3. La primera vez tarda unos minutos: instala Ollama y baja el modelo (3 a 4 GB). Esperá a que la terminal
   diga **Codespace listo**.
4. En la terminal, la tarea para la clase 2:

   ```bash
   ollama run qwen3.5:4b
   ```

   Escribí `/set nothink`, hacé la pregunta de la tarea y `/bye` para salir.

## Lo que tenés que saber

- **Cuota.** Tu cuenta gratuita incluye 120 horas de cómputo por mes; esta máquina cuenta por 4, así que
  te alcanza para unas 30 horas. Detenelo cuando no lo uses: *Code* → *Codespaces* → *…* → *Stop codespace*.
- **Velocidad.** No tiene GPU: cada respuesta puede tardar más que en una computadora con buena memoria.
- **Si algo falló al crearlo**, corré en la terminal `bash .devcontainer/preparar.sh`.
