from typing import TypeVar
import pygame
from Actor import Actor, ActorComponent
from Clock import Clock
from Vector import Vector

ActorComponentOwnerType = TypeVar('ActorComponentOwnerType', bound=Actor)


class MovementComponent(ActorComponent[ActorComponentOwnerType]):
    def __init__(self, owned_by: ActorComponentOwnerType, movement_speed: int = 300, gravity_enabled: bool = False, gravity_acceleration: int = 500, max_fall_speed: int = 500):
        """_summary_

        Args:
            owned_by (_type_): _description_
            movement_speed (int, optional): _description_. Defaults to 300.
            gravity_enabled (bool, optional): _description_. Defaults to False.
            gravity_acceleration (int, optional): _description_. Defaults to 300.
            max_fall_speed (int, optional): _description_. Defaults to 300.
        """
        super().__init__(owned_by)

        self.movement_speed: int = movement_speed
        self.velocity: Vector = Vector(0, 0)

        self.gravity_enabled: bool = gravity_enabled
        self.gravity_acceleration: int = gravity_acceleration
        self.max_fall_speed: int = max_fall_speed

    def set_direction(self, direction: Vector) -> None:
        self.velocity = self.movement_speed * direction.get_direction()

    def set_x_direction(self, direction: int) -> None:
        """_summary_

        Args:
            direction (float): > 0 for right, < 0 for left
        """
        constrained_direction: int = 0

        if direction > 0:
            constrained_direction = 1
        elif direction < 0:
            constrained_direction = -1
        self.velocity.x = self.movement_speed * constrained_direction

    def apply_gravity(self) -> None:
        self.velocity.y = min(
            self.velocity.y + self.gravity_acceleration * (
                Clock().get_delta_time() / 1000), self.max_fall_speed)

    def tick(self) -> None:
        if (self.gravity_enabled):
            self.apply_gravity()
        if not self.velocity.equals(Vector.ZeroVector()):
            moved: Vector = self.velocity * (
                Clock().get_delta_time() / 1000)
            self.owned_by.set_position(
                Vector(self.owned_by.get_position() + moved)
            )
