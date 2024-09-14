import pygame
from src.engine.widget.widget import Widget
from src.engine.engine import Engine

PADDING = 10


class Label(Widget):
    def __init__(self, position: tuple[float,float], text: str, engine: Engine):
        super().__init__(position, (0,0), engine )
        self.text = text

        
        font = self.engine.font_manager.get_font("arial-button")
        self._ren_text =  pygame.font.Font.render( font, self.text, True, (255,255,255) )

        self.size = pygame.math.Vector2(self._ren_text.get_width() + PADDING*2, self._ren_text.get_height() + PADDING*2)
        
    def render(self, canvas: pygame.Surface):

        canvas.blit(
            self._ren_text,
            (self.position.x+PADDING, self.position.y+PADDING)
        )
        
    
        

