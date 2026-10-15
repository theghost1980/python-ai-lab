"""Día 10: verificación de citas sin modelo, tu sello.

Una cita es válida si su texto aparece literalmente en lo que dijo ese hablante.
"""

from demo_agent.models import Quote


def quote_is_verbatim(quote: Quote, transcript: str) -> bool:
    """True si `quote.text` aparece tal cual en una línea de `quote.speaker`."""
    # TODO (día 10): recorre las líneas "HABLANTE: texto" y comprueba la subcadena.
    #   Extra: normaliza espacios y comillas tipográficas antes de comparar.
    raise NotImplementedError
