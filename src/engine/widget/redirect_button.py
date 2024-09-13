import pygame
from engine.widget.button import Button
from engine.scene.scene import Scene
from engine.engine import Engine

class RedirectButton(Button):
    def __init__(self, x: float, y: float,text: str, engine: Engine):
        super().__init__(x, y,100, 50, text, engine)

    """def update(self):
        if self.is_hover(): #pygame.mouse.get_pressed()[0]:
            self.color = (0,255,0)
        else:
            self.color = (255,255,255)"""
    def render(self, canvas: pygame.Surface):
        
        pygame.draw.rect(
            canvas, 
            self.color, 
            pygame.Rect(
                self.position.x, self.position.y,
                self.size.x, self.size.y
            )
        )
        