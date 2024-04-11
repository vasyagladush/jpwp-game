from typing import Generic, TypeVar


T = TypeVar('T')

class Pointer(Generic[T]):
    def __init__(self, ref_to_obj: T) -> None:
        self.holded_ref: T = ref_to_obj

