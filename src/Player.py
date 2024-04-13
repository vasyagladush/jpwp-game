from typing import override
import pygame
from pygame.key import ScancodeWrapper

from InputController import InputController
from Vector import Vector
from actors.characters.Fox import Fox
from components.GravityComponent import GravityComponent
from components.MovementComponent import MovementComponent


class Player():
    """Singleton class that holds an instance of Player."""
    class PlayerCharacter(Fox):
        @override
        def tick(self):
            keys: ScancodeWrapper = InputController().keys_state
            movement_direction: Vector = Vector(0, 0)

            if keys[pygame.K_w] or keys[pygame.K_UP]:
                movement_direction.y -= 1
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                movement_direction.y += 1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                movement_direction.x -= 1
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                movement_direction.x += 1

            self.movement_component.set_direction(movement_direction) 

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
