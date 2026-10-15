"""Tests que ya pasan desde el día 0: comprueban que el entorno está bien montado."""

from fastapi.testclient import TestClient

from demo_agent.api import app
from demo_agent.models import CallAnalysis


def test_health() -> None:
    assert TestClient(app).get("/health").json() == {"status": "ok"}


def test_models_validate() -> None:
    analysis = CallAnalysis.model_validate(
        {"is_voicemail": False, "appointment_booked": True, "insights": []}
    )
    assert analysis.appointment_booked
