import pygame

from Vector import Vector
from actors.characters.Fox import Fox
from components.GravityComponent import GravityComponent
from components.MovementComponent import MovementComponent


class Player():
    """CREATED FOR TESTING PURPOSES. Singleton class that holds an instance of Player. CREATED FOR TESTING PURPOSES."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.player = Fox(Vector(0, 0), 0)
            cls._instance.player.components.append(MovementComponent(cls._instance.player))
            # cls._instance.player.components.append(GravityComponent(cls._instance.player))
        return cls._instance

    @property
    def player(self) -> Fox:
        return self._player

    @player.setter
    def player(self, value) -> None:
        self._player: Fox = value
