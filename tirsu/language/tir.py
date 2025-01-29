"""Classes for strings and words in the Tir language."""

from collections import UserString
from typing import Literal, Self

import numpy as np

from tirsu.language import alphabet

__all__ = ["TirStr", "TirWord"]


class TirStr(UserString):
    """A string that uses the Tir alphabet.

    Attributes:
        translation (list[str]): a list containing the gith letters
        in the string.
    """

    def __init__(self, seq) -> None:
        """Initializes the string from a sequence.

        Raises:
            ValueError: If characters not in the Tir alphabet are found.
        """

        super().__init__(seq)
        self.data = self.data.strip()

        invalid = set(self.data.lower()) - alphabet.tir_alphabet - set(" ")
        if invalid:
            raise ValueError(f"Invalid characters found: {invalid}")

    def __iter__(self):
        yield from self.letters

    def __getitem__(self, key) -> Self:
        return self.__class__("".join(self.letters[key]))

    @property
    def letters(self) -> list[str]:
        """Returns a list of the Tir letters in the word."""

        newdata: list[str] = []
        for letter in self.data:
            if len(newdata) > 0:
                combined = newdata[-1] + letter
                if alphabet.in_alphabet(combined):
                    newdata[-1] = combined
                    continue
            newdata.append(letter)
        return newdata

    def __len__(self) -> int:
        return len(self.letters)


class TirWord(TirStr):
    """A class containing the data for a single word in Tir'su."""

    def __init__(self, word: str, orientation: Literal[-1, 1] = 1) -> None:
        """Initializes the word.

        Args:
            word (str): The word in the Tir language.
            orientation (Literal[-1, 1], optional): Whether to use the
            githyanki convention (1) or the githzerai convention (-1).
            Defaults to 1.

        Raises:
            ValueError: If the supplied TirStr isn't exactly one word.
        """

        if len(word.split()) != 1:
            raise ValueError("Input must be exactly one word")

        super().__init__(word)

        self.orientation = orientation

    @property
    def angles(self) -> np.ndarray:
        """Returns an array containing the angle of each letter in the word."""

        n = len(self)
        unity = np.arange(n) / n
        angles = self.orientation * (0.25 - unity)

        return 2 * np.pi * angles

    @property
    def convention(self) -> Literal["githyanki", "githzerai"]:
        """Returns whether the glyph uses the githyanki (starts from top,
        goes clockwise) or githzerai (starts from bottom, goes
        counterclockwise) dialect."""

        return "githzerai" if self.orientation == -1 else "githyanki"
