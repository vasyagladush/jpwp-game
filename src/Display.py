import pygame

from constants import SCREEN_RESOLUTION


class Display:
    """Singleton class that holds an instance of pygame.screen"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.display = pygame.display.set_mode(SCREEN_RESOLUTION)
        return cls._instance

    @property
    def display(self) -> pygame.Surface:
        return self._display

    @display.setter
    def display(self, value) -> None:
        self._display: pygame.Surface = value

