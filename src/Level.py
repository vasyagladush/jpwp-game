import bisect
from typing import Optional, Sequence

import pygame

from Actor import Actor
from Display import Display
from Vector import Vector
from constants import SCREEN_RESOLUTION


class Level:
    def __init__(self, actors: Sequence[Actor], background_color: pygame.Color = pygame.Color(0, 0, 0), render_area_size: tuple[int, int] = SCREEN_RESOLUTION) -> None:
        self._actors: list[Actor] = list(actors)
        self._actors.sort(key=Actor.get_actor_z_index)
        self.background_color: pygame.Color = background_color
        self.render_area_size: tuple[int, int] = render_area_size

    @property
    def actors(self) -> tuple[Actor, ...]:
        return tuple(self._actors)

    def add_actor(self, new_actor: Actor) -> None:
        bisect.insort(self._actors, new_actor,
                      key=Actor.get_actor_z_index)

    def tick(self) -> None:
        for actor in self._actors:
            actor.tick()

    def render_tick(self) -> None:
        Display().level_surface.fill(self.background_color)
        for actor in self._actors:
            actor.render()
