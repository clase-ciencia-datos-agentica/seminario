#!/usr/bin/env bash
# Se corre una vez, al crear el Codespace: instala Ollama, baja el modelo y, si ya está publicado, el kit.
# Si algo falla, se puede volver a correr: bash .devcontainer/preparar.sh
set -euo pipefail

echo "== Instalando Ollama"
sudo apt-get update -y && sudo apt-get install -y zstd   # el instalador de Ollama lo necesita
curl -fsSL https://ollama.com/install.sh | sh

echo "== Arrancando Ollama"
bash .devcontainer/iniciar.sh

echo "== Bajando el modelo (3 a 4 GB)"
ollama pull qwen3.5:4b

if [ -f kit/requirements.txt ]; then   # el kit se publica con la clase 2
  echo "== Instalando los paquetes del kit"
  pip install --user -r kit/requirements.txt
fi

echo
echo "Codespace listo. Probá: ollama run qwen3.5:4b"
