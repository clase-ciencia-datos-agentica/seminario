#!/usr/bin/env bash
# Se corre cada vez que arranca el Codespace: deja Ollama sirviendo en segundo plano.
if ! curl -fs http://127.0.0.1:11434/api/version > /dev/null; then
  nohup setsid ollama serve > /tmp/ollama.log 2>&1 &
  for _ in $(seq 1 30); do
    curl -fs http://127.0.0.1:11434/api/version > /dev/null && break
    sleep 1
  done
fi
