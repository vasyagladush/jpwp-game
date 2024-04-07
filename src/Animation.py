from enum import Enum
from typing import Optional, Sequence
import pygame

from Clock import Clock


class AnimationFrame:
    def __init__(self, image: pygame.Surface, duration: int) -> None:
        self.image: pygame.Surface = image
        self.duration: int = duration


class AnimationPlayMode(Enum):
    ONCE = 0
    LOOP = 1
    STATIC_IMAGE = 2


class Animation:
    def __init__(self, frames: Sequence[AnimationFrame], playmode: AnimationPlayMode = AnimationPlayMode.LOOP) -> None:
        self.frames: Sequence[AnimationFrame] = frames
        self.playmode: AnimationPlayMode = playmode


class AnimationController:
    def __init__(self, animation: Animation, playspeed: float = 1.0) -> None:
        self._animation: Animation = animation
        self.playing: bool = True
        self.playspeed: float = playspeed
        self.current: pygame.Surface = self.animation.frames[0].image
        self.timeleft: float = self.animation.frames[0].duration
        self.frame_time: float = self.timeleft
        self.frame_num: int = 0
        self.next_frame: int = (self.frame_num + 1) % len(self.animation.frames)
        self.next: pygame.Surface = self.animation.frames[self.next_frame].image
        self.playtime: float = 0.0
        self.transition: float = 0.0

    @property
    def animation(self) -> Animation:
        return self._animation

    @animation.setter
    def animation(self, value: Animation) -> None:
        self._animation: Animation = value
        self.reset()

    def get_current_image(self) -> pygame.Surface:
        return self.current

    def reset(self) -> None:
        self.current = self.animation.frames[0].image
        self.timeleft = self.animation.frames[0].duration
        self.frame_time = self.timeleft
        self.next_frame = (self.frame_num + 1) % len(self.animation.frames)
        self.next = self.animation.frames[self.next_frame].image
        self.frame_num = 0
        self.playtime = 0.0
        self.transition = 0.0

    def start(self, playspeed=1.0) -> None:
        self.playspeed = playspeed
        self.reset()
        self.unpause()

    def pause(self) -> None:
        self.playing = False

    def unpause(self) -> None:
        self.playing = True

    def update(self) -> None:
        if self.animation.playmode == AnimationPlayMode.STATIC_IMAGE:
            return
        
        dt: float = Clock().get_delta_time() * self.playspeed
        if self.playing:
            self.playtime += dt
            self.timeleft -= dt
            self.transition = self.timeleft / self.frame_time

            while self.timeleft <= 0.0:
                self.frame_num = (
                    self.frame_num + 1) % len(self.animation.frames)
                if self.animation.playmode == AnimationPlayMode.ONCE and self.frame_num == 0:
                    self.pause()
                    return

                next_frame: int = (
                    self.frame_num + 1) % len(self.animation.frames)

                frame: pygame.Surface = self.animation.frames[self.frame_num].image
                time: int = self.animation.frames[self.frame_num].duration
                self.frame_time = time
                self.timeleft += time
                self.current = frame
                self.next = self.animation.frames[next_frame].image
                self.transition: float = self.timeleft / time

                if self.frame_num == 0:
                    self.playtime: float = self.timeleft
