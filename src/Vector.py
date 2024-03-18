from typing import Optional, Sequence, overload


class Vector:
    @overload
    def __init__(self, x: int, y: int, /) -> None: ...
    @overload
    def __init__(self, position: Sequence[int], /) -> None: ...

    def __init__(self, x_or_position: int | Sequence[int], y: Optional[int] = None, /) -> None:
        if isinstance(x_or_position, int) and y is not None:
            self.x: int = x_or_position
            self.y: int = y
        elif isinstance(x_or_position, Sequence) and y is None:
            self.x = x_or_position[0]
            self.y = x_or_position[1]
        else:
            raise TypeError("Wrong arguments provided, see the constructor's overloads")

    def coordinates_to_list(self) -> list[int]:
        return [self.x, self.y]
    
    def coordinates_to_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
    
    @overload
    def set_coordinates(self, x: int, y: int, /) -> 'Vector': ...
    @overload
    def set_coordinates(self, position: Sequence[int], /) -> 'Vector': ...

    def set_coordinates(self, x_or_position: int | Sequence[int], y: Optional[int] = None, /) -> 'Vector':
        if isinstance(x_or_position, int) and y is not None:
            self.x = x_or_position
            self.y = y
        elif isinstance(x_or_position, Sequence) and y is None:
            self.x = x_or_position[0]
            self.y = x_or_position[1]
        else:
            raise TypeError("Wrong arguments provided, see the method's overloads")
        return self
    

#Tests
if __name__ == "__main__":
    p = Vector(3, 5)
    p.set_coordinates(4, 6)
    p.set_coordinates([4, 6])
    p.set_coordinates((5, 7))
    # p.set_coordinates((5, 7), 3)
    print(p.x, p.y)


# TODO: clean this up
# # from typing import TypeAlias

# # Position: TypeAlias = list[int]

# class Position:
#     def __init__(self, x: int, y: int):
#         self.x: int = x
#         self.y: int = y

#     def __iter__(self):
#         return self
    
#        def __next__(self):
#         if self.current >= self.length:
#             raise StopIteration

#         self.current += 1
#         return self.current ** 2

#     def __getitem__(self, key: int, value: int) -> int:
#         if key == 0:
#             return self.x
#         elif key == 1:
#             return self.y
#         else:
#             raise IndexError()

#     def __setitem__(self, key: int, value: int):
#         if key == 0:
#             self.x = value
#         elif key == 1:
#             self.y = value
#         else:
#             raise IndexError()