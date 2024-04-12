from abc import ABC
from enum import Enum, auto
from typing import override
from Actor import Actor
from Animation import Animation
from RenderingController import RenderingController_WithAnimation
from Vector import Vector
from components.MovementComponent import MovementComponent


class CharacterState(Enum):
    IDLE = auto()
    RUNNING = auto()
    JUMPING = auto()
    FALLING = auto()


class Character(Actor[RenderingController_WithAnimation], ABC):
    idle_animation: Animation
    running_animation: Animation
    jumping_animation: Animation
    falling_animation: Animation

    def __init__(self, position: Vector[int], z_index: int, movement_speed: int = 100) -> None:
        self.state: CharacterState = CharacterState.IDLE
        self.isFacingRight: bool = True
        rendering_controller: RenderingController_WithAnimation = RenderingController_WithAnimation(
            self.__class__.idle_animation)
        super().__init__(position, rendering_controller, z_index)
        self.movement_component: MovementComponent = MovementComponent(self, movement_speed)
        self.components.append(self.movement_component)

    def set_animation(self, animation: Animation) -> None:
        if animation:
            self.rendering_controller.set_animation(
                animation)
            if (not self.isFacingRight):
                self.rendering_controller.flip(True, False)

    @override
    def tick(self) -> None:
        super().tick()

        # Flipping
        if ((self.isFacingRight and self.movement_component.velocity.x < 0) or (not self.isFacingRight and self.movement_component.velocity.x > 0)):
            self.isFacingRight = not self.isFacingRight
            self.flip(True, False)

        # State managing
        if (self.state == CharacterState.JUMPING or self.state == CharacterState.FALLING and self.movement_component.velocity.y == 0):
            self.state = CharacterState.IDLE
            self.set_animation(
                self.__class__.idle_animation)
            
        if (self.movement_component.velocity.y > 0):
            self.state = CharacterState.JUMPING
            self.set_animation(
                self.__class__.jumping_animation)
        elif (self.movement_component.velocity.y < 0):
            self.state = CharacterState.FALLING
            self.set_animation(
                self.__class__.falling_animation)
            
        elif (self.state == CharacterState.IDLE and self.movement_component.velocity.y == 0 and self.movement_component.velocity.x != 0):
            self.state = CharacterState.RUNNING
            self.set_animation(
                self.__class__.running_animation)
        elif (self.state == CharacterState.RUNNING and self.movement_component.velocity.x == 0):
            self.state = CharacterState.IDLE
            self.set_animation(
                self.__class__.idle_animation)
