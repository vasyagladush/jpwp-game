from typing import override

from Actor import Actor
from Vector import Vector
from utils.ImageUtil import ImageUtil


class Actor1(Actor):
    def __init__(self, position: Vector, rendering_order: int) -> None:
        super().__init__(position, ImageUtil.load_image(
            './assets/sprites/player/idle/player-idle-1.png'), rendering_order)

    @override
    def tick(self) -> None:
        print('Actor1 tick')
