"""Día 6: modelos Pydantic, el equivalente a tus esquemas Zod.

Docs: https://docs.pydantic.dev/latest/concepts/models/
"""

from typing import Literal

from pydantic import BaseModel, Field


class Quote(BaseModel):
    """Una cita literal extraída de la transcripción."""

    speaker: Literal["AGENT", "CUSTOMER"]
    text: str = Field(min_length=3)


class Insight(BaseModel):
    """Una observación de coaching basada en citas."""

    title: str
    explanation: str
    quotes: list[Quote] = Field(min_length=1)


class CallAnalysis(BaseModel):
    """Resultado completo del análisis de una llamada."""

    is_voicemail: bool
    appointment_booked: bool
    # TODO (día 6): añade un campo `sentiment` que solo acepte "positive", "neutral" o "negative"
    insights: list[Insight] = Field(default_factory=list)
