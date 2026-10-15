# python-ai-lab

Mi laboratorio para pasar de TypeScript a Python aplicado a GenAI. El plan completo y el progreso están en **[PLAN.md](PLAN.md)**.

## Puesta en marcha (una sola vez)
```powershell
uv sync                   # crea .venv e instala todo
copy .env.example .env    # y pon tu OPENROUTER_API_KEY
uv run pytest             # 2 tests en verde y 3 en skip: todo listo
```

## Comandos del día a día
| Para… | Comando |
|---|---|
| Ejecutar un ejercicio | `uv run python ejercicios/semana1/dia02_estadisticas.py` |
| Consola interactiva | `uv run python` |
| Lint y formato | `uv run ruff check . --fix` y `uv run ruff format .` |
| Tipos (modo estricto) | `uv run mypy src ejercicios` |
| Tests | `uv run pytest` |
| Arrancar la API | `uv run uvicorn demo_agent.api:app --reload` → http://127.0.0.1:8000/docs |
| Añadir una librería | `uv add nombre` (o `uv add --dev nombre` para herramientas) |

En VS Code también puedes pulsar **F5** con un archivo abierto ("Ejecutar archivo actual") para ejecutarlo con el depurador.

## Estructura
```
ejercicios/      prácticas guiadas, un archivo por día (semanas 1-2)
src/demo_agent/  el proyecto que crece hasta ser la demo 1
tests/           pytest
data/            transcripciones ficticias para practicar
notas/           tu chuleta de TypeScript a Python
```
