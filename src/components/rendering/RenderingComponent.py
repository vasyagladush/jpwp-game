from typing import override
import pygame
from Animation import Animation, AnimationController, AnimationFrame
from Display import Display
from Vector import Vector
from abc import ABC, abstractmethod


class RenderingComponent(ABC):
    def __init__(self, rendering_order: int) -> None:
        self.rendering_order: int = rendering_order

    # @staticmethod
    # @final
    # def get_rendering_order(el: 'Renderable') -> int:
    #     return el.rendering_order

    @abstractmethod
    def render(self, position: Vector) -> None:
        pass

    @abstractmethod
    def set_all_images_to_size(self, size: Vector) -> None:
        pass


class RenderingComponent_WithStaticImage(RenderingComponent):
    def __init__(self, image: pygame.Surface, rendering_order: int) -> None:
        super().__init__(rendering_order)
        self.image: pygame.Surface = image

    def set_image(self, image: pygame.Surface) -> None:
        self.image = image

    @override
    def render(self, position: Vector) -> None:
        Display().display.blit(
            self.image, position.coordinates_to_tuple())

    @override
    def set_all_images_to_size(self, size: Vector) -> None:
        self.image = pygame.transform.scale(
            self.image, size.coordinates_to_tuple())


class RenderingComponent_WithAnimation(RenderingComponent):
    def __init__(self, animation: Animation, rendering_order: int) -> None:
        super().__init__(rendering_order)
        self._animation_controller: AnimationController = AnimationController(
            animation)
        self._animation_controller.start()

    def set_animation(self, animation: Animation) -> None:
        self._animation_controller.animation = animation

    @override
    def render(self, position: Vector) -> None:
        self._animation_controller.update()
        if self._animation_controller.current:
            Display().display.blit(
                self._animation_controller.get_current_image(), position.coordinates_to_tuple())

    @override
    def set_all_images_to_size(self, size: Vector) -> None:
        self._animation_controller.current = pygame.transform.scale(
            self._animation_controller.current, size.coordinates_to_tuple())
        self._animation_controller.next = pygame.transform.scale(
            self._animation_controller.next, size.coordinates_to_tuple())
        resized_frames: list[AnimationFrame] = [AnimationFrame(pygame.transform.scale(
            frame.image, size.coordinates_to_tuple()), frame.duration) for frame in self._animation_controller.animation.frames]
        self._animation_controller.animation = Animation(
            resized_frames, self._animation_controller.animation.playmode)
