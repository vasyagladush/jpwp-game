import pygame
from enum import Enum
from Animation import AnimationPlayMode
from Level import Level
from Vector import Vector
from actors.characters.Fox import Fox
from components.test.TestComponent import TestComponent
from levels.level1.Tilemap1 import Tilemap1
from utils.ImageUtil import ImageUtil



class RenderingOrder(Enum):
    BACKGROUND = -1
    PLAYABLEGROUND = 0
    FOREGROUND = 1


class Level1(Level):
    background_image = ImageUtil.load_image('assets/sky.png')
    def __init__(self) -> None:
        super().__init__(
            actors=Tilemap1().actors,
            background_color=pygame.Color(53, 81, 92), background_image=Level1.background_image, render_area_size=(4000, 2500), player_start_position=Vector(200, 200))
