import pygame
from engine.widget.widget import Widget

class Scene:
    #from engine.engine import Engine
    def __init__(self, engine ):
        self.engine = engine
        self.widgets: list[Widget] = []
    
    def update(self):
        for wid in self.widgets:
            wid.update()
    
    def render( self, canvas: pygame.Surface ):
        self.render_widgets(canvas)

    def render_widgets(self, canvas: pygame.Surface):
        for wid in self.widgets:
            wid.render(canvas)
            
    def add_widgets(self, *widgets: Widget):
        for wid in widgets:
            self.widgets.append(wid)
 