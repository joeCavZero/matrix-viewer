import pygame
from src.engine.widget.widget import Widget
from src.engine.engine import Engine

PADDING = 10


class Button(Widget):
    def __init__(self, position: tuple[float,float], size: tuple[float,float], text: str, engine: Engine):
        super().__init__(position, size, engine )
        self.text = text
        self.color = pygame.color.Color(0,0,0)

        
        font = self.engine.font_manager.get_font("arial-button")
        self._ren_text =  pygame.font.Font.render( font, self.text, True, (0,0,0) )

        self.size = pygame.math.Vector2(self._ren_text.get_width() + PADDING*2, self._ren_text.get_height() + PADDING*2)
        
        
    def update_color_on_hover(self):
        if self.is_hover():
            self.color = pygame.color.Color(0,255,0)
        else:
            self.color = pygame.color.Color(255,255,255)
            
    def update(self):
        pass
    def render(self, canvas: pygame.Surface):
        
        pygame.draw.rect(
            canvas, 
            self.color, 
            self.get_rect()
        )

        canvas.blit(
            self._ren_text,
            (self.position.x+PADDING, self.position.y+PADDING)
        )
        
    
        

