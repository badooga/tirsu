from os import PathLike
from typing import Literal

import cairo

from .grid import Grid
from ..draw import DrawLetter

from ..language import TirWord


def write_word(
    ctx: cairo.Context,
    word: TirWord,
    center: complex,
    radius: float,
) -> None:
    draw = DrawLetter(ctx, center, radius)
    draw.circle(0, radius)

    letters, angles = word.letters, word.angles

    for letter, angle in zip(letters, angles):
        draw.delta = angle
        if angle == angles[0]:
            draw.beginning()
        if letter == "'":
            draw.apostrophe()
        else:
            getattr(draw, letter)()


def write_tirsu(
    path: str | PathLike,
    text: str,
    orientation: Literal[-1, 1] = 1,
    scale: float = 1,
) -> None:
    text = text.replace(",", "").replace(".", "\n").replace("?", "\n").replace("!", "\n").strip().lower()

    sentences: list[list[TirWord]] = []

    radius = 0
    for sentence in text.split("\n"):
        sentences.append([])
        for word in sentence.split():
            tirword = TirWord(word, orientation)
            sentences[-1].append(tirword)
            radius = max(len(tirword), radius)

    ny = len(sentences)
    nx = max(map(len, sentences))

    grid = Grid(nx, ny, radius, 2 * DrawLetter.h_max, scale)
    centers = grid.centers

    with cairo.SVGSurface(str(path), grid.x, grid.y) as surface:
        ctx = cairo.Context(surface)

        for sentence, row in zip(sentences, centers):
            for word, center in zip(sentence, row):
                write_word(ctx, word, center, radius)
