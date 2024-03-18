from Renderable import Renderable
from Vector import Vector


class Actor(Renderable):
    def __init__(self, position: Vector, rendering_order: int) -> None:
        super().__init__(rendering_order)
        self.position = position

    def tick(self) -> None:
        print("Actor tick")
