# Chuleta de TypeScript a Python

Ve añadiendo filas a medida que aprendas.

| TypeScript / Node | Python |
|---|---|
| pnpm / npm | uv |
| `package.json` | `pyproject.toml` |
| `node_modules` | `.venv` |
| `pnpm add x` | `uv add x` |
| `npx tsx file.ts` | `uv run python file.py` |
| ESLint + Prettier | Ruff |
| `tsc --strict` | mypy (strict) / Pylance |
| Vitest / Jest | pytest |
| Zod | Pydantic |
| Express / Fastify | FastAPI |
| `type User = {…}` (inmutable) | `@dataclass(frozen=True)` |
| `string \| null` | `str \| None` |
| `arr.map(x => x * 2)` | `[x * 2 for x in arr]` |
| `arr.filter(x => x > 0)` | `[x for x in arr if x > 0]` |
| `Promise.all([...])` | `await asyncio.gather(...)` |
| `p-limit(5)` | `asyncio.Semaphore(5)` |
| `fetch` / axios | httpx |
| `process.env.X` | `os.environ["X"]` (+ python-dotenv) |
| `` `Hola ${name}` `` | `f"Hola {name}"` |
| `try / catch` | `try / except` |
| `str.indexOf(x)` → -1 | `str.find(x)` → -1 (¡ojo con `[:-1]`!) |
