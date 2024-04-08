from io import TextIOWrapper
import json
from Actor import Actor_TilemapCompatible
from typing import Optional, Type, TypeAlias, TypedDict

from Vector import Vector


class TilemapFileContentElementVector(TypedDict):
    x: int
    y: int


class TilemapFileContentElementTransform(TypedDict):
    size: Optional[TilemapFileContentElementVector]
    flip_x: Optional[bool]
    flip_y: Optional[bool]
    angle: Optional[int]


class TilemapFileContentElement(TypedDict):
    type: str
    z_index: int
    position: TilemapFileContentElementVector
    transform: Optional[TilemapFileContentElementTransform]


TilemapFileContent: TypeAlias = list[TilemapFileContentElement]

# TODO: could write some validation for the .json file passed in
# TODO: docs for this?


class Tilemap:
    def __init__(self, path_to_tilemap_file: str, tile_size: int, type_to_actor_dict: dict[str, Type[Actor_TilemapCompatible]]) -> None:
        self.actors: list[Actor_TilemapCompatible] = []

        try:
            file: TextIOWrapper = open(path_to_tilemap_file)
            file_content: TilemapFileContent = json.load(file)

            for tile in file_content:
                # Creating an actor based on the type of the tile
                actor_class: Type[Actor_TilemapCompatible] = type_to_actor_dict[tile["type"]]
                actor = actor_class(Vector(
                    tile['position']['x'] * tile_size, tile['position']['y'] * tile_size), tile['z_index'])
                # Editing the actor's transformation
                if 'transform' in tile and tile['transform'] is not None:
                    transform: TilemapFileContentElementTransform = tile['transform']
                    actor_size_vector: Vector = Vector(transform['size']['x'], transform['size']['x']) if 'size' in transform and transform['size'] is not None else Vector(
                        tile_size, tile_size)
                    actor.set_size(actor_size_vector)
                    flip_x: bool = transform['flip_x'] if 'flip_x' in transform and transform['flip_x'] is not None else False
                    flip_y: bool = transform['flip_y'] if 'flip_y' in transform and transform['flip_y'] else False
                    if flip_x or flip_y:
                        actor.flip(flip_x, flip_y)
                    if 'angle' in transform and transform['angle'] is not None:
                        actor.set_angle(transform['angle'])
                else:
                    actor.set_size(Vector(tile_size, tile_size))
                # Appending the actor to the list of created actors
                self.actors.append(actor)

            file.close()
        except FileNotFoundError as e:
            raise e
