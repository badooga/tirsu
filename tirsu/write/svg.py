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
    draw = DrawLetter(ctx, center)
    draw.circle(0, radius)

    letters, angles = word.letters, word.angles

    draw.beginning(radius, angles[0])
    for letter, angle in zip(letters, angles):
        if letter == "'":
            draw.apostrophe(radius, angle)
        else:
            getattr(draw, letter)(radius, angle)


def write_text(
    path: str | PathLike,
    text: str,
    scale: float,
    orientation: Literal[-1, 1] = 1,
) -> None:
    text = text.replace(".", "\n").replace("?", "\n").replace("!", "\n").strip().lower()

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

    grid = Grid(nx, ny, radius, 2 * DrawLetter.h_max)
    centers = grid.centers

    with cairo.SVGSurface(str(path), grid.x, grid.y) as surface:
        ctx = cairo.Context(surface)

        # ctx.save()
        # ctx.scale(scale, scale)

        for sentence, row in zip(sentences, centers):
            for word, center in zip(sentence, row):
                print(word)
                write_word(ctx, word, center, radius)

        # ctx.stroke()
        # ctx.restore()
