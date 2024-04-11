import pygame
from Actor import ActorComponent
from Clock import Clock
from Vector import Vector


class MovementComponent(ActorComponent):
    def __init__(self, owned_by, movement_speed: int = 300):
        """_summary_

        Args:
            owned_by (_type_): _description_
            speed (int, optional): [pixels/second]. Defaults to 300.
        """
        super().__init__(owned_by)
        self.movement_speed: int = movement_speed
        self.velocity: Vector[int] = Vector(0, 0)

    def tick(self) -> None:
        keys = pygame.key.get_pressed()

        new_velocity: Vector[int] = Vector(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            new_velocity.y -= self.movement_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            new_velocity.y += self.movement_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            new_velocity.x -= self.movement_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            new_velocity.x += self.movement_speed

        self.velocity = new_velocity

        moved: Vector[int] = (Clock().get_delta_time() / 1000) * self.velocity
        self.owned_by.position.set_coordinates(
            self.owned_by.position + moved
        )
