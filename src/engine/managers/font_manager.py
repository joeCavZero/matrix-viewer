import pygame

class FontManager:
    def __init__(self):
        self._fonts = {}
    
    def load_sysfont(self, name: str, font: str, size: int):
        if name not in self._fonts:
            self._fonts[name] = pygame.font.SysFont(font, size)
    
    def get_font(self, name: str)-> pygame.Font:
        return self._fonts[name] if name in self._fonts else None