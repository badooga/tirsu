import cairo
import numpy as np

__all__ = ["draw_line", "draw_ellipse"]


def draw_line(
    ctx: cairo.Context, z0: complex, L: float, delta: float = 0, stroke: bool = True
) -> None:
    """Draws a line using cairo.

    Args:
        ctx (cairo.Context): The cairo Context to draw in.
        z0 (complex): The starting point x0 + i*y0 of the line.
        L (float): The length of the line.
        delta (float, optional): The angle of the line relative
        to the x-axis. Defaults to 0.
        stroke (bool, optional): Whether to end the brush stroke
        after creating the line. Defaults to True.
    """

    # moves to z0
    ctx.move_to(z0.real, z0.imag)

    # draws vector for L at angle delta
    dz = np.exp(1j * delta) * L
    ctx.rel_line_to(dz.real, dz.imag)

    if stroke:
        ctx.stroke()


def draw_ellipse(
    ctx: cairo.Context,
    z0: complex,
    a: float,
    b: float,
    delta: float = 0,
    t0: float = 0,
    t1: float = 2 * np.pi,
    stroke: bool = True,
    fill: bool = False,
) -> None:
    """Draws an ellipse using cairo.

    Args:
        ctx (cairo.Context): The cairo Context to draw in.
        z0 (complex): The center of the ellipse.
        a (float): The major axis of the ellipse.
        b (float): The minor axis of the ellipse.
        delta (float, optional): The angle of the minor axis
        relative to the x-axis. Defaults to 0.
        t0 (float, optional): The starting angle of the ellipse.
        Defaults to 0.
        t1 (float, optional): The ending angle of the ellipse.
        Defaults to 2*np.pi.
        stroke (bool, optional): Whether to end the brush stroke
        after creating the line. Defaults to True.
        fill (bool, optional): Whether to fill in the ellipse.
        Defaults to False.
    """

    ctx.save()

    # transforms the space so that we can draw a circular arc
    ctx.translate(z0.real, z0.imag)
    ctx.rotate(-delta)
    ctx.scale(a, b)

    # draws the arc
    t0, t1 = min(t0, t1), max(t0, t1)
    ctx.arc(0, 0, 1, t0, t1)

    # reverts the transformation, turning it into an ellipse
    ctx.restore()

    if fill:
        ctx.fill()
    if stroke:
        ctx.stroke()
