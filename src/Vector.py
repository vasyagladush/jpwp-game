import math
from typing import Optional, Sequence, overload


class Vector:
    @overload
    def __init__(self, x: float, y: float, /) -> None: ...
    @overload
    def __init__(self, position: Sequence, /) -> None: ...
    @overload
    def __init__(self, vector: 'Vector', /) -> None: ...

    def __init__(self, x_or_position_or_vector: float | Sequence | 'Vector', y: Optional[float] = None, /) -> None:
        if isinstance(x_or_position_or_vector, int | float) and y is not None:
            self.x: float = x_or_position_or_vector
            self.y: float = y
        elif isinstance(x_or_position_or_vector, Sequence) and y is None:
            self.x = x_or_position_or_vector[0]
            self.y = x_or_position_or_vector[1]
        elif isinstance(x_or_position_or_vector, Vector) and y is None:
            self.x = x_or_position_or_vector.x
            self.y = x_or_position_or_vector.y
        else:
            raise TypeError(
                "Wrong arguments provided, see the constructor's overloads")

    def coordinates_to_list(self) -> list[float]:
        return [self.x, self.y]

    def coordinates_to_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def coordinates_to_int_list(self) -> list[int]:
        return [int(self.x), int(self.y)]

    def coordinates_to_int_tuple(self) -> tuple[int, int]:
        return (int(self.x), int(self.y))

    @overload
    def set_coordinates(self, x: float, y: float, /) -> 'Vector':
        ...

    @overload
    def set_coordinates(self, position: Sequence, /) -> 'Vector':
        ...

    @overload
    def set_coordinates(self, vector: 'Vector', /) -> 'Vector':
        ...

    def set_coordinates(self, x_or_position_or_vector: float | Sequence | 'Vector', y: Optional[float] = None, /) -> 'Vector':
        if isinstance(x_or_position_or_vector, int | float) and y is not None:
            self.x = x_or_position_or_vector
            self.y = y
        elif isinstance(x_or_position_or_vector, Sequence) and y is None:
            self.x = x_or_position_or_vector[0]
            self.y = x_or_position_or_vector[1]
        elif isinstance(x_or_position_or_vector, Vector) and y is None:
            self.x = x_or_position_or_vector.x
            self.y = x_or_position_or_vector.y
        else:
            raise TypeError(
                "Wrong arguments provided, see the method's overloads")
        return self

    def get_direction(self) -> 'Vector':
        magnitude: float = math.sqrt(self.x**2 + self.y**2)
        if magnitude == 0:
            return Vector(0, 0)
        direction_x: float = self.x / magnitude
        direction_y: float = self.y / magnitude
        return Vector(direction_x, direction_y)

    def equals(self, other: 'Vector') -> bool:
        """Cheecks if self's and other's coordinates are equal

        Returns:
            bool: True, if coordinates are equal, False - otherwise
        """
        return self.x == other.x and self.y == other.y

    @staticmethod
    def ZeroVector() -> 'Vector':
        """
        Returns:
            Vector: a new instance of Vector with x and y set to 0
        """
        return Vector(0, 0)

    def __mul__(self, other: 'float | Vector') -> 'Vector':
        if isinstance(other, int | float):
            return Vector((other * self.x, other * self.y))
        elif isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            raise TypeError(
                "Unsupported operand type for *: 'Vector' and {type(other)}")

    def __imul__(self, other: 'float | Vector') -> 'Vector':
        if isinstance(other, int | float):
            self.x *= other
            self.y *= other
            return self
        elif isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError(
                "Unsupported operand type for +=: 'Vector' and {type(other)}")

    def __rmul__(self, other: 'float | Vector') -> 'Vector':
        return self.__mul__(other)

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(
                "Unsupported operand type for +: 'Vector' and {type(other)}")

    def __radd__(self, other: 'Vector') -> 'Vector':
        return self.__add__(other)

    def __sub__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(
                "Unsupported operand type for -: 'Vector' and {type(other)}")

    def __rsub__(self, other: 'Vector') -> 'Vector':
        return self.__sub__(other)

    def __iadd__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        else:
            raise TypeError(
                "Unsupported operand type for +=: 'Vector' and {type(other)}")

    def __isub__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            return self
        else:
            raise TypeError(
                "Unsupported operand type for -=: 'Vector' and {type(other)}")
