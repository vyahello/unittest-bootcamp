from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstraction of a shape."""

    @abstractmethod
    def perimeter(self) -> int:
        pass

    @abstractmethod
    def area(self) -> float:
        pass


class Triangle(Shape):
    """Represent a triangle object."""

    def __init__(self, side1: int, side2: int, side3: int, height: int) -> None:
        self._side1: int = side1
        self._side2: int = side2
        self._side3: int = side3
        self._height: int = height

    def perimeter(self) -> int:
        """Equal to sum of all triangle sides like side1 + side2 + side3."""

        return self._side1 + self._side2 + self._side3

    def area(self) -> float:
        """Equal to height * base_side / 2."""

        return self._height * self._side2 / 2


class Square(Shape):
    """Represent a square object."""

    def __init__(self, side: int) -> None:
        self._side: int = side

    def perimeter(self) -> int:
        """Equal to 4 * side."""

        return 4 * self._side

    def area(self) -> int:
        """Equal to square_side ** 2 """

        return self._side ** 2


class Rectangle(Shape):
    """Represent a rectangle object."""

    def __init__(self, length: int, width: int) -> None:
        self._length: int = length
        self._width: int = width

    def perimeter(self) -> int:
        """Equal to 2 * (length + width)."""

        return 2 * (self._length + self._width)

    def area(self) -> int:
        """Equal to length * width."""

        return self._length * self._width
