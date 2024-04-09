from Tilemap import Tilemap
from actors.environment.Block import Block_TilemapCompatible


class Tilemap1(Tilemap):
    def __init__(self) -> None:
        super().__init__('./src/levels/level1/tilemap.json', 128,
                         {'Ground': Block_TilemapCompatible})
