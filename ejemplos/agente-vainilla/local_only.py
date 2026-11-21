"""Opt in to Ollama's documented local-only mode; preserve existing settings."""
import json
import shutil
from pathlib import Path


def main():
    path = Path.home() / ".ollama" / "server.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    settings = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if not isinstance(settings, dict):
        raise ValueError("Existing server.json is not a JSON object; no changes made")
    if path.exists():
        backup = path.with_name("server.json.before-seminar")
        if not backup.exists():
            shutil.copy2(path, backup)
    settings["disable_ollama_cloud"] = True
    path.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    print(f"Local-only mode configured in {path}. Quit and reopen Ollama now.")
    print("On a Linux system service use OLLAMA_NO_CLOUD=1 in the service environment instead; see README.")


if __name__ == "__main__":
    main()
