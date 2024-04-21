import bisect
from typing import Optional, Sequence

import pygame

from Actor import Actor
from Display import Display
from Player import Player
from Vector import Vector
from components.CollisionComponent import CollisionComponent
from constants import SCREEN_RESOLUTION


class Level:
    def __init__(self, actors: Sequence[Actor], background_color: pygame.Color = pygame.Color(0, 0, 0), background_image: Optional[pygame.Surface] = None, render_area_size: tuple[int, int] = SCREEN_RESOLUTION, player_start_position: Vector = Vector(0, 0)) -> None:
        self._actors: list[Actor] = list(actors) + [Player().player]
        self._actors.sort(key=Actor.get_actor_z_index)
        self.render_area_size: tuple[int, int] = render_area_size
        self.background_color: pygame.Color = background_color
        self.background_image: Optional[pygame.Surface] = pygame.transform.scale(
            background_image, self.render_area_size) if background_image else None
        self.player_start_position: Vector = player_start_position

    @property
    def actors(self) -> tuple[Actor, ...]:
        return tuple(self._actors)

    def render_tick(self) -> None:
        Display().level_surface.holded_ref.fill(self.background_color)
        if self.background_image:
            Display().level_surface.holded_ref.blit(self.background_image, (0, 0))
        for actor in self._actors:
            actor.render()

    def tick(self):
        self.handle_collisions()
        for actor in self._actors:
            actor.tick()

    def add_actor(self, new_actor: Actor) -> None:
        bisect.insort(self._actors, new_actor, key=Actor.get_actor_z_index)

    def handle_collisions(self):
        for actor in self._actors:
            for component in actor.components:
                if isinstance(component, CollisionComponent):
                    for other_actor in self._actors:
                        if actor != other_actor:
                            for other_actor_component in other_actor.components:
                                if isinstance(other_actor_component, CollisionComponent):
                                    component.check_and_process_collision(
                                        other_actor_component)
