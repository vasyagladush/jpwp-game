import sys
from typing import NoReturn
import pygame

from Clock import Clock
from Display import Display
from constants import FPS
from levels.level1.Level1 import Level1


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('JPWP Game')
        self.display: Display = Display()
        self.clock: Clock = Clock()
        self.level = Level1()

    def run(self) -> NoReturn:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level.tick()
            self.level.render_tick()
            pygame.display.update()
            self.clock.clock.tick(FPS)


if __name__ == '__main__':
    Game().run()
