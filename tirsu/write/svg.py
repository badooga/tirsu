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


def write_phrase(
    path: str | PathLike,
    phrase: str | TirWord,
    scale: float,
    orientation: Literal[-1, 1] = 1,
) -> None:
    words = [TirWord(word, orientation) for word in phrase.strip().split()]
    max_len = max(map(len, words))
    radius = max_len  # TODO: get max from formula

    grid = Grid(len(words), radius, 2 * DrawLetter.h_max)
    L = grid.length

    with cairo.SVGSurface(str(path), L, L) as surface:
        ctx = cairo.Context(surface)

        #ctx.save()
        #ctx.scale(scale, scale)

        for word, center in zip(words, grid.centers):
            write_word(ctx, word, center, radius)

        #ctx.stroke()
        #ctx.restore()
