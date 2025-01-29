import pytest
from typing import Literal

import numpy as np

from .. import alphabet, tir


class TestTirStr:
    @pytest.fixture(
        scope="class", params=["vlaakith", "zhak vo'n'fynh duj", "zhak vo'n'ash duj"]
    )
    def phrase(self, request: pytest.FixtureRequest) -> tir.TirStr:
        word = request.param
        return tir.TirStr(word)

    def test_letters(self, phrase: tir.TirStr) -> None:
        for letter in phrase.letters:
            assert alphabet.in_alphabet(letter)
            assert 1 <= len(letter) <= 2

class TestTirWord:
    @pytest.fixture(
        scope="class", params=["vlaakith", "vo'n'fynh", "vo'n'ash"]
    )
    def word(self, request: pytest.FixtureRequest) -> tir.TirWord:
        word = request.param
        return tir.TirWord(word)

    @pytest.mark.parametrize("orientation", [1, -1])
    def test_angles(self, word: tir.TirWord, orientation: Literal[-1, 1]) -> None:
        word.orientation = orientation
        n = len(word)

        shifted = np.pi/2 - word.orientation * word.angles
        actual = np.exp(1j * shifted)

        np.testing.assert_almost_equal(actual**n, 1)

        unity = np.roots([-1, *(0 for _ in range(n-1)), 1])
        unity = unity[np.argsort(np.angle(unity) % (2 * np.pi))]

        np.testing.assert_almost_equal(actual, unity)
