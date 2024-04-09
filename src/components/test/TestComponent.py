import pygame

from Actor import Actor, ActorComponent


class TestComponent(ActorComponent):
    def __init__(self, owned_by: Actor) -> None:
        self.owned_by: Actor = owned_by
        self.last_flip_time: int = 0

    def tick(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_flip_time > 500:
            self.last_flip_time = now
            self.owned_by.flip(True, False)
        pass


