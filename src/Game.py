from os import access, login_tty
import sys
from typing import NoReturn
import pygame

from Animation import Animation, AnimationController, AnimationFrame
from HUD import HUD
from utils.ImageUtil import ImageUtil
from Clock import Clock
from Display import Display
from Level import Level
from Player import Player
from constants import FPS, SCREEN_RESOLUTION
from levels.level1.Level1 import Level1


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('JPWP Game')
        self.display: Display = Display()
        self.clock: Clock = Clock()
        self.player: Player = Player()
        self.level = Level1()
        self.hud = HUD()

    def run(self) -> NoReturn:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Tick
            self.level.tick()

            # Render tick
            self.level.render_tick()
            self.hud.render_tick()

            # Camera surface offset update
            player_position: tuple[int,
                                   int] = self.player.player.position.coordinates_to_tuple()
            display_size: tuple[int, int] = self.display.display.get_size()
            self.display.update_camera_offset((player_position[0] - (int)(
                display_size[0] / 2), player_position[1] - (int)(display_size[1] / 2)))
            
            # Blitting on display
            self.display.display.blit(self.display.camera_surface, (0, 0))
            self.display.display.blit(self.display.hud_surface, (0, 0))
            pygame.display.update()
            
            self.clock.clock.tick(FPS)

    @property
    def level(self) -> Level:
        return self._level

    @level.setter
    def level(self, value) -> None:
        self._level: Level = value
        self.player.player.position = self._level.player_start_position
        self.display.set_level_surface_size(self._level.render_area_size)


if __name__ == '__main__':
    Game().run()
