from typing import final
import pygame
from Animation import Animation, AnimationController
from Display import Display
from Vector import Vector


class Renderable:
    def __init__(self, animation: Animation, rendering_order: int) -> None:
        self._animation_controller: AnimationController = AnimationController(
            animation)
        self.rendering_order: int = rendering_order
        self._animation_controller.start()

    @staticmethod
    @final
    def get_rendering_order(el: 'Renderable') -> int:
        return el.rendering_order
    
    def set_animation(self, animation: Animation) -> None:
        self._animation_controller.animation = animation

    def render(self, position: Vector) -> None:
        self._animation_controller.update()
        if self._animation_controller.current:
            Display().display.blit(
                self._animation_controller.get_current_image(), position.coordinates_to_tuple())
