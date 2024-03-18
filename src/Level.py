import bisect
from typing import NoReturn, Sequence

from Actor import Actor
from Renderable import Renderable
from Vector import Vector


class Level:
    def __init__(self, actors: Sequence[Actor]):
        self._actors: list[Actor] = list(actors)
        self._actors.sort(key=Renderable.get_rendering_order)

    @property
    def actors(self):
        return self._actors

    def addActor(self, new_actor: Actor):
        bisect.insort(self._actors, new_actor, key=Renderable.get_rendering_order)


    def tick(self) -> None:
        print('Level tick')
        for actor in self.actors:
            actor.tick()

    def render_tick(self) -> None:
        print('Level render tick')
        for actor in self.actors:
            actor.render()

# Tests
if __name__ == '__main__':
    l = Level([Actor(Vector(3, 3), 2), Actor(Vector(2,2), -1)])
    l.addActor(Actor(Vector(1, 1), 1))
    l.addActor(Actor(Vector(1, 1), 5))
    l.addActor(Actor(Vector(1, 1), -3))
    for a in l.actors:
        print(a.rendering_order)