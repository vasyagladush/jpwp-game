import pygame
from Renderable import Renderable
from Vector import Vector


class Actor(Renderable):
    def __init__(self, position: Vector, image: pygame.Surface, rendering_order: int) -> None:
        super().__init__(position, image, rendering_order)

    def tick(self) -> None:
        print("Actor tick")
