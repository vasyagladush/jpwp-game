from Actor import ActorComponent
from Vector import Vector

class GravityComponent(ActorComponent):
    def __init__(self, owned_by, gravity: int = 1, max_fall_speed: int = 10):
        super().__init__(owned_by)
        self.gravity = gravity
        self.max_fall_speed = max_fall_speed
        self.velocity = Vector(0, 0)

    def tick(self) -> None:
        self.velocity.y = min(self.velocity.y + self.gravity, self.max_fall_speed)

        self.owned_by.position.set_coordinates(
            self.owned_by.position.x,
            self.owned_by.position.y + self.velocity.y
        )

        #Logic -> colission
