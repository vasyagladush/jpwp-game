import pygame
from Display import Display
from Vector import Vector


class Renderable:
    display: pygame.Surface = Display().display

    def __init__(self, position: Vector, image: pygame.Surface, rendering_order: int) -> None:
        self.position: Vector = position
        self.image: pygame.Surface = image
        self.rendering_order: int = rendering_order

    @staticmethod
    def get_rendering_order(el: 'Renderable') -> int:
        return el.rendering_order

    def render(self) -> None:
        Renderable.display.blit(
            self.image, self.position.coordinates_to_tuple())
