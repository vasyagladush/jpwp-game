import os
from typing import Optional
import pygame


class ImageUtil:
    def __init__(self, base_path: str) -> None:
        self.base_path = base_path

    @staticmethod
    def load_image(path: str, convert_alpha: bool = False, colorkey: Optional[pygame.Color] = None) -> pygame.Surface:
        """A static method that loads an image and converts it immediately.

        Args:
            ``path (str)``: path to the image
            ``convert_alpha (bool, optional)``: Instead of pygame's ``convert()`` method, the ``convert_alpha()`` will be used on the image. Use for loading ``.png`` files with transparent background. Defaults to ``False``.
            ``colorkey (Optional[pygame.Color], optional)``: Pixels of this color will become transparent. Not required for ``.png`` files with transparent backgrounds, instead set ``convert_alpha`` to ``True``. Defaults to ``None``.

        Returns:
            ``pygame.Surface``: The loaded and converted image
        """
        image: pygame.Surface = pygame.image.load(path).convert_alpha() if convert_alpha else pygame.image.load(path).convert()
        if colorkey:
            image.set_colorkey(colorkey)
        return image
    
    @staticmethod
    def load_images_from_dir(path_to_dir: str, convert_alpha: bool = False, colorkey: Optional[pygame.Color] = None) -> list[pygame.Surface]:
        """A static method that loads images from directory and converts them immediately.

        Args:
            ``path_to_dir (str)``: path to the directory
            ``convert_alpha (bool, optional)``: Instead of pygame's ``convert()`` method, the ``convert_alpha()`` will be used on the image. Use for loading ``.png`` files with transparent background. Defaults to ``False``.
            ``colorkey (Optional[pygame.Color], optional)``: Pixels of this color will become transparent. Not required for ``.png`` files with transparent backgrounds, instead set ``convert_alpha`` to ``True``. Defaults to ``None``.

        Returns:
            ``list[pygame.Surface]``: The list of loaded and converted images
        """
        images: list[pygame.Surface] = []
        for path in os.listdir(path_to_dir):
            full_path_to_file = os.path.join(path_to_dir, path)
            # check if the current path is a file
            if os.path.isfile(full_path_to_file):
                images.append(ImageUtil.load_image(full_path_to_file, convert_alpha, colorkey))

        return images
    
    def load(self, path: str, convert_alpha: bool = False, colorkey: Optional[pygame.Color] = None) -> pygame.Surface:
        """A method that loads an image from a path relative to the ``base_path`` of the ``ImageUtil`` object.

        Args:
            ``path (str)``: path to the image
            ``convert_alpha (bool, optional)``: Instead of pygame's ``convert()`` method, the ``convert_alpha()`` will be used on the image. Use for loading ``.png`` files with transparent background. Defaults to ``False``.
            ``colorkey (Optional[pygame.Color], optional)``: Pixels of this color will become transparent. Not required for ``.png`` files with transparent backgrounds, instead set ``convert_alpha`` to ``True``. Defaults to ``None``.

        Returns:
            ``pygame.Surface``: The loaded and converted image
        """
        full_path: str = os.path.join(self.base_path, path)
        return ImageUtil.load_image(full_path, convert_alpha, colorkey)

    def load_from_dir(self, path_to_dir: str, convert_alpha: bool = False, colorkey: Optional[pygame.Color] = None) -> list[pygame.Surface]:
        """A method that loads images from a directory under a path relative to the ``base_path`` of the ``ImageUtil`` object.

        Args:
            ``path_to_dir (str)``: path to the directory
            ``convert_alpha (bool, optional)``: Instead of pygame's ``convert()`` method, the ``convert_alpha()`` will be used on the image. Use for loading ``.png`` files with transparent background. Defaults to ``False``.
            ``colorkey (Optional[pygame.Color], optional)``: Pixels of this color will become transparent. Not required for ``.png`` files with transparent backgrounds, instead set ``convert_alpha`` to ``True``. Defaults to ``None``.

        Returns:
            ``list[pygame.Surface]``: The list of loaded and converted images
        """
        full_path: str = os.path.join(self.base_path, path_to_dir)
        return ImageUtil.load_images_from_dir(full_path, convert_alpha, colorkey)
