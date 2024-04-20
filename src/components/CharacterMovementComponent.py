from components.CollisionComponent import CollisionComponentEvents
from components.MovementComponent import MovementComponent


class CharacterMovementComponent(MovementComponent['Character']):
    def __init__(self, owned_by, movement_speed: int = 400, gravity_enabled: bool = False, gravity_acceleration: int = 1000, max_fall_speed: int = 1000, jump_start_speed: int = -700):
        super().__init__(owned_by, movement_speed, gravity_enabled,
                         gravity_acceleration, max_fall_speed)
        self.jump_start_speed = jump_start_speed

        self.owned_by.collision_component.add_event_subscription(
            CollisionComponentEvents.STAYING_ON_GROUND, self.nullify_velocity_y)

    def apply_gravity(self) -> None:
        if not self.owned_by.collision_component.isOnGround:
            super().apply_gravity()

    def nullify_velocity_y(self, event_type: CollisionComponentEvents) -> None:
        self.velocity.y = 0

    def jump(self) -> None:
        self.velocity.y = self.jump_start_speed

from Character import Character