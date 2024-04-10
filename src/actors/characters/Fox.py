from typing import override

import pygame

from Actor import Actor
from Animation import Animation, AnimationFrame, AnimationPlayMode
from Vector import Vector
from RenderingController import RenderingController_WithAnimation
from utils.ImageUtil import ImageUtil


class Fox(Actor):
    image_util = ImageUtil('./assets/sprites/player')

    def __init__(self, position: Vector, z_index: int, animation_playmode: AnimationPlayMode) -> None:
        images: list[pygame.Surface] = [pygame.transform.scale(
            image, (150, 150)) for image in Fox.image_util.load_from_dir('idle', True)]
        frames = tuple(map(lambda image: AnimationFrame(image, 150), images))
        rendering_controller = RenderingController_WithAnimation(
            Animation(frames, animation_playmode))
        super().__init__(position, rendering_controller, z_index)

    @override
    def tick(self) -> None:
        super().tick()
        # some other logic
