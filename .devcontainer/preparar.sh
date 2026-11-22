#!/usr/bin/env bash
# Se corre una vez, al crear el Codespace: instala Ollama, baja el modelo y los paquetes del kit.
# Si algo falla, se puede volver a correr: bash .devcontainer/preparar.sh
set -euo pipefail

echo "== Instalando Ollama"
sudo apt-get update -y && sudo apt-get install -y zstd   # el instalador de Ollama lo necesita
curl -fsSL https://ollama.com/install.sh | sh

echo "== Arrancando Ollama"
bash .devcontainer/iniciar.sh

echo "== Bajando el modelo (3 a 4 GB)"
ollama pull qwen3.5:4b

echo "== Instalando los paquetes del kit"
pip install --user -r kit/requirements.txt

echo
echo "Codespace listo. Probá: cd ejemplos/agente-vainilla && python agent.py --check"
