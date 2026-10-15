"""Día 10: tests de la verificación de citas. Quita el `skip` cuando la implementes."""

import pytest

from demo_agent.models import Quote
from demo_agent.verify import quote_is_verbatim

TRANSCRIPT = "AGENT: The brake inspection is free.\nCUSTOMER: Great, please book me in."

pytestmark = pytest.mark.skip(reason="Día 10: implementa verify.py y borra esta línea")


def test_exact_quote_is_valid() -> None:
    assert quote_is_verbatim(Quote(speaker="AGENT", text="inspection is free"), TRANSCRIPT)


def test_invented_quote_is_rejected() -> None:
    assert not quote_is_verbatim(Quote(speaker="AGENT", text="we fix it for free"), TRANSCRIPT)


def test_wrong_speaker_is_rejected() -> None:
    assert not quote_is_verbatim(Quote(speaker="AGENT", text="please book me in"), TRANSCRIPT)
