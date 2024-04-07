import bisect
from typing import Optional, Sequence

import pygame

from Actor import Actor
from Display import Display
from Renderable import Renderable
from Vector import Vector


class Level:
    def __init__(self, actors: Sequence[Actor], background_color: pygame.Color = pygame.Color(0, 0, 0)) -> None:
        self._actors: list[Actor] = list(actors)
        self._actors.sort(key=Renderable.get_rendering_order)
        self.background_color: pygame.Color = background_color

    @property
    def actors(self) -> tuple[Actor, ...]:
        return tuple(self._actors)

    def addActor(self, new_actor: Actor) -> None:
        bisect.insort(self._actors, new_actor,
                      key=Renderable.get_rendering_order)

    def tick(self) -> None:
        for actor in self._actors:
            actor.tick()

    def render_tick(self) -> None:
        Display().display.fill(self.background_color)
        for actor in self._actors:
            actor.render()
