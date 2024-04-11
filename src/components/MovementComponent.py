import pygame
from Actor import ActorComponent
from Vector import Vector

class MovementComponent(ActorComponent):
    def __init__(self, owned_by, speed: int = 5):
        super().__init__(owned_by)
        self.speed = speed

    def tick(self) -> None:
        keys = pygame.key.get_pressed()
        movement = Vector(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            movement.y -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            movement.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            movement.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            movement.x += self.speed

        self.owned_by.position.set_coordinates(
            self.owned_by.position.x + movement.x,
            self.owned_by.position.y + movement.y
        )
