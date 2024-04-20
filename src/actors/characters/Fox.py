from typing import override

import pygame

from Animation import Animation, AnimationFrame
from Character import Character
from Vector import Vector
from utils.ImageUtil import ImageUtil


class Fox(Character):
    image_util = ImageUtil('./assets/sprites/player')
    idle_animation = Animation(tuple(map(lambda image: AnimationFrame(image, 150), [pygame.transform.scale(
        image, (150, 150)) for image in image_util.load_from_dir('idle', True)])))
    running_animation = Animation(tuple(map(lambda image: AnimationFrame(image, 150), [pygame.transform.scale(
        image, (150, 150)) for image in image_util.load_from_dir('run', True)])))
    jumping_animation = Animation(tuple(map(lambda image: AnimationFrame(image, 150), [pygame.transform.scale(
        image, (150, 150)) for image in image_util.load_from_dir('jump', True)])))
    falling_animation = Animation(tuple(map(lambda image: AnimationFrame(image, 150), [pygame.transform.scale(
        image, (150, 150)) for image in image_util.load_from_dir('falling', True)])))

    def __init__(self, position: Vector, z_index: int, movement_speed: int = 300) -> None:
        super().__init__(position, z_index)
        self.collision_component.relavive_position_offset = Vector(30, 55)
        self.collision_component.rect.width = self.collision_component.rect.width * 0.6
        self.collision_component.rect.height = self.collision_component.rect.height * 0.65

    @override
    def tick(self) -> None:
        super().tick()
        # some other logic
