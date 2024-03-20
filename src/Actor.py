from typing import Optional, override
import pygame
from Renderable import Renderable
from Vector import Vector


class Actor(Renderable):
    def __init__(self, position: Vector, image: pygame.Surface, rendering_order: int) -> None:
        super().__init__(image, rendering_order)
        self.position: Vector = position

    def tick(self) -> None:
        print("Actor tick")

    @override
    def render(self, position: Optional[Vector] = None) -> None:
        if position is not None:
            return super().render(position)
        return super().render(self.position)
