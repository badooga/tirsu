import numpy as np

from .shapes import DrawShape


class DrawLetter(DrawShape):  # pylint: disable=too-many-public-methods
    h_max = 22

    def beginning(self, r, delta) -> None:
        self.spoke(r, -self.h_max/5, delta)

    def a(self, r, delta) -> None:
        self.arms(r + self.h_max, delta, direction=-1, spoke=True, h=self.h_max)

    def b(self, r, delta) -> None:
        self.y(r, delta)
        self.vbar(r + self.h_max - 8, delta)

    def c(self, r, delta) -> None:
        self.o(r, delta)
        self.vbar(r + self.h_max - 8, delta)

    def d(self, r, delta) -> None:
        self.a(r, delta)
        self.vbar(r + self.h_max - 8, delta)

    def e(self, r, delta) -> None:
        self.i(r, delta)
        self.vbar(r + self.h_max, delta)

    def f(self, r, delta) -> None:
        self.e(r, delta)
        self.vbar(r + self.h_max - 2, delta)

    def g(self, r, delta) -> None:
        self.c(r, delta)
        self.vbar(r + self.h_max - 8, delta)

    def h(self, r, delta) -> None:
        self.d(r, delta)
        self.vbar(r + self.h_max - 10, delta)

    def i(self, r, delta) -> None:
        self.spoke(r, self.h_max, delta)

    def j(self, r, delta) -> None:
        self.arms(
            r + self.h_max,
            delta,
            10,
            direction=-1,
            spoke=True,
            h=self.h_max,
            down_only=True,
        )

    def k(self, r, delta) -> None:
        self.j(r, delta)
        self.arms(r + self.h_max - 3, delta, 10, direction=-1, down_only=True)

    def l(self, r, delta) -> None:  # noqa: E743
        self.spoke(r, self.h_max - 5 * np.sqrt(2), delta)
        self.triangle(r + self.h_max, delta, direction=-1)

    def m(self, r, delta) -> None:
        self.l(r, delta)
        self.vbar(r + self.h_max - 2 - 5 * np.sqrt(2), delta)

    def n(self, r, delta) -> None:
        self.m(r, delta)
        self.vbar(r + self.h_max - 4 - 5 * np.sqrt(2), delta)

    def o(self, r, delta) -> None:
        self.spoke(r, self.h_max - 6.5, delta)
        self.ellipse(r + self.h_max - 6.5 + 3.5, delta, 3, 5)

    def p(self, r, delta) -> None:
        self.a(r, delta)
        self.arms(r + self.h_max - 3, delta, 10, direction=-1, down_only=True)

    def q(self, r, delta) -> None:  # noqa: E743
        self.spoke(r, self.h_max - 5 * np.sqrt(2), delta)
        self.triangle(r + self.h_max - 5 * np.sqrt(2), delta, direction=1)

    def r(self, r, delta) -> None:
        self.b(r, delta)
        self.vbar(r + self.h_max - 11, delta)

    def s(self, r, delta) -> None:
        self.o(r, delta)
        self.line(r + self.h_max - 7.5, delta, 10, 3 * np.pi / 4)

    def t(self, r, delta) -> None:
        self.s(r, delta)
        self.line(r + self.h_max - 10.5, delta, 10, 3 * np.pi / 4)

    def u(self, r, delta) -> None:
        self.spoke(r, self.h_max - 6, delta)
        self.ellipse(r + self.h_max, delta, 6, 5, -3 * np.pi / 2, -np.pi / 2)

    def v(self, r, delta) -> None:
        self.u(r, delta)
        self.vbar(r + self.h_max - 7.5, delta)

    def w(self, r, delta) -> None:
        self.v(r, delta)
        self.vbar(r + self.h_max - 9.5, delta)

    def x(self, r, delta) -> None:
        self.spoke(r, self.h_max - 6, delta)
        self.crescent(r + self.h_max - 6, delta)

    def y(self, r, delta) -> None:
        self.arms(r + self.h_max - 7, delta, spoke=True, h=self.h_max - 7)

    def z(self, r, delta) -> None:
        self.x(r, delta)
        self.vbar(r + self.h_max - 7.5, delta)

    def ea(self, r, delta) -> None:
        self.e(r + 0.25, delta)
        self.a(r, delta)

    def apostrophe(self, r, delta) -> None:
        self.spoke(r, self.h_max - 9, delta)
        self.ellipse(r - 1.5, delta, 0.2, 0.2)

    def oa(self, r, delta) -> None:
        self.o(r, delta)
        self.arms(r + self.h_max - 7.5, delta, direction=-1)

    def oi(self, r, delta) -> None:
        dr = 5 * np.sqrt(2)
        self.spoke(r, self.h_max - 6.5 - dr, delta)
        self.ellipse(r + self.h_max - 3 - dr, delta, 3, 5)
        self.arms(r + self.h_max - dr + 0.25, delta)

    def ou(self, r, delta) -> None:
        dr = 1 + 6
        self.spoke(r, self.h_max - 6 - dr, delta)
        self.ellipse(r + self.h_max - 7 + 3.5, delta, 3, 5)
        self.ellipse(r + self.h_max - dr, delta, 6, 5, -3 * np.pi / 2, -np.pi / 2)

    def ch(self, r, delta) -> None:
        dr = -2 + 5 * np.sqrt(2)
        self.spoke(r, self.h_max - 6.5 - dr, delta)
        self.ellipse(r + self.h_max - 3 - dr, delta, 3, 5)
        self.vbar(r + self.h_max - 8 - dr, delta)
        self.arms(r + self.h_max, delta, direction=-1)

    def sh(self, r, delta) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.spoke(r, self.h_max - 6.5 - dr, delta)
        self.ellipse(r + self.h_max - 3 - dr, delta, 3, 5)
        self.arms(r + self.h_max, delta, direction=-1)
        self.line(r + self.h_max - 7.5 - dr, delta, 7, 3 * np.pi / 4)

    def th(self, r, delta) -> None:
        dr = -2.5 + 5 * np.sqrt(2)
        self.sh(r, delta)
        self.line(r + self.h_max - 10.5 - dr, delta, 7, 3 * np.pi / 4)

    def zh(self, r, delta) -> None:
        self.z(r, delta)
        self.vbar(r + self.h_max - 9.5, delta)
