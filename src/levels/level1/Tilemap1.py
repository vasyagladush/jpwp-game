from Tilemap import Tilemap
from actors.environment.Block import Block_TilemapCompatible
from actors.environment.Tree import Tree_TilemapCompatible


class Tilemap1(Tilemap):
    def __init__(self) -> None:
        super().__init__('./src/levels/level1/tilemap.json', {'Ground': Block_TilemapCompatible, 'Tree': Tree_TilemapCompatible})
