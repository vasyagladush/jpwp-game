from typing import Optional
import pygame


class ImageUtil:
    def __init__(self, base_path: str) -> None:
        self.base_path = base_path

    @staticmethod
    def load_image(path: str, colorkey: Optional[tuple[int, int, int]] = (0, 0, 0)) -> pygame.Surface:
        image = pygame.image.load(path).convert()
        image.set_colorkey(colorkey)
        return image
    
    def load(self, path: str, colorkey: Optional[tuple[int, int, int]] = (0, 0, 0)) -> pygame.Surface:
        full_path = self.base_path
        if not full_path.endswith('/'): 
            full_path += '/'
        full_path += path[1:] if path.startswith('/') else path 
        
        return ImageUtil.load_image(full_path, colorkey)
