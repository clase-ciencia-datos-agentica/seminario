# Sin instalar nada: GitHub Codespaces

Si tu computadora no puede correr el modelo, podés usar todo el curso desde el navegador. Un Codespace es
una máquina de GitHub con este repositorio, Python, Ollama y el modelo ya instalados.

## Cómo abrirlo

1. Iniciá sesión en GitHub.
2. En la página de este repositorio: botón verde *Code* → pestaña *Codespaces* → *Create codespace on main*.
3. La primera vez tarda unos minutos: instala Ollama, baja el modelo (3 a 4 GB) y los paquetes del kit.
   Esperá a que la terminal diga **Codespace listo**.
4. En la terminal:

   ```bash
   cd ejemplos/agente-vainilla
   python agent.py --check
   python agent.py
   ```

Para el kit (clases 2 a 5), abrí los notebooks de `kit/notebooks/` desde el editor del Codespace.

## Lo que tenés que saber

- **Cuota.** Tu cuenta gratuita de GitHub incluye 120 horas de cómputo por mes; esta máquina tiene 4
  núcleos y cuenta por 4, así que te alcanza para unas 30 horas por mes. Sobra para el seminario si lo
  detenés cuando no lo usás: *Code* → *Codespaces* → *…* → *Stop codespace*. Con el
  [paquete para estudiantes de GitHub](https://education.github.com/pack) tenés más horas.
- **Dónde corre.** En una máquina de GitHub, no en tu computadora. Para este curso no importa: los datos
  son sintéticos o están disfrazados.
- **Velocidad.** No tiene GPU: cada turno del modelo puede tardar más que en una computadora con buena
  memoria.
- **Tu trabajo.** No podés guardar cambios en este repositorio: si querés guardarlos con git, GitHub te
  ofrece crear una copia propia (un *fork*); aceptá. Para las entregas, seguí lo que indique el docente.
- **Si algo falló al crearlo**, corré en la terminal `bash .devcontainer/preparar.sh`.
