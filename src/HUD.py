import pygame

from Animation import Animation, AnimationController, AnimationFrame
from Display import Display
from RenderingController import RenderingController, RenderingController_WithAnimation
from Vector import Vector
from utils.ImageUtil import ImageUtil
from utils.Pointer import Pointer


class HUD:
    """Singleton class that holds an instance of HUD"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            in_game_logo_animation: Animation = Animation([AnimationFrame(
                pygame.transform.scale(img, (100, 100)), 150) for img in ImageUtil.load_images_from_dir('assets/sprites/item-feedback', True)])
            cls._instance.in_game_logo = RenderingController_WithAnimation(in_game_logo_animation,
                                                                           Pointer(Display().hud_surface))
        return cls._instance

    @property
    def in_game_logo(self) -> RenderingController_WithAnimation:
        return self._in_game_logo

    @in_game_logo.setter
    def in_game_logo(self, value) -> None:
        self._in_game_logo: RenderingController_WithAnimation = value

    def render_tick(self) -> None:
        Display().hud_surface.fill((0, 0, 0, 0))
        self.in_game_logo.render(Vector(0, 0))

    # TODO: does it make sense?
    # def get_delta_frames(self) -> int:
    #     return round(self.get_delta_time() * FPS)
