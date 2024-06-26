from abc import ABC, abstractmethod
from enum import Enum, auto
from functools import wraps
from typing import Callable, Dict, Generic, Optional, TypeVar, final
from Vector import Vector
from RenderingController import RenderingController
from utils.EventEmitter import EventEmitter

RenderingControllerType = TypeVar(
    'RenderingControllerType', bound=RenderingController)


class ActorEventType(Enum):
    SIZE_CHANGED = auto()
    ANGLE_CHANGED = auto()
    FLIPPED = auto(),
    POSITION_CHANGED = auto()


class Actor(Generic[RenderingControllerType], EventEmitter[ActorEventType]):

    def __init__(self, position: Vector, rendering_controller: RenderingControllerType, z_index: int) -> None:
        super().__init__(ActorEventType)
        self._position: Vector = position
        self.rendering_controller: RenderingControllerType = rendering_controller
        self.z_index: int = z_index
        self.components: list[ActorComponent] = []

        # TODO: add transform class that will hold position, rotation and maybe flip?, maybe scale?
        # TODO: use those in class __init__
        # TODO: check that private fields are not accessed where they should not be
        # TODO: check if we could load images only once (as a class property) instead of loading it every time a new instance is constructed
        # TODO: add a guide on how to use the code with python3.11 or less if someone has problems installing python3.12

    def get_position(self):
        return Vector(self._position)

    @EventEmitter.emits(ActorEventType.POSITION_CHANGED)
    def set_position(self, position: Vector):
        self._position = position

    # Tick method
    def tick(self) -> None:
        for component in self.components:
            component.tick()

    # Utility method
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
            return self.rendering_controller.render(position)
        return self.rendering_controller.render(self._position)

    @EventEmitter.emits(ActorEventType.SIZE_CHANGED)
    def set_size(self, size: Vector) -> None:
        self.rendering_controller.set_size(size)
        # TODO: add physical collision box set_size here

    @EventEmitter.emits(ActorEventType.ANGLE_CHANGED)
    def set_angle(self, angle: int) -> None:
        self.rendering_controller.set_angle(angle)
        # TODO: add physical collision box set_angle here

    @EventEmitter.emits(ActorEventType.FLIPPED)
    def flip(self, x: bool, y: bool) -> None:
        self.rendering_controller.flip(x, y)


class Actor_TilemapCompatible(Actor, ABC):
    """An abstract class that represents an actor that can be used for a tilemap.
    """
    @abstractmethod
    def __init__(self, position: Vector, z_index: int) -> None:
        pass


ActorComponentOwnerType = TypeVar('ActorComponentOwnerType', bound=Actor)
class ActorComponent(Generic[ActorComponentOwnerType], ABC):
    def __init__(self, owned_by: ActorComponentOwnerType) -> None:
        self.owned_by: ActorComponentOwnerType = owned_by

    @abstractmethod
    def tick(self) -> None:
        pass


# ActorComponentOwner = TypeVar('ActorComponentOwner', bound=Actor)


# class ActorComponent(Generic[ActorComponentOwner], ABC):
#     def __init__(self, owned_by: ActorComponentOwner) -> None:
#         self.owned_by: ActorComponentOwner | Actor = owned_by
#         self.owned_by.add_event_subscription(
#             Actor.Event.SIZE_CHANGED, self.tick)

#     @abstractmethod
#     def tick(self) -> None:
#         pass
