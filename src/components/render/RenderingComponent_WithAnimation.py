from Animation import Animation, AnimationController
from Display import Display
from Renderable import Renderable
from Vector import Vector


class RenderingComponent_WithAnimation(Renderable):
    def __init__(self, animation: Animation, rendering_order: int) -> None:
        super().__init__(rendering_order)
        self._animation_controller: AnimationController = AnimationController(
            animation)
        self._animation_controller.start()
    
    def set_animation(self, animation: Animation) -> None:
        self._animation_controller.animation = animation

    def render(self, position: Vector) -> None:
        self._animation_controller.update()
        if self._animation_controller.current:
            Display().display.blit(
                self._animation_controller.get_current_image(), position.coordinates_to_tuple())