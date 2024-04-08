from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, final, override
import pygame
from Animation import Animation
from Vector import Vector
from components.rendering.RenderingComponent import RenderingComponent


class Actor():
    def __init__(self, position: Vector, rendering_component: RenderingComponent) -> None:
        self.rendering_component: RenderingComponent = rendering_component
        self.position: Vector = position

    def tick(self) -> None:
        print("Actor tick")

    @final
    @staticmethod
    def get_actor_rendering_order(el: 'Actor') -> int:
        return el.rendering_component.rendering_order

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
            return self.rendering_component.render(position)
        return self.rendering_component.render(self.position)


class Actor_TilemapCompatible(Actor, ABC):
    """An abstract class that represents an actor that can be used for a tilemap.
    """
    @abstractmethod
    def __init__(self, position: Vector, rendering_order: int) -> None:
        pass
