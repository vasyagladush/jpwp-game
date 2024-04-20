from Actor import Actor, Actor_TilemapCompatible
from Vector import Vector
from RenderingController import RenderingController_WithStaticImage
from constants import DEFAULT_TILE_SIZE
from utils.ImageUtil import ImageUtil
from components.CollisionComponent import CollisionComponent


class Block_TilemapCompatible(Actor_TilemapCompatible):
    image = ImageUtil.load_image('assets/block.png')

    def __init__(self,  position: Vector, z_index: int) -> None:
        rendering_controller = RenderingController_WithStaticImage(
            Block_TilemapCompatible.image)
        Actor.__init__(self, position, rendering_controller, z_index)
        self.collision_component = CollisionComponent(self, Vector(DEFAULT_TILE_SIZE, DEFAULT_TILE_SIZE))
        self.components.append(self.collision_component)

    def tick(self) -> None:
        super().tick()

