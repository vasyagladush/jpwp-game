import pygame
from Actor import ActorComponent
from Clock import Clock
from Vector import Vector

class MovementComponent(ActorComponent):
    def __init__(self, owned_by, speed: int = 300):
        """_summary_

        Args:
            owned_by (_type_): _description_
            speed (int, optional): [pixels/second]. Defaults to 300.
        """
        super().__init__(owned_by)
        self.speed = speed

    def tick(self) -> None:
        keys = pygame.key.get_pressed()
        movement = Vector(0, 0)
        passed_distance: int = (int)(self.speed * Clock().get_delta_time() / 1000)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            movement.y -= passed_distance
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            movement.y += passed_distance
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            movement.x -= passed_distance
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            movement.x += passed_distance

        self.owned_by.position.set_coordinates(
            self.owned_by.position.x + movement.x,
            self.owned_by.position.y + movement.y
        )
