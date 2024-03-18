from Actor import Actor
from Level import Level
from Vector import Vector
from actors.Actor1 import Actor1


class Level1(Level):
    def __init__(self) -> None:
        super().__init__([Actor(Vector(3, 4), 0), Actor1(Vector(1, 3), 2)])
