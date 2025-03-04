from contextlib import contextmanager
from typing import Literal

import cairo
import numpy as np

__all__ = ["rel_coords", "DrawShape"]


@contextmanager
def rel_coords(
    ctx: cairo.Context, origin: complex, z0: complex, delta: float = np.pi / 2
):
    ctx.save()
    try:
        ctx.translate(origin.real, origin.imag)
        ctx.rotate(-delta)
        ctx.move_to(z0.real, z0.imag)
        yield
    finally:
        ctx.stroke()
        ctx.restore()


class DrawShape:
    def __init__(self, ctx: cairo.Context, o: complex) -> None:
        self.ctx = ctx
        self.origin = o

        self.ctx.set_line_width(25 / 22)
        self.ctx.set_source_rgba(0, 0, 0, 1)

    def draw(
        self, vecs: list[complex], z0: complex, delta: float = np.pi / 2
    ) -> None:
        """Draws between a list of relative points.

        Args:
            vecs (list[complex]): The list of vectors to draw along.
            z0 (complex): The point to start at.
            delta (float, optional): The angle from the x-axis
            to be considered as the real axis. Defaults to 0.
        """

        with rel_coords(self.ctx, self.origin, z0, delta):
            for vec in vecs:
                self.ctx.rel_line_to(vec.real, vec.imag)
            for vec in vecs[::-1]:
                self.ctx.rel_line_to(-vec.real, -vec.imag)

    def circle(self, center: complex, R: float, fill: bool = False) -> None:
        with rel_coords(self.ctx, self.origin, center, 0):
            self.ctx.rel_move_to(R, 0)
            self.ctx.arc(center.real, center.imag, R, 0, 2 * np.pi)
            if fill:
                self.ctx.fill()

    def line(
        self, L: float = 10, theta: float = 0, go_back: bool = False
    ) -> list[complex]:
        """Constructs a line.

        Args:
            L (float): The length of the line.
            theta (float): The angle of the line in the relative coordinate system.
            go_back (bool, optional): Whether to go back along the route

        Returns:
            list[complex]: The points along the line.
        """

        vec = L * np.exp(1j * theta)
        if go_back:
            return [vec, -vec]
        return [vec]

    def spoke(self, L: float = 10, go_back: bool = False) -> list[complex]:
        return self.line(L, 0, go_back)

    def ellipse(
        self, a: float = 3, b: float = 5, t0: float = 0, t1: float = 2.1 * np.pi
    ) -> list[complex]:
        """Constructs an ellipse.

        Args:
            a (float, optional): The major axis of the ellipse. Defaults to 3u.
            b (float, optional): The minor axis of the ellipse. Defaults to 5u.
            t0 (float, optional): The starting angle of the ellipse. Defaults to 0.
            t1 (float, optional): The ending angle of the ellipse. Defaults to a little over 2*np.pi.
            fill (bool, optional): Whether to fill in the ellipse. Defaults to False.

        Returns:
            list[complex]: The points along the ellipse.
        """

        t0, t1 = min(t0, t1), max(t0, t1)
        t = np.linspace(t0, t1, 100)

        z = a * np.cos(t) + 1j * b * np.sin(t)
        return np.diff(z).tolist()

    def arms(
        self, L: float = 10, theta: float = np.pi / 4, direction: Literal[-1, 1] = 1
    ) -> list[complex]:
        up = L * np.exp(-1j * theta)
        if direction == -1:
            up = -np.conj(up)
        down = np.conj(up)

        return [up, -up, down, -down]

    def vbar(self, L: float = 10) -> list[complex]:
        return self.arms(L / 2, np.pi / 2)

    def triangle(self, L: float = 10, direction: Literal[-1, 1] = 1) -> list[complex]:
        vecs = self.arms(L, direction=direction)
        vecs[-1] = vecs[0] - vecs[2]
        vecs.append(vecs[1])
        return vecs

    def crescent(self, s: float = 6) -> list[complex]:
        right, up, down = s, -1j * s, 1j * s

        return [down / 2, up, right, down]
