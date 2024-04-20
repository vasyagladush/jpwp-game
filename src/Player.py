import pygame
from pygame.key import ScancodeWrapper

from InputController import InputController
from Vector import Vector
from actors.characters.Fox import Fox


class Player():
    """Singleton class that holds an instance of Player."""
    class PlayerCharacter(Fox):
        def tick(self):
            keys: ScancodeWrapper = InputController().keys_state
            x_movement_direction: int = 0

            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                x_movement_direction -= 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                x_movement_direction += 1

            self.movement_component.set_x_direction(x_movement_direction) 

            if keys[pygame.K_SPACE]:
                self.jump()

            super().tick()

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.player = Player.PlayerCharacter(Vector(0, 0), 0)
            # cls._instance.player.components.append(GravityComponent(cls._instance.player))
        return cls._instance

    @property
    def player(self) -> Fox:
        return self._player

    @player.setter
    def player(self, value) -> None:
        self._player: Fox = value
