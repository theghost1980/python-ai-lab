"""Día 4: asyncio (gather + Semaphore), el equivalente a Promise.all + p-limit.

Lee: https://realpython.com/async-io-python/
Ejecuta:  uv run python ejercicios/semana1/dia04_async.py
Necesitas OPENROUTER_API_KEY en el archivo .env
"""

import asyncio
import os
import time

import httpx
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
MODELO = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini")
MAX_CONCURRENCIA = 5

PREGUNTAS = [f"Dime en una frase un dato curioso sobre el número {n}." for n in range(1, 21)]


async def preguntar(cliente: httpx.AsyncClient, limite: asyncio.Semaphore, pregunta: str) -> str:
    """Hace UNA llamada al LLM respetando el límite de concurrencia."""
    async with limite:
        # TODO: cliente.post(API_URL, headers={"Authorization": f"Bearer {API_KEY}"},
        #       json={"model": MODELO, "messages": [{"role": "user", "content": pregunta}]})
        #       y devuelve el texto de choices[0].message.content
        raise NotImplementedError


async def main() -> None:
    limite = asyncio.Semaphore(MAX_CONCURRENCIA)
    inicio = time.perf_counter()
    async with httpx.AsyncClient(timeout=60) as cliente:
        # Esto ya está hecho: lanza las 20 preguntas a la vez (el Semaphore limita a 5).
        # Tu trabajo es completar preguntar().
        respuestas = await asyncio.gather(*(preguntar(cliente, limite, p) for p in PREGUNTAS))
    for r in respuestas:
        print("-", r)
    print(f"{len(respuestas)} respuestas en {time.perf_counter() - inicio:.1f}s")


if __name__ == "__main__":
    asyncio.run(main())
