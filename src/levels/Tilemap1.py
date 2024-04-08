from typing import Type
from Actor import Actor_TilemapCompatible
from Tilemap import Tilemap
from actors.Block import Block_TilemapCompatible
from actors.actor1.Actor1_TilemapCompatible import Actor1_TilemapCompatible


class Tilemap1(Tilemap):
    def __init__(self) -> None:
        super().__init__('./src/levels/tilemap.json', 128,
                         {'Fox': Actor1_TilemapCompatible, 'Ground': Block_TilemapCompatible})
