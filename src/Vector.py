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

    def direction(self) -> 'Vector':
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

    # def __truediv__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
    #     if isinstance(other, Number) and other != 0:
    #         other: NumberType = convert_number(other, type(self.x))
    #         return Vector[NumberType](self.x / other, self.y / other)
    #     elif isinstance(other, Vector) and other.x != 0 and other.y != 0:
    #         return Vector[NumberType](self.x / other.x, self.y / other.y)
    #     else:
    #         raise ValueError("Division by zero or unsupported operand type")

    # def __itruediv__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
    #     if isinstance(other, Number) and other != 0:
    #         t = type(self.x)
    #         self.x = self.x / convert_number(other, t)
    #         self.y = self.y / convert_number(other, t)
    #         return self
    #     elfi
    #     else:
    #         raise ValueError("Division by zero or unsupported operand type")


# Tests
if __name__ == "__main__":
    p = Vector(3, 5)
    p.set_coordinates(4, 6)
    p.set_coordinates([4, 6])
    p.set_coordinates((5, 7))
    # p.set_coordinates((5, 7), 3)
    print(p.x, p.y)


# TODO: clean this up
# # from typing import TypeAlias

# # Position: TypeAlias = list[NumberType]

# class Position:
#     def __init__(self, x: NumberType, y: NumberType):
#         self.x: NumberType = x
#         self.y: NumberType = y

#     def __iter__(self):
#         return self

#        def __next__(self):
#         if self.current >= self.length:
#             raise StopIteration

#         self.current += 1
#         return self.current ** 2

#     def __getitem__(self, key: NumberType, value: NumberType) -> NumberType:
#         if key == 0:
#             return self.x
#         elif key == 1:
#             return self.y
#         else:
#             raise IndexError()

#     def __setitem__(self, key: NumberType, value: NumberType):
#         if key == 0:
#             self.x = value
#         elif key == 1:
#             self.y = value
#         else:
#             raise IndexError()




# import math
# from typing import Generic, Optional, Sequence, Type, TypeVar, cast, overload

# from utils.MathUtil import Number, NumberType, convert_number


# class Vector(Generic[NumberType]):
#     @overload
#     def __init__(self, x: NumberType, y: NumberType, /) -> None: ...
#     @overload
#     def __init__(self, position: Sequence[NumberType], /) -> None: ...
#     @overload
#     def __init__(self, vector: 'Vector', /) -> None: ...

#     def __init__(self, x_or_position_or_vector: NumberType | Sequence[NumberType] | 'Vector[NumberType]', y: Optional[NumberType] = None, /) -> None:
#         if isinstance(x_or_position_or_vector, Number) and y is not None:
#             self.x: NumberType = x_or_position_or_vector
#             self.y: NumberType = y
#         elif isinstance(x_or_position_or_vector, Sequence) and y is None:
#             self.x = x_or_position_or_vector[0]
#             self.y = x_or_position_or_vector[1]
#         elif isinstance(x_or_position_or_vector, Vector) and y is None:
#             self.x = x_or_position_or_vector.x
#             self.y = x_or_position_or_vector.y
#         else:
#             raise TypeError(
#                 "Wrong arguments provided, see the constructor's overloads")

#     def coordinates_to_list(self) -> list[NumberType]:
#         return [self.x, self.y]

#     def coordinates_to_tuple(self) -> tuple[NumberType, NumberType]:
#         return (self.x, self.y)

#     @overload
#     def set_coordinates(self, x: NumberType, y: NumberType, /) -> 'Vector[NumberType]':
#         ...

#     @overload
#     def set_coordinates(self, position: Sequence[NumberType], /) -> 'Vector[NumberType]':
#         ...

#     @overload
#     def set_coordinates(self, vector: 'Vector[NumberType]', /) -> 'Vector[NumberType]':
#         ...

#     def set_coordinates(self, x_or_position_or_vector: NumberType | Sequence[NumberType] | 'Vector[NumberType]', y: Optional[NumberType] = None, /) -> 'Vector[NumberType]':
#         if isinstance(x_or_position_or_vector, Number) and y is not None:
#             self.x = x_or_position_or_vector
#             self.y = y
#         elif isinstance(x_or_position_or_vector, Sequence) and y is None:
#             self.x = x_or_position_or_vector[0]
#             self.y = x_or_position_or_vector[1]
#         elif isinstance(x_or_position_or_vector, Vector) and y is None:
#             self.x = x_or_position_or_vector.x
#             self.y = x_or_position_or_vector.y
#         else:
#             raise TypeError(
#                 "Wrong arguments provided, see the method's overloads")
#         return self

