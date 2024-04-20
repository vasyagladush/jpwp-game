from enum import Enum, auto
from typing import TypeVar
import pygame
from Actor import Actor, ActorComponent, ActorEventType
from Display import Display
from Vector import Vector
from constants import DEBUG_COLLISIONS
from utils.EventEmitter import EventEmitter

ActorComponentOwnerType = TypeVar('ActorComponentOwnerType', bound=Actor)


class CollisionComponentEvents(Enum):
    STAYING_ON_GROUND = auto()


class CollisionComponent(EventEmitter[CollisionComponentEvents], ActorComponent[ActorComponentOwnerType]):
    def __init__(self, owned_by: ActorComponentOwnerType, size: Vector, relavive_position_offset: Vector = Vector(0, 0), isPhysical: bool = True):
        EventEmitter.__init__(
            self, CollisionComponentEvents)
        ActorComponent.__init__(self, owned_by)
        self.owned_by.add_event_subscription(
            ActorEventType.POSITION_CHANGED, self.update_rect)

        self.rect = pygame.Rect(owned_by.get_position().x,
                                owned_by.get_position().y, size.x, size.y)
        self.isPhysical: bool = isPhysical
        """Tells if there's a collision at the bottom"""
        self.isOnGround = False
        """Position offset relative to owned_by topleft"""
        self.relavive_position_offset: Vector = relavive_position_offset

    def update_rect(self, event_type: ActorEventType = ActorEventType.POSITION_CHANGED):
        self.rect.topleft = (self.owned_by.get_position().x + self.relavive_position_offset.x,
                             self.owned_by.get_position().y + self.relavive_position_offset.y)

    def check_and_process_collision(self, other: 'CollisionComponent'):
        pass

    def update_owned_by_position(self):
        self.owned_by.set_position(Vector(
            self.rect.x - self.relavive_position_offset.x, self.rect.y - self.relavive_position_offset.y))

    def resolve_collision(self, other: 'CollisionComponent'):
        dx: float = (self.rect.centerx - other.rect.centerx) / other.rect.width
        dy: float = (self.rect.centery - other.rect.centery) / \
            other.rect.height

        if abs(dx) > abs(dy):
            if dx > 0:
                self.rect.left = other.rect.right
            else:
                self.rect.right = other.rect.left
        else:
            if dy > 0:
                self.rect.top = other.rect.bottom
            else:
                self.isOnGround = True
                self.emit_event(CollisionComponentEvents.STAYING_ON_GROUND)
                self.rect.bottom = other.rect.top + 1
        # dx: float = (self.rect.centerx - other.rect.centerx) / other.rect.width
        # dy: float = (self.rect.centery - other.rect.centery) / \
        #     other.rect.height

        # if abs(dx) > abs(dy):
        #     if dx > 0:
        #         self.owned_by.position.x = other.rect.right
        #     else:
        #         self.owned_by.position.x = other.rect.left - self.rect.width
        # else:
        #     if dy > 0:
        #         self.owned_by.position.y = other.rect.bottom
        #     else:
        #         self.isOnGround = True
        #         self.owned_by.position.y = other.rect.top - self.rect.height

        self.update_owned_by_position()

    def tick(self):
        if DEBUG_COLLISIONS:
            pygame.draw.rect(Display().level_surface.holded_ref,
                             pygame.Color(255, 0, 0, 50), self.rect)
        self.isOnGround = False
        self.update_rect()
