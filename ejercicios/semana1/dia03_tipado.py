"""Día 3: tipado y dataclasses.

1. Lee la cheat sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
2. Completa el código y comprueba:  uv run mypy ejercicios/semana1/dia03_tipado.py
   Objetivo: 0 errores en modo strict.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Turno:
    """Una intervención de la llamada (como un `type` inmutable de TS)."""

    hablante: str
    texto: str


def parsear(ruta: Path) -> list[Turno]:
    """Convierte el archivo en una lista de Turno."""
    # TODO: reutiliza la lógica del día 2, pero devolviendo dataclasses
    raise NotImplementedError


def es_buzon_de_voz(turnos: list[Turno]) -> bool:
    """True si el primer turno del AGENT contiene 'leave a message'."""
    # TODO: next(...) con un generator y un valor por defecto
    raise NotImplementedError


if __name__ == "__main__":
    for archivo in ("data/llamada_ejemplo.txt", "data/llamada_buzon.txt"):
        turnos = parsear(Path(archivo))
        print(archivo, "-> buzón de voz:", es_buzon_de_voz(turnos))
