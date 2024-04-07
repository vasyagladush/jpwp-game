import pygame


class Clock:
    """Singleton class that holds an instance of pygame.clock"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.clock = pygame.time.Clock()
        return cls._instance

    @property
    def clock(self) -> pygame.time.Clock:
        return self._clock

    @clock.setter
    def clock(self, value) -> None:
        self._clock: pygame.time.Clock = value

    def get_delta_time(self) -> int:
        """Get time in milliseconds passed between the last two frames

        Returns:
            ``int``: Time in milliseconds passed between the last two frames
        """
        return self.clock.get_time()

    # TODO: does it make sense?
    # def get_delta_frames(self) -> int:
    #     return round(self.get_delta_time() * FPS)
