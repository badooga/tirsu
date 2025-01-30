import numpy as np
from numpy.typing import NDArray

__all__ = ["Grid"]


class Grid:
    def __init__(self, count: int, radius: float, padding: float | None = None) -> None:
        if padding is None:
            padding = 0.5 * radius

        self.count = count
        self.radius = radius
        self.padding = padding

    @property
    def s(self) -> int:
        return int(np.ceil(self.count**0.5))**2

    @property
    def spacing(self) -> float:
        return self.radius + 2 * self.padding

    @property
    def centers(self) -> NDArray[np.complex128]:
        x, y = np.arange(self.s), np.arange(self.s)
        X, Y = np.meshgrid(x, y)

        grid = X + 1j * Y
        grid += (1 + 1j) / 2
        grid = grid * self.spacing

        return grid.ravel()[: self.count]

    @property
    def length(self):
        return self.s * self.spacing
