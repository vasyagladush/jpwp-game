from typing import override

import pygame

from Actor import Actor
from Animation import Animation, AnimationFrame, AnimationPlayMode
from Vector import Vector
from components.rendering.RenderingComponent import RenderingComponent_WithAnimation
from utils.ImageUtil import ImageUtil


class Actor1(Actor):
    image_util = ImageUtil('./assets/sprites/player')

    def __init__(self, position: Vector, rendering_order: int, animation_playmode: AnimationPlayMode) -> None:
        images: list[pygame.Surface] = [pygame.transform.scale(
            image, (200, 200)) for image in Actor1.image_util.load_from_dir('idle', True)]
        frames = tuple(map(lambda image: AnimationFrame(image, 300), images))
        rendering_component = RenderingComponent_WithAnimation(
            Animation(frames, animation_playmode), rendering_order)
        super().__init__(position, rendering_component)

    @override
    def tick(self) -> None:
        pass
        # print('Actor1 tick')