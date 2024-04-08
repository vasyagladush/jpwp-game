from typing import override

import pygame

from Actor import Actor, Actor_TilemapCompatible
from Animation import Animation, AnimationFrame, AnimationPlayMode
from Vector import Vector
from components.rendering.RenderingComponent import RenderingComponent_WithAnimation
from utils.ImageUtil import ImageUtil


class Actor1_TilemapCompatible(Actor_TilemapCompatible):
    image_util = ImageUtil('./assets/sprites/player')

    @override
    def __init__(self,  position: Vector, rendering_order: int) -> None:
        images: list[pygame.Surface] = [pygame.transform.scale(
            image, (200, 200)) for image in Actor1_TilemapCompatible.image_util.load_from_dir('idle', True)]
        frames = tuple(map(lambda image: AnimationFrame(image, 300), images))
        rendering_component = RenderingComponent_WithAnimation(
            Animation(frames, AnimationPlayMode.LOOP), rendering_order)
        Actor.__init__(self, position, rendering_component)

    @override
    def tick(self) -> None:
        pass
        # print('Actor1 tick')
