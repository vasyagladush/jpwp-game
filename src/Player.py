from enum import Enum, auto
from typing import override
import pygame
from pygame.key import ScancodeWrapper

from Actor import Actor
from InputController import InputController
from RenderingController import RenderingController_WithStaticImage
from Vector import Vector
from actors.characters.Fox import Fox
from components.CharacterCollisionComponent import CharacterCollisionComponent
from components.CollisionComponent import CollisionComponent


class Player():
    """Singleton class that holds an instance of Player."""

    class PlayerCharacterCollisionComponent(CharacterCollisionComponent):
        @override
        def check_and_process_collision(self, other: CollisionComponent[Actor]) -> None:
            super().check_and_process_collision(other)
            # YOUR CODE HERE

    class PlayerCharacter(Fox):
        def __init__(self, position: Vector, z_index: int, movement_speed: int = 300) -> None:
            super().__init__(position, z_index, movement_speed)
            self.dead: bool = False
            # MADE FOR TASK CONSTRUCTING PURPOSES
            old_collision_component = self.collision_component
            existing_event_handlers = self.collision_component._event_handlers
            self.collision_component = Player.PlayerCharacterCollisionComponent(
                self, Vector(self.idle_animation.frames[0].image.get_size()))
            self.collision_component.relavive_position_offset = Vector(30, 55)
            self.collision_component.rect.width = self.collision_component.rect.width * 0.6
            self.collision_component.rect.height = self.collision_component.rect.height * 0.65
            self.collision_component._event_handlers = existing_event_handlers
            self.components.remove(old_collision_component)
            self.components.append(self.collision_component)

        def die(self):
            self.dead = True
            self.rendering_controller = RenderingController_WithStaticImage() # type: ignore

        @override
        def tick(self):
            if not self.dead:
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

from actors.characters.enemy.Enemy import Enemy