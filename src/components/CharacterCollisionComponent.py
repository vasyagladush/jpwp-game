from Character import Character
from typing import override
from Actor import Actor
from Vector import Vector
from components.CollisionComponent import CollisionComponent


class CharacterCollisionComponent(CollisionComponent['Character']):
    def __init__(self, owned_by: 'Character', size: Vector, relative_position_offset: Vector = Vector(0, 0), isPhysical: bool = True):
        super().__init__(owned_by, size, relative_position_offset, isPhysical)

    @override
    def check_and_process_collision(self, other: CollisionComponent[Actor]) -> None:
        if self.isPhysical and other.isPhysical and self.owned_by.z_index == other.owned_by.z_index and not isinstance(other.owned_by, Character) and self.rect.colliderect(other.rect):
            self.resolve_collision(other)
