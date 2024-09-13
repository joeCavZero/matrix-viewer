import pygame
import pygame.math as math

from settings import *

class Widget:
    from engine.engine import Engine
    def __init__(self, x: float, y: float, width: float, height: float, engine: Engine ):
        self.position = math.Vector2(x, y)
        self.size = math.Vector2(width, height)
        self.engine = engine
    
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
