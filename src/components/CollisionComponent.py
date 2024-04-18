import pygame
from Actor import ActorComponent
from Clock import Clock
from Vector import Vector
from Character import Character
from components.MovementComponent import MovementComponent

class CollisionComponent(ActorComponent):
    def __init__(self, owned_by, size: Vector):
        super().__init__(owned_by)
        self.rect = pygame.Rect(owned_by.position.x, owned_by.position.y, size.x, size.y)

    def update_rect(self):
        self.rect.x = self.owned_by.position.x
        self.rect.y = self.owned_by.position.y

    def check_collision(self, other):
        if self.rect.colliderect(other.rect):
            self.resolve_collision(other)

    def resolve_collision(self, other):
        dx = (self.rect.centerx - other.rect.centerx) / other.rect.width
        dy = (self.rect.centery - other.rect.centery) / other.rect.height

        if abs(dx) > abs(dy):
            if dx > 0: 
                self.owned_by.position.x = other.rect.right
            else: 
                self.owned_by.position.x = other.rect.left - self.rect.width
        else:
            if dy > 0: 
                self.owned_by.position.y = other.rect.bottom
            else: 
                self.owned_by.position.y = other.rect.top - self.rect.height
    def tick(self):
        
        self.update_rect()