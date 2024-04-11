import pygame
from enum import Enum
from Animation import AnimationPlayMode
from Level import Level
from Vector import Vector
from actors.characters.Fox import Fox
from components.test.TestComponent import TestComponent
from levels.level1.Tilemap1 import Tilemap1



class RenderingOrder(Enum):
    BACKGROUND = -1
    PLAYABLEGROUND = 0
    FOREGROUND = 1


class Level1(Level):
    def __init__(self) -> None:
        flipping_fox = Fox(
            Vector(180, 180), RenderingOrder.PLAYABLEGROUND.value)
        flipping_fox.components.append(TestComponent(flipping_fox))
        super().__init__(
            actors=Tilemap1().actors + [flipping_fox, Fox(Vector(120, 120), RenderingOrder.BACKGROUND.value),
                                        Fox(Vector(220, 260), RenderingOrder.FOREGROUND.value)],
            background_color=pygame.Color(53, 81, 92), render_area_size=(4000, 4000), player_start_position=Vector(800, 800))
