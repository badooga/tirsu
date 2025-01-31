import numpy as np
from numpy.typing import NDArray

__all__ = ["Grid"]


class Grid:
    def __init__(
        self, nx: int, ny: int, radius: float, padding: float | None = None, scale: float = 1,
    ) -> None:
        if padding is None:
            padding = 0.5 * radius

        self.nx = nx
        self.ny = ny
        self.radius = radius
        self.padding = padding
        self.scale = scale

    @property
    def units(self) -> float:
        return self.radius + 2 * self.padding

    @property
    def x(self) -> float:
        return self.nx * self.units * self.scale

    @property
    def y(self) -> float:
        return self.ny * self.units * self.scale

    @property
    def centers(self) -> NDArray[np.complex128]:
        ax, ay = np.arange(self.nx), np.arange(self.ny)
        AX, AY = np.meshgrid(ax, ay)

        grid = AX + 1j * AY
        grid += (1 + 1j) / 2
        grid *= self.units

        return grid * self.scale
