import pygame
from Actor import Actor
from Level import Level
from Vector import Vector
from actors.Actor1 import Actor1

from enum import Enum

from utils.ImageUtil import ImageUtil


class RenderingOrder(Enum):
    BACKGROUND = -1
    PLAYABLEGROUND = 1
    FOREGROUND = 2


class Level1(Level):
    def __init__(self) -> None:
        super().__init__(
            [Actor(Vector(100, 100),  pygame.transform.scale(ImageUtil.load_image(
                './assets/sprites/cherry/cherry-1.png', (255, 255, 255)), (200, 200)), RenderingOrder.BACKGROUND.value),
                Actor(Vector(100, 150), pygame.transform.scale(ImageUtil.load_image(
                    './assets/sprites/player/idle/player-idle-1.png', (255, 255, 255)), (200, 200)), RenderingOrder.PLAYABLEGROUND.value),
             Actor(Vector(130, 250), pygame.transform.scale(ImageUtil.load_image(
                 './assets/sprites/item-feedback/item-feedback-1.png', (255, 255, 255)), (200, 200)), RenderingOrder.FOREGROUND.value)])
