import pygame
from Actor import Actor, ActorComponent
from Clock import Clock
from Vector import Vector


class MovementComponent(ActorComponent[Actor]):
    def __init__(self, owned_by, movement_speed: int = 300):
        """_summary_

        Args:
            owned_by (_type_): _description_
            speed (int, optional): [pixels/second]. Defaults to 300.
        """
        super().__init__(owned_by)
        self.movement_speed: int = movement_speed
        self.velocity: Vector = Vector(0, 0)

    def set_direction(self, direction: Vector) -> None:
        self.velocity = self.movement_speed * direction.get_direction()

    def tick(self) -> None:
        if not self.velocity.equals(Vector.ZeroVector()):
            moved: Vector = (
                Clock().get_delta_time() / 1000) * self.velocity
            self.owned_by.position.set_coordinates(
                self.owned_by.position + moved
            )
