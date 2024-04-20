from abc import ABC
from enum import Enum, auto
from typing import Any 
from Actor import Actor
from Animation import Animation
from RenderingController import RenderingController_WithAnimation
from Vector import Vector


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

    def __init__(self, position: Vector, z_index: int) -> None:
        self.state: CharacterState = CharacterState.IDLE
        self.isFacingRight: bool = True
        rendering_controller: RenderingController_WithAnimation = RenderingController_WithAnimation(
            self.__class__.idle_animation)
        super().__init__(position, rendering_controller, z_index)
        self.collision_component: CharacterCollisionComponent = CharacterCollisionComponent(
            self, Vector(self.idle_animation.frames[0].image.get_size()))
        self.movement_component: CharacterMovementComponent = CharacterMovementComponent(
            self, gravity_enabled=True)
        self.components.extend(
            [self.movement_component, self.collision_component])
        self.collision_component.add_event_subscription(CollisionComponentEvents.STAYING_ON_GROUND, self.onStayingOnGround)

    def set_animation(self, animation: Animation) -> None:
        if animation:
            self.rendering_controller.set_animation(
                animation)
            if (not self.isFacingRight):
                self.rendering_controller.flip(True, False)

    def jump(self) -> None:
        if self.state != CharacterState.JUMPING and self.state != CharacterState.FALLING:
            self.movement_component.jump()

    def onStayingOnGround(self, event_type: Any) -> None:
        if (self.state == CharacterState.JUMPING or self.state == CharacterState.FALLING):
            self.state = CharacterState.IDLE
            self.set_animation(
                self.__class__.idle_animation)

    def tick(self) -> None:
        super().tick()

        # Flipping
        if ((self.isFacingRight and self.movement_component.velocity.x < 0) or (not self.isFacingRight and self.movement_component.velocity.x > 0)):
            self.isFacingRight = not self.isFacingRight
            self.flip(True, False)

        # State managing

        # if (self.state == CharacterState.JUMPING or self.state == CharacterState.FALLING and self.movement_component.velocity.y == 0):
        #     self.state = CharacterState.IDLE
        #     self.set_animation(
        #         self.__class__.idle_animation)

        if (self.movement_component.velocity.y < 0):
            self.state = CharacterState.JUMPING
            self.set_animation(
                self.__class__.jumping_animation)
        elif (self.movement_component.velocity.y > 0):
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

from components.CharacterMovementComponent import CharacterMovementComponent
from components.CharacterCollisionComponent import CharacterCollisionComponent
from components.CollisionComponent import CollisionComponentEvents