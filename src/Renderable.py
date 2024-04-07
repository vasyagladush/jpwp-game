from typing import final
import pygame
from Display import Display
from Vector import Vector


class Renderable:
    def __init__(self, image: pygame.Surface, rendering_order: int) -> None:
        self.image: pygame.Surface = image
        self.rendering_order: int = rendering_order

    @staticmethod
    @final
    def get_rendering_order(el: 'Renderable') -> int:
        return el.rendering_order

    def render(self, position: Vector) -> None:
        Display().display.blit(
            self.image, position.coordinates_to_tuple())
