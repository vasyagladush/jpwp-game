from typing import override
import pygame
from Animation import Animation, AnimationController, AnimationFrame
from Display import Display
from Vector import Vector
from abc import ABC, abstractmethod


class RenderingController(ABC):
    def __init__(self) -> None:
        pass

    # @staticmethod
    # @final
    # def get_z_index(el: 'Renderable') -> int:
    #     return el.z_index

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
    def __init__(self, image: pygame.Surface) -> None:
        super().__init__()
        self.image: pygame.Surface = image

    def set_image(self, image: pygame.Surface) -> None:
        self.image = image

    @override
    def render(self, position: Vector) -> None:
        Display().display.blit(
            self.image, position.coordinates_to_tuple())

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
    def __init__(self, animation: Animation) -> None:
        super().__init__()
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
        
    #TODO: create a method set_transformation(self, size, angle, flip)
