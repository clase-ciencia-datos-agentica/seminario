#!/usr/bin/env bash
# Se corre una vez, al crear el Codespace: instala Ollama, baja el modelo e instala DuckDB.
# Si algo falla, se puede volver a correr: bash .devcontainer/preparar.sh
set -euo pipefail

echo "== Instalando Ollama"
sudo apt-get update -y && sudo apt-get install -y zstd   # el instalador de Ollama lo necesita
curl -fsSL https://ollama.com/install.sh | sh

echo "== Arrancando Ollama"
bash .devcontainer/iniciar.sh

echo "== Bajando el modelo (3 a 4 GB)"
ollama pull qwen3.5:4b

echo "== Instalando DuckDB (el agente de la clase 2)"
pip install --user duckdb

echo
echo "Codespace listo. Probá: ollama run qwen3.5:4b"
