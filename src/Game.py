import sys
from time import time
from typing import NoReturn
import pygame

from Display import Display
from constants import FPS
from levels.Level1 import Level1


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('JPWP Game')
        self.previous_tick_epoch: float = time()
        self.delta_time: float = 0.0
        self.delta_frames: int = 0
        self.display: pygame.Surface = Display().display
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.level = Level1()

    def run(self) -> NoReturn:
        while True:
            self.delta_time = time() - self.previous_tick_epoch
            self.previous_tick_epoch = time()
            self.delta_frames = round(self.delta_time * FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.tick()
            self.level.render_tick()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
