from io import TextIOWrapper
import json
from Actor import Actor_TilemapCompatible
from typing import Type, TypeAlias, TypedDict

from Vector import Vector


class TilemapFileContentElementPosition(TypedDict):
    x: int
    y: int


class TilemapFileContentElement(TypedDict):
    type: str
    rendering_order: int
    position: TilemapFileContentElementPosition


TilemapFileContent: TypeAlias = list[TilemapFileContentElement]

# TODO: could write some validation for the .json file passed in


class Tilemap:
    def __init__(self, path_to_tilemap_file: str, tile_size: int, type_to_actor_dict: dict[str, Type[Actor_TilemapCompatible]]) -> None:
        self.actors: list[Actor_TilemapCompatible] = []

        try:
            file: TextIOWrapper = open(path_to_tilemap_file)
            file_content: TilemapFileContent = json.load(file)

            for tile in file_content:
                actor_class: Type[Actor_TilemapCompatible] = type_to_actor_dict[tile["type"]]
                actor = actor_class(Vector(tile['position']['x'] * tile_size, tile['position']['y'] * tile_size), tile['rendering_order'])
                actor.rendering_component.set_all_images_to_size(Vector(tile_size, tile_size))
                self.actors.append(actor)

            file.close()
        except FileNotFoundError as e:
            raise e
