import pygame
import pygame.math as math

from settings import *

class Widget:
    def __init__(self, size: tuple[float,float], width: float, height: float, engine ):
        self.position = math.Vector2(size[0],size[1])
        self.size = math.Vector2(width, height)
        from engine.engine import Engine
        self.engine: Engine = engine
    
    def update(self):
        pass
    def is_hover(self) -> bool:

        mouse_pos = pygame.mouse.get_pos()

        scale = self.engine.canvas_scale

        diff_x = self.engine.window.get_width() - (CANVAS_WIDTH * scale)
        diff_y = self.engine.window.get_height() - (CANVAS_HEIGHT * scale)

        return (
            diff_x//2 + self.position.x * scale < mouse_pos[0] < diff_x//2 + (self.position.x + self.size.x) * scale and
            diff_y//2 + self.position.y * scale < mouse_pos[1] < diff_y//2 + (self.position.y + self.size.y) * scale
        )

    def render(self, canvas: pygame.Surface):
        pass
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.position.x, self.position.y, self.size.x, self.size.y)
    
    def center(self) -> "Widget":
        self.position.x = self.engine.window.get_width()//2 - self.size.x//2
        return self 