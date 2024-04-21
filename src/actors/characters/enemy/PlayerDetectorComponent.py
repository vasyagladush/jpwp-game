from Vector import Vector
from components.CollisionComponent import CollisionComponent
from constants import DEFAULT_TILE_SIZE


class PlayerDetectorComponent(CollisionComponent['Enemy']):
    def __init__(self, owned_by: 'Enemy'):
        super().__init__(owned_by, Vector(200, DEFAULT_TILE_SIZE), Vector(0, 0), False)

from actors.characters.enemy.Enemy import Enemy