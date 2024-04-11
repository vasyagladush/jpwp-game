from typing import override
import pygame
from Animation import Animation, AnimationController, AnimationFrame
from Display import Display
from Vector import Vector
from abc import ABC, abstractmethod

from utils.Pointer import Pointer


class RenderingController(ABC):
    def __init__(self, surface: Pointer[pygame.Surface] = Display().level_surface) -> None:
        self.surface: Pointer[pygame.Surface] = surface

    def blit(self, image: pygame.Surface, position: Vector):
        self.surface.holded_ref.blit(image, position.coordinates_to_tuple())

    @abstractmethod
    def render(self, position: Vector) -> None:
        pass

    @abstractmethod
    def set_size(self, size: Vector) -> None:
        pass

    @abstractmethod
    def set_angle(self, angle: int) -> None:
        pass

    @abstractmethod
    def flip(self, x: bool, y: bool) -> None:
        pass


class RenderingController_WithStaticImage(RenderingController):
    def __init__(self, image: pygame.Surface, surface: Pointer[pygame.Surface] = Display().level_surface) -> None:
        super().__init__(surface)
        self.image: pygame.Surface = image

    def set_image(self, image: pygame.Surface) -> None:
        self.image = image

    @override
    def render(self, position: Vector) -> None:
        self.blit(
            self.image, position)

    @override
    def set_size(self, size: Vector) -> None:
        self.image = pygame.transform.scale(
            self.image, size.coordinates_to_tuple())

    @override
    def set_angle(self, angle: int) -> None:
        self.image = pygame.transform.rotate(
            self.image, angle)

    @override
    def flip(self, x: bool, y: bool) -> None:
        self.image = pygame.transform.flip(
            self.image, x, y)


class RenderingController_WithAnimation(RenderingController):
    def __init__(self, animation: Animation, surface: Pointer[pygame.Surface] = Display().level_surface) -> None:
        super().__init__(surface)
        self._animation_controller: AnimationController = AnimationController(
            animation)
        self._animation_controller.start()

    def set_animation(self, animation: Animation) -> None:
        self._animation_controller.animation = animation

    @override
    def render(self, position: Vector) -> None:
        self._animation_controller.update()
        if self._animation_controller.current:
            self.blit(
                self._animation_controller.get_current_image(), position)

    @override
    def set_size(self, size: Vector) -> None:
        # TODO: maybe add del statements on old frames and animation
        resized_frames: list[AnimationFrame] = [AnimationFrame(pygame.transform.scale(
            frame.image, size.coordinates_to_tuple()), frame.duration) for frame in self._animation_controller.animation.frames]
        self._animation_controller.animation = Animation(
            resized_frames, self._animation_controller.animation.playmode)

    @override
    def set_angle(self, angle: int) -> None:
        angled_frames: list[AnimationFrame] = [AnimationFrame(pygame.transform.rotate(
            frame.image, angle), frame.duration) for frame in self._animation_controller.animation.frames]
        self._animation_controller.animation = Animation(
            angled_frames, self._animation_controller.animation.playmode)

    @override
    def flip(self, x: bool, y: bool) -> None:
        flipped_frames: list[AnimationFrame] = [AnimationFrame(pygame.transform.flip(
            frame.image, x, y), frame.duration) for frame in self._animation_controller.animation.frames]
        self._animation_controller.animation = Animation(
            flipped_frames, self._animation_controller.animation.playmode)

    # TODO: create a method set_transformation(self, size, angle, flip)
