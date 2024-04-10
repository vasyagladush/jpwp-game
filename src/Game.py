import sys
from typing import NoReturn
import pygame

from Clock import Clock
from Display import Display
from Level import Level
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

            # self.display.update_camera_offset((self.display.camera_surface.get_offset()[ # TESTING
            #                                     0] + 5, self.display.camera_surface.get_offset()[1] + 5)) # TESTING
            self.display.display.blit(self.display.camera_surface, (0, 0))

            pygame.display.update()
            self.clock.clock.tick(FPS)

    @property
    def level(self) -> Level:
        return self._level

    @level.setter
    def level(self, value) -> None:
        self._level: Level = value
        self.display.set_level_surface_size(self._level.render_area_size)


if __name__ == '__main__':
    Game().run()
