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
        """A function to render the actor on the singleton Display object.
        If a position is passed in, it will render the actor at that position.
        Otherwise, it will render the actor at the position of the actor.

        Args:
            ``position (Optional[Vector], optional)``: position to render actor at (instead of actor's object position). Defaults to ``None``.

        Returns:
            ``None``
        """
        if position is not None:
            return super().render(position)
        return super().render(self.position)
