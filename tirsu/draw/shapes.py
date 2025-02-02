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
        self.ctx.move_to(self.z0.real, self.z0.imag)

    def __exit__(self, cls, value, traceback) -> Literal[True]:
        self.ctx.stroke()
        self.ctx.restore()
        return True


class DrawShape:
    def __init__(self, ctx: cairo.Context, o: complex) -> None:
        self.ctx = ctx
        self.origin = o

        self.ctx.set_line_width(25 / 22)
        self.ctx.set_source_rgba(0, 0, 0, 1)

    def line(
        self,
        z0: complex,
        delta: float = np.pi / 2,
        L: float = 10,
        theta: float = 0,
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

        with RelCoords(self.ctx, self.origin, z0, delta):
            vec = L * np.exp(1j * theta)
            self.ctx.rel_line_to(vec.real, vec.imag)

    def spoke(self, r: float, delta: float = np.pi / 2, L: float = 13) -> None:
        self.line(r, delta, L, 0)

    def ellipse(
        self,
        r: float,
        delta: float = np.pi / 2,
        a: float = 3,
        b: float = 5,
        t0: float = 0,
        t1: float = 2 * np.pi,
        fill: bool = False,
    ) -> None:
        """Draws an ellipse.

        Args:
            r (float): The distance of the ellipse's center to the origin.
            a (float, optional): The major axis of the ellipse. Defaults to 3u.
            b (float): The minor axis of the ellipse. Defaults to 5u.
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

            x, y = a * np.cos(t), b * np.sin(t)
            dx, dy = np.diff(x), np.diff(y)

            self.ctx.move_to(r + x[0], y[0])
            for dx_, dy_ in zip(dx, dy):
                self.ctx.rel_line_to(dx_, dy_)

            if fill:
                self.ctx.fill()

    def circle(self, center: complex, R: float, fill: bool = False) -> None:
        with RelCoords(self.ctx, self.origin, center, 0):
            self.ctx.rel_move_to(R, 0)
            self.ctx.arc(center.real, center.imag, R, 0, 2 * np.pi)
            if fill:
                self.ctx.fill()

    def arms(
        self,
        r: float,
        delta: float = np.pi / 2,
        L: int | float = 10,
        theta: float = np.pi / 4,
        direction: Literal[-1, 1] = 1,
        spoke: bool = False,
        h: float = 0,
        down_only: bool = False,
        triangle: bool = False,
    ) -> None:
        vec = np.exp(-1j * theta)
        if direction == -1:
            vec = -np.conj(vec)

        up = L * vec
        down = np.conj(up)

        with RelCoords(self.ctx, self.origin, r, delta):
            if spoke:
                if direction == -1 and not down_only:
                    self.ctx.rel_move_to(-0.25, 0)
                    h -= 0.25
                self.ctx.rel_line_to(-h, 0)
                self.ctx.rel_line_to(h, 0)
                if direction == -1 and not down_only:
                    self.ctx.rel_move_to(0.25, 0)
            if down_only:
                self.ctx.rel_line_to(down.real, down.imag)
            elif triangle and direction == 1:
                self.ctx.rel_line_to(up.real, up.imag)
                self.ctx.rel_line_to(0, L * np.sqrt(2))
            elif triangle and direction == -1:
                self.ctx.rel_line_to(up.real, up.imag)
                self.ctx.rel_line_to(0, L * np.sqrt(2))
            else:
                self.ctx.rel_line_to(up.real, up.imag)
                self.ctx.rel_line_to(-up.real, -up.imag)
                self.ctx.rel_line_to(down.real, down.imag)
            self.ctx.close_path()

    def vbar(self, r: float, delta: float = np.pi / 2, L: float = 10) -> None:
        self.arms(r, delta, L / 2, np.pi / 2)

    def triangle(
        self,
        r: float,
        delta: float = np.pi / 2,
        L: float = 10,
        direction: Literal[-1, 1] = 1,
        spoke: bool = False,
        h: float = 0,
    ) -> None:
        self.arms(r, delta, L, direction=direction, spoke=spoke, h=h, triangle=True)

    def crescent(self, r: float, delta: float = np.pi / 2, s: int = 6) -> None:
        with RelCoords(self.ctx, self.origin, r, delta):
            self.ctx.rel_move_to(0, s / 2)
            self.ctx.rel_line_to(0, -s)
            self.ctx.rel_line_to(s, 0)
            self.ctx.rel_line_to(0, s)

            self.ctx.rel_line_to(0, -s)
            self.ctx.rel_line_to(-s, 0)
            self.ctx.close_path()
