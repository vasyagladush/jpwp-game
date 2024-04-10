from typing import override

import pygame

from Actor import Actor, Actor_TilemapCompatible
from Vector import Vector
from RenderingController import RenderingController_WithStaticImage
from utils.ImageUtil import ImageUtil


class Block_TilemapCompatible(Actor_TilemapCompatible):
    image_util = ImageUtil('./assets/sprites')

    @override
    def __init__(self,  position: Vector, z_index: int) -> None:
        image: pygame.Surface = Block_TilemapCompatible.image_util.load(
            'block-big.png')
        rendering_controller = RenderingController_WithStaticImage(
            image)
        Actor.__init__(self, position, rendering_controller, z_index)

    @override
    def tick(self) -> None:
        pass
        # print('Actor1 tick')
