import pygame
from Actor import ActorComponent
from Clock import Clock
from Vector import Vector
from Character import Character
from components.MovementComponent import MovementComponent

class CollisionComponent(ActorComponent):
    def __init__(self, owned_by, size: Vector):
        super().__init__(owned_by)
        self.rect = pygame.Rect(
            owned_by.position.x, owned_by.position.y, size.x, size.y)

    def update_rect(self):
        self.rect.x = self.owned_by.position.x
        self.rect.y = self.owned_by.position.y

    def check_collision(self, other):
        return self.rect.colliderect(other.rect)

    def tick(self):
        self.update_rect()

