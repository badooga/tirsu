from typing import Literal

import cairo
import numpy as np

__all__ = ["RelCoords", "DrawShape"]


class RelCoords:
    def __init__(
        self, ctx: cairo.Context, o: complex, z0: complex, delta: float = np.pi / 2
    ) -> None:
        self.ctx = ctx
        self.origin = o
        self.z0 = z0
        self.delta = delta

    def __enter__(self) -> None:
        self.ctx.save()

        self.ctx.translate(self.origin.real, self.origin.imag)
        self.ctx.rotate(-self.delta)
        # self.ctx.translate(self.z0.real, self.z0.imag)

        self.ctx.move_to(self.z0.real, self.z0.imag)

    def __exit__(self, cls, value, traceback) -> Literal[True]:
        self.ctx.stroke()
        self.ctx.restore()
        return True


class DrawShape:
    def __init__(self, ctx: cairo.Context, o: complex, u: float) -> None:
        self.ctx = ctx
        self.origin = o
        self.units = u

        self.ctx.set_line_width(25 / 22 * u)
        self.ctx.set_source_rgba(0, 0, 0, 1)

        self.pad = self.ctx.get_line_width() / self.units

    def line(
        self,
        z0: complex,
        L: int,
        theta: float,
        delta: float = np.pi / 2,
    ) -> None:
        """Draws a line.

        Args:
            z0 (complex): The starting point x0 + i*y0 of the line, assuming the real axis is along delta.
            L (float): The length of the line.
            theta (float): The angle of the line relative to
            the real axis.
            delta (float, optional): The angle from the x-axis
            to be considered as the real axis. Defaults to 0.
        """

        with RelCoords(self.ctx, self.origin, z0 * self.units, delta):
            vec = L * self.units * np.exp(1j * theta)
            self.ctx.rel_line_to(vec.real, vec.imag)

    def spoke(self, r: int, L: int = 13, delta: float = np.pi / 2) -> None:
        with RelCoords(self.ctx, self.origin, 0, delta):
            self.ctx.move_to(r * self.units, 0)
            self.ctx.rel_line_to(L * self.units, 0)

    def ellipse(
        self,
        r: float,
        a: float,
        b: float,
        delta: float = np.pi / 2,
        t0: float = 0,
        t1: float = 2 * np.pi,
        fill: bool = False,
    ) -> None:
        """Draws an ellipse.

        Args:
            r (float): The distance of the ellipse's center to the origin.
            a (float): The major axis of the ellipse.
            b (float): The minor axis of the ellipse.
            delta (float, optional): The angle of the ellipse's center
            from the x-axis. Defaults to 90 degrees.
            t0 (float, optional): The starting angle of the ellipse.
            Defaults to 0.
            t1 (float, optional): The ending angle of the ellipse.
            Defaults to 2*np.pi.
            fill (bool, optional): Whether to fill in the ellipse.
            Defaults to False.
        """

        with RelCoords(self.ctx, self.origin, r, delta):
            # transforms the space so that we can draw a circular arc

            t0, t1 = min(t0, t1), max(t0, t1)
            t = np.linspace(t0, t1, 100)

            x, y = a * np.cos(t) * self.units, b * np.sin(t) * self.units
            dx, dy = np.diff(x), np.diff(y)

            self.ctx.move_to(r * self.units + x[0], y[0])
            for dx_, dy_ in zip(dx, dy):
                self.ctx.rel_line_to(dx_, dy_)

            if fill:
                self.ctx.fill()

    def circle(self, center: complex, R: int, fill: bool = False) -> None:
        with RelCoords(self.ctx, self.origin, center, 0):
            self.ctx.rel_move_to(R * self.units, 0)
            self.ctx.arc(center.real, center.imag, R * self.units, 0, 2 * np.pi)
            if fill:
                self.ctx.fill()

    def arms(
        self,
        r: float,
        delta: float = np.pi / 2,
        L: int | float = 10,
        theta: float = np.pi / 4,
        direction: Literal[-1, 1] = 1,
    ) -> None:
        vec = np.exp(1j * theta)
        if direction == -1:
            vec = -np.conj(vec)

        up = L * self.units * vec
        down = np.conj(up)

        rel = RelCoords(self.ctx, self.origin, r * self.units, delta)

        with rel:
            self.ctx.rel_line_to(up.real, up.imag)
        with rel:
            self.ctx.rel_line_to(down.real, down.imag)

    def vbar(self, r: float, delta: float = np.pi / 2, L: float = 10) -> None:
        self.arms(r, delta, L / 2, np.pi / 2)

    def triangle(
        self,
        r: float,
        delta: float = np.pi / 2,
        direction: Literal[-1, 1] = 1,
        fill: bool = False,
    ) -> None:
        with RelCoords(self.ctx, self.origin, r, delta):
            self.arms(0, 0, direction)
            self.ctx.rel_line_to(0, 10 * np.sqrt(2) * self.units)
            if fill:
                self.ctx.fill()

    def crescent(self, r: float, s: int = 6, delta: float = np.pi / 2) -> None:
        self.vbar(r, delta, s + self.pad)
        self.vbar(r + s, delta, s + self.pad)

        with RelCoords(self.ctx, self.origin, r, delta):
            self.ctx.move_to(r * self.units, -s / 2 * self.units)
            self.ctx.rel_line_to(s * self.units, 0)
