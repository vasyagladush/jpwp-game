from typing import Generic, Optional, Sequence, Type, TypeVar, overload

Number = int | float
NumberType = TypeVar('NumberType', bound=Number)


class Vector(Generic[NumberType]):
    @overload
    def __init__(self, x: NumberType, y: NumberType, /) -> None: ...
    @overload
    def __init__(self, position: Sequence[NumberType], /) -> None: ...
    @overload
    def __init__(self, vector: 'Vector', /) -> None: ...

    def __init__(self, x_or_position_or_vector: NumberType | Sequence[NumberType] | 'Vector', y: Optional[NumberType] = None, /) -> None:
        if isinstance(x_or_position_or_vector, Number) and y is not None:
            self.x: NumberType = x_or_position_or_vector
            self.y: NumberType = y
        elif isinstance(x_or_position_or_vector, Sequence) and y is None:
            self.x = x_or_position_or_vector[0]
            self.y = x_or_position_or_vector[1]
        elif isinstance(x_or_position_or_vector, Vector) and y is None:
            self.x = x_or_position_or_vector.x
            self.y = x_or_position_or_vector.y
        else:
            raise TypeError(
                "Wrong arguments provided, see the constructor's overloads")

    def coordinates_to_list(self) -> list[NumberType]:
        return [self.x, self.y]

    def coordinates_to_tuple(self) -> tuple[NumberType, NumberType]:
        return (self.x, self.y)

    @overload
    def set_coordinates(self, x: NumberType, y: NumberType, /) -> 'Vector': ...

    @overload
    def set_coordinates(self, position: Sequence[NumberType], /) -> 'Vector':
        ...

    @overload
    def set_coordinates(self, vector: 'Vector', /) -> 'Vector': ...

    def set_coordinates(self, x_or_position_or_vector: NumberType | Sequence[NumberType] | 'Vector', y: Optional[NumberType] = None, /) -> 'Vector':
        if isinstance(x_or_position_or_vector, Number) and y is not None:
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

    def __mul__(self, other: NumberType) -> 'Vector':
        if isinstance(other, Number):
            return Vector((other * self.x, other * self.y))
        else:
            raise TypeError(
                "Unsupported operand type for *: 'Vector' and {type(other)}")

    def __rmul__(self, other) -> 'Vector':
        return self.__mul__(other)

    def __add__(self, other: 'Vector') -> 'Vector':
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(
                "Unsupported operand type for +: 'Vector' and {type(other)}")

    def __radd__(self, other: 'Vector') -> 'Vector':
        return self.__add__(other)


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
