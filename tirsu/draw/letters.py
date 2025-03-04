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
        self.r2 = self.r1 + self.h_max
        self.delta = delta

    def write(self, vecs: list[complex], z0: complex = 0) -> None:
        self.draw(vecs, self.r1 + z0, self.delta)

    def beginning(self) -> None:
        self.i(-self.r1 / 1.5)

    def a(self, height: float = h_max) -> None:
        self.i(height)
        self.write(self.arms(direction=-1), height)

    def b(self) -> None:
        self.y()
        self.e(self.h_max - 8)

    def c(self, shift: float = 0) -> None:
        self.o(self.h_max + shift)
        self.e(self.h_max - 8 + shift)

    def d(self) -> None:
        self.a()
        self.e(self.h_max - 8)

    def e(self, height: float = h_max) -> None:
        self.i(height)
        self.write(self.vbar(), height)

    def f(self, height: float = h_max) -> None:
        self.e(height)
        self.e(height - 2)

    def g(self) -> None:
        self.o()
        self.f(self.h_max - 8)

    def h(self) -> None:
        self.a()
        self.f(self.h_max - 8)

    def i(self, height: float = h_max) -> None:
        self.write(self.spoke(height))

    def j(self, height: float = h_max, L: float = 10) -> None:
        vecs = self.spoke(height) + self.arms(L, direction=-1)[2:]
        self.write(vecs)

    def k(self, height: float = h_max, L: float = 10, dy: float = 3) -> None:
        self.j(height, L)
        self.j(height - dy, L)

    def l(self) -> None:  # noqa: E743
        self.i(self.h_max - 5 * 2**0.5)
        self.write(self.triangle(direction=-1), self.h_max)

    def m(self) -> None:
        self.l()
        self.e(self.h_max - 5 * 2**0.5 - 2)

    def n(self) -> None:
        self.l()
        self.f(self.h_max - 5 * 2**0.5 - 2)

    def o(self, height: float = h_max, spoke: bool = True) -> None:
        if spoke:
            self.i(height - 6)
        self.write(self.ellipse(), height)

    def p(self) -> None:
        self.a()
        self.j(self.h_max - 3)

    def q(self) -> None:  # noqa: E743
        height = self.h_max - 5 * 2**0.5
        self.i(height)
        self.write(self.triangle(), height)

    def r(self) -> None:
        self.y()
        self.f(self.h_max - 8)

    def s(self, shift: float = 0, L: float = 10) -> None:
        self.o(self.h_max + shift)
        self.j(self.h_max - 7.5 + shift, L)

    def t(self, shift: float = 0, L: float = 10, dy: float = 3) -> None:
        self.o(self.h_max + shift)
        self.k(self.h_max - 7.5 + shift, L, dy)

    def u(self, shift: float = 0) -> None:
        self.i(self.h_max - 6 + shift)
        self.write(self.ellipse(6, 5, -3 * np.pi / 2, -np.pi / 2), self.h_max + 5j + shift)

    def v(self) -> None:
        self.u()
        self.e(self.h_max - 7.5)

    def w(self) -> None:
        self.u()
        self.f(self.h_max - 7.5)

    def x(self) -> None:
        height = self.h_max - 6
        self.i(height)
        self.write(self.crescent(), height)

    def y(self) -> None:
        height = self.h_max - 7
        self.i(height)
        self.write(self.arms(), height)

    def z(self) -> None:
        self.x()
        self.e(self.h_max - 7.5)

    def ea(self) -> None:
        self.e(self.h_max + 0.25)
        self.a()

    def apostrophe(self) -> None:
        self.i(self.h_max - 9)
        self.write(self.ellipse(0.2, 0.2, t1=3 * np.pi), - 1.5)

    def oa(self) -> None:
        self.o()
        self.a(self.h_max - 7.5)

    def oi(self) -> None:
        height = self.h_max - 5 * 2**0.5
        self.o(height)
        self.write(self.arms(), height + 0.25)

    def ou(self) -> None:
        self.u(-7)
        self.o(self.h_max - 2, False)

    def ch(self) -> None:
        self.c(2 - 5 * 2**0.5)
        self.write(self.arms(direction=-1), self.h_max)

    def sh(self) -> None:
        self.s(2.5 - 5 * 2**0.5, 7)
        self.write(self.arms(direction=-1), self.h_max)

    def th(self) -> None:
        self.t(2.5 - 5 * 2**0.5, 7, 2.5)
        self.write(self.arms(direction=-1), self.h_max)

    def zh(self) -> None:
        self.x()
        self.f(self.h_max - 7.5)
