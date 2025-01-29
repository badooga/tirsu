import pytest

from .. import alphabet, tir


class TestTirStr:
    @pytest.fixture(
        scope="class", params=["vlaakith", "zhak vo'n'fynh duj", "zhak vo'n'ash duj"]
    )
    def phrase(self, request: pytest.FixtureRequest) -> tir.TirStr:
        word = request.param
        return tir.TirStr(word)

    def test_letters(self, phrase: tir.TirStr):
        for letter in phrase.letters:
            assert alphabet.in_alphabet(letter)
            assert 1 <= len(letter) <= 2
