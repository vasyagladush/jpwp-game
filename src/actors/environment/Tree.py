from typing import override

import pygame

from Actor import Actor, Actor_TilemapCompatible
from Vector import Vector
from RenderingController import RenderingController_WithStaticImage
from constants import DEFAULT_TILE_SIZE
from utils.ImageUtil import ImageUtil
from components.CollisionComponent import CollisionComponent


class Tree_TilemapCompatible(Actor_TilemapCompatible):
    image = ImageUtil.load_image('assets/colored_tree.png', True)

    @override
    def __init__(self,  position: Vector, z_index: int) -> None:
        rendering_controller = RenderingController_WithStaticImage(
            Tree_TilemapCompatible.image)
        Actor.__init__(self, position, rendering_controller, z_index)

    @override
    def tick(self) -> None:
        super().tick()

