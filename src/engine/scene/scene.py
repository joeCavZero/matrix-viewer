import pygame

class Scene:
    from engine.engine import Engine
    def __init__(self, engine: Engine):
        self.engine = engine
        self.widgets = []
    
    def update(self):
        for wid in self.widgets:
            wid.update()
    
    def render( self, canvas: pygame.Surface ):
        for wid in self.widgets:
            wid.render(canvas)