from abc import ABC, abstractmethod
from typing import final
from Vector import Vector


class Renderable(ABC):
    def __init__(self, rendering_order: int) -> None:
        self.rendering_order: int = rendering_order

    # @staticmethod
    # @final
    # def get_rendering_order(el: 'Renderable') -> int:
    #     return el.rendering_order
    
    @abstractmethod
    def render(self, position: Vector) -> None:
        pass

