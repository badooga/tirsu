import cairo
import numpy as np

from .shapes import DrawShape

__all__ = ["DrawLetter"]

class DrawLetter(DrawShape):  # pylint: disable=too-many-public-methods
    h_max = 22

    def __init__(self, ctx: cairo.Context, o: complex, r1: float):
        super().__init__(ctx, o)
        self.r1 = r1
        self.r2 = r1 + self.h_max

    def beginning(self, delta) -> None:
        self.spoke(self.r1, delta, -self.h_max / 5)

    def a(self, delta) -> None:
        self.arms(self.r2, delta, direction=-1, spoke=True, h=self.h_max)

    def b(self, delta) -> None:
        self.y(delta)
        self.vbar(self.r2 - 8, delta)

    def c(self, delta, shift: float = 0) -> None:
        self.o(delta, shift)
        self.vbar(self.r2 - 8 + shift, delta)

    def d(self, delta) -> None:
        self.a(delta)
        self.vbar(self.r2 - 8, delta)

    def e(self, delta, shift: float = 0) -> None:
        self.spoke(self.r1, delta, self.h_max + shift)
        self.vbar(self.r2 + shift, delta)

    def f(self, delta, shift: float = 0) -> None:
        self.e(delta, shift)
        self.vbar(self.r2 + shift - 2, delta)

    def g(self, delta) -> None:
        self.c(delta)
        self.vbar(self.r2 - 8, delta)

    def h(self, delta) -> None:
        self.d(delta)
        self.vbar(self.r2 - 10, delta)

    def i(self, delta) -> None:
        self.spoke(self.r1, delta, self.h_max)

    def j(self, delta) -> None:
        self.arms(
            self.r2,
            delta,
            10,
            direction=-1,
            spoke=True,
            h=self.h_max,
            down_only=True,
        )

    def k(self, delta) -> None:
        self.j(delta)
        self.arms(self.r2 - 3, delta, 10, direction=-1, down_only=True)

    def l(self, delta) -> None:  # noqa: E743
        self.spoke(self.r1, delta, self.h_max - 5 * np.sqrt(2))
        self.triangle(self.r2, delta, direction=-1)

    def m(self, delta) -> None:
        self.l(delta)
        self.vbar(self.r2 - 2 - 5 * np.sqrt(2), delta)

    def n(self, delta) -> None:
        self.m(delta)
        self.vbar(self.r2 - 4 - 5 * np.sqrt(2), delta)

    def o(self, delta, shift: float = 0) -> None:
        self.spoke(self.r1, delta, self.h_max - 6.5 + shift)
        self.ellipse(self.r2 - 3 + shift, delta, 3, 5)

    def p(self, delta) -> None:
        self.a(delta)
        self.arms(self.r2 - 3, delta, 10, direction=-1, down_only=True)

    def q(self, delta) -> None:  # noqa: E743
        self.spoke(self.r1, delta, self.h_max - 5 * np.sqrt(2))
        self.triangle(self.r2 - 5 * np.sqrt(2), delta, direction=1)

    def r(self, delta) -> None:
        self.b(delta)
        self.vbar(self.r2 - 11, delta)

    def s(self, delta, shift: float = 0, L: float = 10) -> None:
        self.o(delta, shift)
        self.line(self.r2 + shift - 7.5, delta, L, 3 * np.pi / 4)

    def t(self, delta) -> None:
        self.s(delta)
        self.line(self.r2 - 10.5, delta, 10, 3 * np.pi / 4)

    def u(self, delta, shift: float = 0) -> None:
        self.spoke(self.r1, delta, self.h_max - 6 - shift)
        self.ellipse(self.r2 - shift, delta, 6, 5, -3 * np.pi / 2, -np.pi / 2)

    def v(self, delta) -> None:
        self.u(delta)
        self.vbar(self.r2 - 7.5, delta)

    def w(self, delta) -> None:
        self.v(delta)
        self.vbar(self.r2 - 9.5, delta)

    def x(self, delta) -> None:
        self.spoke(self.r1, delta, self.h_max - 6)
        self.crescent(self.r2 - 6, delta)

    def y(self, delta) -> None:
        self.arms(self.r2 - 7, delta, spoke=True, h=self.h_max - 7)

    def z(self, delta) -> None:
        self.x(delta)
        self.vbar(self.r2 - 7.5, delta)

    def ea(self, delta) -> None:
        self.e(self.r1 + 0.25, delta)
        self.a(delta)

    def apostrophe(self, delta) -> None:
        self.spoke(self.r1, delta, self.h_max - 9)
        self.ellipse(self.r1 - 1.5, delta, 0.2, 0.2)

    def oa(self, delta) -> None:
        self.o(delta)
        self.arms(self.r2 - 7.5, delta, direction=-1)

    def oi(self, delta) -> None:
        dr = 5 * np.sqrt(2)
        self.spoke(self.r1, delta, self.h_max - 6.5 - dr)
        self.ellipse(self.r2 - 3 - dr, delta, 3, 5)
        self.arms(self.r2 - dr + 0.25, delta)

    def ou(self, delta) -> None:
        dr = 1 + 6
        self.spoke(self.r1, delta, self.h_max - 6 - dr)
        self.ellipse(self.r2 - 7 + 3.5, delta, 3, 5)
        self.ellipse(self.r2 - dr, delta, 6, 5, -3 * np.pi / 2, -np.pi / 2)

    def ch(self, delta) -> None:
        dr = -2 + 5 * np.sqrt(2)
        self.spoke(self.r1, delta, self.h_max - 6.5 - dr)
        self.ellipse(self.r2 - 3 - dr, delta, 3, 5)
        self.vbar(self.r2 - 8 - dr, delta)
        self.arms(self.r2, delta, direction=-1)

    def sh(self, delta) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.o(delta, -dr)
        self.arms(self.r2, delta, direction=-1)
        self.line(self.r2 - 7.5 - dr, delta, 7, 3 * np.pi / 4)

    def th(self, delta) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.sh(delta)
        self.line(self.r2 - 10.5 - dr, delta, 7, 3 * np.pi / 4)

    def zh(self, delta) -> None:
        self.z(delta)
        self.vbar(self.r2 - 9.5, delta)
