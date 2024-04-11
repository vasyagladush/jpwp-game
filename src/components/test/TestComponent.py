import pygame

from Actor import Actor, ActorComponent
from actors.characters.Fox import Fox


class TestComponent(ActorComponent):
    def __init__(self, owned_by: Fox) -> None:
        super().__init__(owned_by)
        self.last_flip_time: int = 0
        self.owned_by.add_event_subscription(
            self.owned_by.EventType.FLIPPED, self.on_flip)

    def tick(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_flip_time > 500:
            self.last_flip_time = now
            self.owned_by.flip(True, False)
        pass

    def on_flip(self) -> None:
        print(f"flipped at {pygame.time.get_ticks() / 1000}s")
