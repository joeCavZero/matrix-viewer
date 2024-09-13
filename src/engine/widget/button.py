import pygame
from engine.widget.widget import Widget
from engine.engine import Engine

class Button(Widget):
    def __init__(self, x: float, y: float, width: float, height: float, text: str, engine):
        super().__init__(x, y, width, height, engine )
        self.text = text
        self.color = pygame.color.Color(200,200,200)
        
    def update(self):
        if self.is_hover():
            self.color = pygame.color.Color(255,255,255)
        else:
            self.color = pygame.color.Color(200,200,200)
    
        

