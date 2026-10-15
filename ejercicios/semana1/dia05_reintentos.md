# Día 5: repaso y robustez

1. Haz 2 o 3 ejercicios de https://exercism.org/tracks/python y pide revisión al mentor.
2. Mejora `dia04_async.py`:
   - Reintentos con espera exponencial (1s, 2s, 4s) si la API responde 429 o 5xx.
   - Un timeout por llamada, y que una llamada fallida no tumbe las demás.
     Pista: `asyncio.gather(..., return_exceptions=True)`.
3. Pasa `uv run ruff check .` y `uv run mypy ejercicios` sin errores.
