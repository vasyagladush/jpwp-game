import pygame
from Display import Display
from Renderable import Renderable
from Vector import Vector


class RenderingComponent_WithStaticImage(Renderable):
    def __init__(self, image: pygame.Surface, rendering_order: int) -> None:
        super().__init__(rendering_order)
        self.image: pygame.Surface = image
    
    def set_image(self, image: pygame.Surface) -> None:
        self.image = image

    def render(self, position: Vector) -> None:
        Display().display.blit(
            self.image, position.coordinates_to_tuple())
