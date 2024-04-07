import pygame
from Animation import AnimationPlayMode
from Level import Level
from Vector import Vector
from actors.Actor1 import Actor1

from enum import Enum


class RenderingOrder(Enum):
    BACKGROUND = -1
    PLAYABLEGROUND = 0
    FOREGROUND = 1


class Level1(Level):
    def __init__(self) -> None:
        super().__init__(
            actors=[Actor1(Vector(100, 100), RenderingOrder.BACKGROUND.value, AnimationPlayMode.STATIC_IMAGE),
                    Actor1(
                        Vector(180, 180), RenderingOrder.PLAYABLEGROUND.value, AnimationPlayMode.LOOP),
                    Actor1(Vector(260, 260), RenderingOrder.FOREGROUND.value, AnimationPlayMode.ONCE)],
            background_color=pygame.Color(53, 81, 92))
