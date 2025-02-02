import cairo
import numpy as np

from .shapes import DrawShape

__all__ = ["DrawLetter"]


class DrawLetter(DrawShape):  # pylint: disable=too-many-public-methods
    h_max = 22

    def __init__(
        self,
        ctx: cairo.Context,
        o: complex,
        r1: float,
        delta: float = 0,
    ) -> None:
        super().__init__(ctx, o)
        self.r1 = r1
        self.r2 = r1 + self.h_max
        self.delta = delta

    def beginning(self) -> None:
        self.spoke(self.r1, self.delta, -self.r1 / 1.5)

    def a(self) -> None:
        self.arms(self.r2, self.delta, direction=-1, spoke=True, h=self.h_max)

    def b(self) -> None:
        self.y()
        self.vbar(self.r2 - 8, self.delta)

    def c(self, shift: float = 0) -> None:
        self.o(shift)
        self.vbar(self.r2 - 8 + shift, self.delta)

    def d(self) -> None:
        self.a()
        self.vbar(self.r2 - 8, self.delta)

    def e(self, shift: float = 0) -> None:
        self.spoke(self.r1, self.delta, self.h_max + shift)
        self.vbar(self.r2 + shift, self.delta)

    def f(self, shift: float = 0) -> None:
        self.e(shift)
        self.vbar(self.r2 + shift - 2, self.delta)

    def g(self) -> None:
        self.c()
        self.vbar(self.r2 - 10, self.delta)

    def h(self) -> None:
        self.d()
        self.vbar(self.r2 - 10, self.delta)

    def i(self) -> None:
        self.spoke(self.r1, self.delta, self.h_max)

    def j(self) -> None:
        self.arms(
            self.r2,
            self.delta,
            10,
            direction=-1,
            spoke=True,
            h=self.h_max,
            down_only=True,
        )

    def k(self) -> None:
        self.j()
        self.arms(self.r2 - 3, self.delta, 10, direction=-1, down_only=True)

    def l(self) -> None:  # noqa: E743
        self.spoke(self.r1, self.delta, self.h_max - 5 * np.sqrt(2))
        self.triangle(self.r2, self.delta, direction=-1)

    def m(self) -> None:
        self.l()
        self.vbar(self.r2 - 2 - 5 * np.sqrt(2), self.delta)

    def n(self) -> None:
        self.m()
        self.vbar(self.r2 - 4 - 5 * np.sqrt(2), self.delta)

    def o(self, shift: float = 0) -> None:
        self.spoke(self.r1, self.delta, self.h_max - 6.5 + shift)
        self.ellipse(self.r2 - 3 + shift, self.delta, 3, 5)

    def p(self) -> None:
        self.a()
        self.arms(self.r2 - 3, self.delta, 10, direction=-1, down_only=True)

    def q(self) -> None:  # noqa: E743
        self.spoke(self.r1, self.delta, self.h_max - 5 * np.sqrt(2))
        self.triangle(self.r2 - 5 * np.sqrt(2), self.delta, direction=1)

    def r(self) -> None:
        self.b()
        self.vbar(self.r2 - 11, self.delta)

    def s(self, shift: float = 0, L: float = 10) -> None:
        self.o(shift)
        self.line(self.r2 + shift - 7.5, self.delta, L, 3 * np.pi / 4)

    def t(self) -> None:
        self.s()
        self.line(self.r2 - 10.5, self.delta, 10, 3 * np.pi / 4)

    def u(self, shift: float = 0) -> None:
        self.spoke(self.r1, self.delta, self.h_max - 6 + shift)
        self.ellipse(self.r2 + shift, self.delta, 6, 5, -3 * np.pi / 2, -np.pi / 2)

    def v(self) -> None:
        self.u()
        self.vbar(self.r2 - 7.5, self.delta)

    def w(self) -> None:
        self.v()
        self.vbar(self.r2 - 9.5, self.delta)

    def x(self) -> None:
        self.spoke(self.r1, self.delta, self.h_max - 6)
        self.crescent(self.r2 - 6, self.delta)

    def y(self) -> None:
        self.arms(self.r2 - 7, self.delta, spoke=True, h=self.h_max - 7)

    def z(self) -> None:
        self.x()
        self.vbar(self.r2 - 7.5, self.delta)

    def ea(self) -> None:
        self.e(0.25)
        self.a()

    def apostrophe(self) -> None:
        self.spoke(self.r1, self.delta, self.h_max - 9)
        self.ellipse(self.r1 - 1.5, self.delta, 0.2, 0.2, 0, 3 * np.pi)

    def oa(self) -> None:
        self.o()
        self.arms(self.r2 - 7.5, self.delta, direction=-1)

    def oi(self) -> None:
        dr = 5 * np.sqrt(2)
        self.spoke(self.r1, self.delta, self.h_max - 6.5 - dr)
        self.ellipse(self.r2 - 3 - dr, self.delta, 3, 5)
        self.arms(self.r2 - dr + 0.25, self.delta)

    def ou(self) -> None:
        self.u(-7)
        self.ellipse(self.r2 - 3.5, self.delta, 3, 5)

    def ch(self) -> None:
        dr = -2 + 5 * np.sqrt(2)
        self.spoke(self.r1, self.delta, self.h_max - 6.5 - dr)
        self.ellipse(self.r2 - 3 - dr, self.delta, 3, 5)
        self.vbar(self.r2 - 8 - dr, self.delta)
        self.arms(self.r2, self.delta, direction=-1)

    def sh(self) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.s(-dr, 7)
        self.arms(self.r2, self.delta, direction=-1)

    def th(self) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.sh()
        self.line(self.r2 - 10.5 - dr, self.delta, 7, 3 * np.pi / 4)

    def zh(self) -> None:
        self.z()
        self.vbar(self.r2 - 9.5, self.delta)