#     def direction(self) -> 'Vector[float]':
#         magnitude: Number = math.sqrt(self.x**2 + self.y**2)
#         if magnitude == 0:
#             return Vector(0, 0)
#         direction_x: float = self.x / magnitude
#         direction_y: float = self.y / magnitude
#         return Vector[float](direction_x, direction_y)

#     def equals(self, other: 'Vector[NumberType]') -> bool:
#         """Cheecks if self's and other's coordinates are equal

#         Returns:
#             bool: True, if coordinates are equal, False - otherwise
#         """
#         return self.x == other.x and self.y == other.y

#     @staticmethod
#     def ZeroVector() -> 'Vector[int]':
#         """
#         Returns:
#             Vector: a new instance of Vector with x and y set to 0
#         """
#         return Vector[int](0, 0)

#     def __mul__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Number):
#             other: NumberType = convert_number(other, type(self.x))
#             return Vector[NumberType]((other * self.x, other * self.y))
#         elif isinstance(other, Vector):
#             t = type(self.x)
#             return Vector[NumberType](self.x * convert_number(other.x, t), self.y * convert_number(other.y, t))
#         else:
#             raise TypeError(
#                 "Unsupported operand type for *: 'Vector' and {type(other)}")

#     def __imul__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Number):
#             other: NumberType = convert_number(other, type(self.x))
#             self.x *= other
#             self.y *= other
#             return self
#         elif isinstance(other, Vector):
#             t = type(self.x)
#             self.x += convert_number(other.x, t)
#             self.y += convert_number(other.y, t)
#             return self
#         else:
#             raise TypeError(
#                 "Unsupported operand type for +=: 'Vector' and {type(other)}")

#     def __rmul__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
#         return self.__mul__(other)

#     def __add__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Vector):
#             t = type(self.x)
#             return Vector[NumberType](self.x + convert_number(other.x, t), self.y + convert_number(other.y, t))
#         else:
#             raise TypeError(
#                 "Unsupported operand type for +: 'Vector' and {type(other)}")

#     def __radd__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         return self.__add__(other)

#     def __sub__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Vector):
#             t = type(self.x)
#             return Vector[NumberType](self.x - convert_number(other.x, t), self.y - convert_number(other.y, t))
#         else:
#             raise TypeError(
#                 "Unsupported operand type for -: 'Vector' and {type(other)}")

#     def __rsub__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         return self.__sub__(other)

#     def __iadd__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Vector):
#             t = type(self.x)
#             self.x += convert_number(other.x, t)
#             self.y += convert_number(other.y, t)
#             return self
#         else:
#             raise TypeError(
#                 "Unsupported operand type for +=: 'Vector' and {type(other)}")

#     def __isub__(self, other: 'Vector[Number]') -> 'Vector[NumberType]':
#         if isinstance(other, Vector):
#             t = type(self.x)
#             self.x -= convert_number(other.x, t)
#             self.y -= convert_number(other.y, t)
#             return self
#         else:
#             raise TypeError(
#                 "Unsupported operand type for -=: 'Vector' and {type(other)}")

    # def __truediv__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
    #     if isinstance(other, Number) and other != 0:
    #         other: NumberType = convert_number(other, type(self.x))
    #         return Vector[NumberType](self.x / other, self.y / other)
    #     elif isinstance(other, Vector) and other.x != 0 and other.y != 0:
    #         return Vector[NumberType](self.x / other.x, self.y / other.y)
    #     else:
    #         raise ValueError("Division by zero or unsupported operand type")

    # def __itruediv__(self, other: 'Number | Vector[Number]') -> 'Vector[NumberType]':
    #     if isinstance(other, Number) and other != 0:
    #         t = type(self.x)
    #         self.x = self.x / convert_number(other, t)
    #         self.y = self.y / convert_number(other, t)
    #         return self
    #     elfi
    #     else:
    #         raise ValueError("Division by zero or unsupported operand type")

