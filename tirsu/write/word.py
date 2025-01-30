import cairo

from ..draw import DrawLetter
from ..language import TirStr, TirWord


def write_glyph(
    ctx: cairo.Context, word: TirWord, center: complex, radius: float, units: float
) -> None:
    draw = DrawLetter(ctx, center, units)
    draw.circle(0, radius)

    letters, angles = word.letters, word.angles

    draw.beginning(radius, angles[0])
    for letter, angle in zip(letters, angles):
        if letter == "'":
            draw.apostrophe(radius, angle)
        else:
            getattr(draw, letter)(radius, angle)
