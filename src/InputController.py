import pygame
from pygame.key import ScancodeWrapper

from Animation import Animation, AnimationController, AnimationFrame
from Display import Display
from RenderingController import RenderingController, RenderingController_WithAnimation
from Vector import Vector
from utils.ImageUtil import ImageUtil
from utils.Pointer import Pointer


class InputController:
    """Singleton class that holds an instance of InputController"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._keys_state = pygame.key.get_pressed()
        return cls._instance

    @property
    def keys_state(self) -> ScancodeWrapper:
        return self._keys_state

    @keys_state.setter
    def keys_state(self, value) -> None:
        self._keys_state: ScancodeWrapper = value

    def tick(self) -> None:
        self.keys_state = pygame.key.get_pressed()
