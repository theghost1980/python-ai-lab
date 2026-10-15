"""Días 8 y 9: la API con FastAPI.

Arranca con:  uv run uvicorn demo_agent.api:app --reload
Documentación interactiva en http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="demo-agent")


class AnalyzeRequest(BaseModel):
    transcript: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


# TODO (día 8): POST /analyze que reciba AnalyzeRequest y devuelva CallAnalysis
# TODO (día 9): POST /analyze/batch que reciba varias transcripciones y envíe el progreso
#               en streaming (StreamingResponse o Server-Sent Events)
