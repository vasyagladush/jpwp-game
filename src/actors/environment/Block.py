from typing import override

import pygame

from Actor import Actor, Actor_TilemapCompatible
from Vector import Vector
from RenderingController import RenderingController_WithStaticImage
from utils.ImageUtil import ImageUtil
from components.CollisionComponent import CollisionComponent


class Block_TilemapCompatible(Actor_TilemapCompatible):
    image = ImageUtil.load_image('assets/sprites/block-big.png')

    @override
    def __init__(self,  position: Vector, z_index: int) -> None:
        rendering_controller = RenderingController_WithStaticImage(
            Block_TilemapCompatible.image)
        Actor.__init__(self, position, rendering_controller, z_index)
        self.collision_component = CollisionComponent(self, Vector(50, 50))
        self.components.append(self.collision_component)

    @override
    def tick(self) -> None:
        super().tick()
        # print('Actor1 tick')
