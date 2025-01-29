import pytest

from .. import alphabet

def test_tir_alphabet() -> None:
    assert len(alphabet.tir_alphabet) == 35

@pytest.mark.parametrize("letter", ["a", "EA", "'", "oA", "ch", "sh", "Th", "zh"])
def test_in_alphabet(letter: str) -> None:
    assert alphabet.in_alphabet(letter)
