# Number = int | float
# NumberType = TypeVar('NumberType', int, float)

from typing import Type, TypeVar, Union

def constrain_int(num: int, min: int, max: int) -> int:
    if num < min:
        return min
    elif num > max:
        return max
    else:
        return num

# def convert_number(value: Union[int, float], to_type: Type[NumberType]) -> NumberType:
#     """
#     Converts a number to the specified type.

#     Args:
#         value: The number to convert.
#         to_type: The type to convert the number to (either int or float).

#     Returns:
#         The converted number.

#     Raises:
#         TypeError: If the value is not a number (int or float).
#     """
#     if not isinstance(value, (int, float)):
#         raise TypeError("Value must be either int or float")
    
#     return to_type(value)