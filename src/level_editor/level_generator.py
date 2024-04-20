import json
from typing import Any


def create_new_level_json(level_string, filename="new_level.json"):
    # Initialize an empty list to store 'x' coordinates
    x_coordinates: list[Any] = []

    # Split the level string into lines
    lines: list[str] = level_string.split('\n')

    # Iterate over each line and character
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            # Check if the character is 'x'
            if char == 'x':
                # Append the coordinates to the list
                x_coordinates.append({"type": "Ground", "position": {
                                     "x": char_index, "y": line_index}, "z_index": 0})
    
    # Write the list of 'x' coordinates to a JSON file
    with open(filename, "w") as file:
        json.dump(x_coordinates, file)


# Example usage:
level = """\
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x                              x
x                              x
x                              x
xxxxxxxxxxxx                   x
x            xxxxx  xxx  xxxxxxx
x                xxxx          x
x                              x
x                              x
x    xxxx                xxxx  x
x                              x
x         xxxxxxxxxxxxxxx      x
x                              x
x               xxx      xxxxxxx
x                              x
x                  xxxxx       x
x                              x
xxxxx     xxxxx                x
x                              x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"""

create_new_level_json(level)
