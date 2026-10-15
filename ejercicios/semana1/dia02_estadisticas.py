"""Día 2: estructuras de datos y comprehensions.

Objetivo: leer una transcripción y sacar estadísticas.
Ejecuta:  uv run python ejercicios/semana1/dia02_estadisticas.py
"""

from pathlib import Path

RUTA = Path("data/llamada_ejemplo.txt")


def leer_lineas(ruta: Path) -> list[str]:
    """Devuelve las líneas con diálogo (ignora vacías y las que empiezan por '#')."""
    # TODO: usa ruta.read_text(encoding="utf-8").splitlines() y una list comprehension
    raise NotImplementedError


def contar_por_hablante(lineas: list[str]) -> dict[str, int]:
    """{'AGENT': 5, 'CUSTOMER': 5}. Pista: str.split(":", 1) y dict.get(clave, 0)."""
    # TODO
    raise NotImplementedError


def palabras_totales(lineas: list[str]) -> int:
    """Cuenta las palabras del texto, sin contar el nombre del hablante."""
    # TODO: sum(...) con un generator expression
    raise NotImplementedError


if __name__ == "__main__":
    lineas = leer_lineas(RUTA)
    print("Intervenciones por hablante:", contar_por_hablante(lineas))
    print("Palabras totales:", palabras_totales(lineas))
