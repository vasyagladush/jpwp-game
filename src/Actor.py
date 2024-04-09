from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, final, override
import pygame
from Vector import Vector
from components.rendering.RenderingComponent import RenderingComponent


class Actor():
    def __init__(self, position: Vector, rendering_component: RenderingComponent, z_index: int) -> None:
        self.position: Vector = position
        self.rendering_component: RenderingComponent = rendering_component
        self.z_index: int = z_index
        self.components: list[ActorComponent] = []
        #TODO: add transform class that will hold position, rotation and maybe flip?, maybe scale?
        #TODO: use those in class __init__
        #TODO: maybe rename rendering_component to something else, maybe it's not even a component
        #TODO: if needed, add Component class that will be able to subscribe to events of its owner like transformChange
        #TODO: optimize, check for necessarry del statements
        #TODO: check that private fields are not accessed where they should not be
        #TODO: check if we could load images only once (as a class property) instead of loading it every time a new instance is constructed
        #TODO: camera (a smaller window is a camera that only shows what's inside its borders, a bigger window is where objects are rendered, add level camera borders)
        #TODO: handle different screen resolutions, resizing maybe too 
        #TODO: add a guide on how to use the code with python3.11 or less if someone has problems installing python3.12

    def tick(self) -> None:
        for component in self.components:
            component.tick()

    @final
    @staticmethod
    def get_actor_z_index(el: 'Actor') -> int:
        return el.z_index

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
    
    def set_size(self, size: Vector) -> None:
        self.rendering_component.set_size(size)
        #TODO: add physical collision box set_size here

    def set_angle(self, angle: int) -> None:
        self.rendering_component.set_angle(angle)
        #TODO: add physical collision box set_angle here

    def flip(self, x: bool, y: bool) -> None:
        self.rendering_component.flip(x, y)


class Actor_TilemapCompatible(Actor, ABC):
    """An abstract class that represents an actor that can be used for a tilemap.
    """
    @abstractmethod
    def __init__(self, position: Vector, z_index: int) -> None:
        pass


class ActorComponent(ABC):
    def __init__(self, owned_by: Actor) -> None:
        self.owned_by: Actor = owned_by
    @abstractmethod
    def tick(self) -> None:
        pass