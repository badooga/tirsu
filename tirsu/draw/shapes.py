from typing import Literal

import cairo
import numpy as np


class RelCoords:
    def __init__(
        self, ctx: cairo.Context, o: complex, z0: complex, delta: float = np.pi / 2
    ) -> None:
        self.ctx = ctx
        self.o = o
        self.z0 = z0
        self.delta = delta

    def __enter__(self) -> None:
        self.ctx.save()

        self.ctx.translate(self.o.real, self.o.imag)
        self.ctx.rotate(-self.delta)
        # self.ctx.translate(self.z0.real, self.z0.imag)

        self.ctx.move_to(self.z0.real, self.z0.imag)

    def __exit__(self, cls, value, traceback) -> Literal[True]:
        self.ctx.stroke()
        self.ctx.restore()
        return True


class Draw:
    def __init__(self, ctx: cairo.Context, o: complex, u: float) -> None:
        self.ctx = ctx
        self.o = o
        self.u = u

        self.ctx.set_line_width(25 / 22 * u)
        self.ctx.set_source_rgba(0, 0, 0, 1)

    def line(
        self,
        z0: complex,
        L: int,
        delta: float = np.pi / 2,
    ) -> None:
        """Draws a line.

        Args:
            z0 (complex): The starting point x0 + i*y0 of the line.
            L (float): The length of the line.
            delta (float, optional): The angle of the line relative
            to the x-axis. Defaults to 0.
            after creating the line. Defaults to True.
        """

        with RelCoords(self.ctx, self.o, z0, delta):
            self.ctx.rel_line_to(L * self.u, 0)

    def spoke(self, r: int, L: int = 13, delta: float = np.pi / 2) -> None:
        with RelCoords(self.ctx, self.o, 0, delta):
            self.ctx.move_to(r * self.u, 0)
            self.ctx.rel_line_to(L * self.u, 0)

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

        with RelCoords(self.ctx, self.o, r, delta):
            # transforms the space so that we can draw a circular arc

            t0, t1 = min(t0, t1), max(t0, t1)
            t = np.linspace(t0, t1, 100)

            x, y = a * np.cos(t) * self.u, b * np.sin(t) * self.u
            dx, dy = np.diff(x), np.diff(y)

            self.ctx.move_to(r * self.u + x[0], y[0])
            for dx_, dy_ in zip(dx, dy):
                self.ctx.rel_line_to(dx_, dy_)

            if fill:
                self.ctx.fill()

    def circle(self, center: complex, R: int, fill: bool = False) -> None:
        with RelCoords(self.ctx, self.o, center, 0):
            self.ctx.rel_move_to(R * self.u, 0)
            self.ctx.arc(center.real, center.imag, R * self.u, 0, 2 * np.pi)
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

        up = L * self.u * vec
        down = np.conj(up)

        rel = RelCoords(self.ctx, self.o, r * self.u, delta)

        with rel:
            self.ctx.rel_line_to(up.real, up.imag)
        with rel:
            self.ctx.rel_line_to(down.real, down.imag)

    def vbar(self, r: int, delta: float = np.pi / 2, L: int = 10) -> None:
        self.arms(r, delta, L / 2, np.pi / 2)

    def triangle(
        self,
        r: float,
        delta: float = np.pi / 2,
        direction: Literal[-1, 1] = 1,
        fill: bool = False,
    ) -> None:
        with RelCoords(self.ctx, self.o, r, delta):
            self.arms(0, 0, direction)
            self.ctx.rel_line_to(0, 10 * np.sqrt(2) * self.u)
            if fill:
                self.ctx.fill()

    def crescent(self, z0: complex, delta: float = np.pi / 2, s: int = 6):
        with RelCoords(self.ctx, self.o, z0, delta):
            self.vbar(0, 0, s)
            self.vbar(s, 0, s)

            self.ctx.move_to(z0.real, z0.imag + s / 2)
            self.ctx.rel_line_to(s, 0)
