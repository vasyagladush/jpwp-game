import pygame

from constants import SCREEN_RESOLUTION
from utils.MathUtil import constrain_int
from utils.Pointer import Pointer


class Display:
    """Singleton class that holds an instance of pygame.screen"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.display = pygame.display.set_mode(
                SCREEN_RESOLUTION, pygame.SCALED | pygame.FULLSCREEN)
            cls._instance.level_surface = Pointer(
                pygame.Surface(SCREEN_RESOLUTION))
            cls._instance.camera_surface = cls._instance.level_surface.holded_ref.subsurface(
                (0, 0), SCREEN_RESOLUTION)
            cls._instance.hud_surface = pygame.Surface(
                SCREEN_RESOLUTION, pygame.SRCALPHA)

        return cls._instance

    @property
    def display(self) -> pygame.Surface:
        return self._display

    @display.setter
    def display(self, value) -> None:
        self._display: pygame.Surface = value

    @property
    def level_surface(self) -> Pointer[pygame.Surface]:
        return self._level_surface

    @level_surface.setter
    def level_surface(self, value) -> None:
        self._level_surface: Pointer[pygame.Surface] = value

    def set_level_surface_size(self, size: tuple[int, int]) -> None:
        self.level_surface.holded_ref = pygame.transform.scale(
            self.level_surface.holded_ref, size)
        self.update_camera_offset(self.camera_surface.get_offset())

    @property
    def camera_surface(self) -> pygame.Surface:
        return self._camera_surface

    @camera_surface.setter
    def camera_surface(self, value) -> None:
        self._camera_surface: pygame.Surface = value

    @property
    def hud_surface(self) -> pygame.Surface:
        return self._hud_surface

    @hud_surface.setter
    def hud_surface(self, value) -> None:
        self._hud_surface: pygame.Surface = value

    # @property
    # def camera_offset(self) -> tuple[int, int]:
    #     return self._camera_offset

    # @camera_offset.setter
    # def camera_offset(self, value) -> None:
    #     self._camera_offset: tuple[int, int] = value

    def update_camera_offset(self, new_offset: tuple[int, int]):
        level_surface_size: tuple[int,
                                  int] = self.level_surface.holded_ref.get_size()
        camera_surface_size: tuple[int, int] = self.camera_surface.get_size()
        constrained_new_offset: tuple[int, int] = (constrain_int(
            new_offset[0], 0, level_surface_size[0] - camera_surface_size[0]),
            constrain_int(
            new_offset[1], 0, level_surface_size[1] - camera_surface_size[1]))
        self.camera_surface = self.level_surface.holded_ref.subsurface(
            constrained_new_offset, SCREEN_RESOLUTION)


# import pygame

# from constants import SCREEN_RESOLUTION
# from utils.MathUtil import constrain_int


# class Display:
#     """Singleton class that holds an instance of pygame.screen"""
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#             cls._instance.display = pygame.display.set_mode(
#                 SCREEN_RESOLUTION, pygame.SCALED | pygame.FULLSCREEN)
#             cls._instance.level_surface = pygame.Surface(SCREEN_RESOLUTION)
#             cls._instance.camera_surface = cls._instance.level_surface.subsurface(
#                 (0, 0), SCREEN_RESOLUTION)
#             cls._instance.camera_offset = (0, 0)

#         return cls._instance

#     @property
#     def display(self) -> pygame.Surface:
#         return self._display

#     @display.setter
#     def display(self, value) -> None:
#         self._display: pygame.Surface = value

#     @property
#     def level_surface(self) -> pygame.Surface:
#         return self._level_surface

#     @level_surface.setter
#     def level_surface(self, value) -> None:
#         self._level_surface: pygame.Surface = value

#     def set_level_surface_size(self, size: tuple[int, int]) -> None:
#         self.level_surface = pygame.Surface(size)

#     @property
#     def camera_surface(self) -> pygame.Surface:
#         return self._camera_surface

#     @camera_surface.setter
#     def camera_surface(self, value) -> None:
#         self._camera_surface: pygame.Surface = value

#     @property
#     def camera_offset(self) -> tuple[int, int]:
#         return self._camera_offset

#     @camera_offset.setter
#     def camera_offset(self, value) -> None:
#         level_surface_size: tuple[int, int] = self.level_surface.get_size()
#         camera_surface_size: tuple[int, int] = self.display.get_size()
#         self._camera_offset: tuple[int, int] = (constrain_int(
#             value[0], 0, level_surface_size[0] - camera_surface_size[0]),
#             constrain_int(
#             value[1], 0, level_surface_size[1] - camera_surface_size[1]))
