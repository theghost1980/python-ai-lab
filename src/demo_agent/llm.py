"""Día 7: llamar al LLM pidiendo JSON y validarlo con Pydantic.

Reutiliza el cliente async de los días 4 y 5.
"""

from demo_agent.models import CallAnalysis


async def analyze_call(transcript: str) -> CallAnalysis:
    """Envía la transcripción al LLM y devuelve un CallAnalysis validado.

    Pasos:
      1. Prompt con instrucciones y el JSON Schema: CallAnalysis.model_json_schema()
      2. Llamada a OpenRouter con response_format={"type": "json_object"}
      3. CallAnalysis.model_validate_json(texto)
      4. Si lanza ValidationError, reintenta una vez pasándole el error al modelo
    """
    # TODO (día 7)
    raise NotImplementedError
