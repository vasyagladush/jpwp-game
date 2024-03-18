from Vector import Vector


class Renderable:
    def __init__(self, rendering_order: int) -> None:
        self.rendering_order = rendering_order

    @staticmethod
    def get_rendering_order(el: 'Renderable') -> int:
        return el.rendering_order

    def render(self) -> None:
        print("Render tick")
