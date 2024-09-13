import pygame
import sys
from settings import *


class Engine:
    
    def __init__(self):
        self._init_core()

        self.window = pygame.display.set_mode( CANVAS_SIZE, pygame.RESIZABLE )
        self.canvas = pygame.Surface( CANVAS_SIZE )
        pygame.display.set_caption( TITLE )
        self.clock = pygame.time.Clock()
        
        self.running = False
        self.scenes_list = []
        self.scene = None
        self.canvas_scale = 1
    
    def _init_core(self):
        pygame.init()
        
    def run(self):
        self.running = True

        from engine.scene.menu import MenuScene
        self.scene = MenuScene(self)

        while self.running:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick( FPS )
        
        self._close()
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def _update(self):
        self.scene.update()

    def _render(self):
        self.window.fill( (0,0,0) )
        self.canvas.fill( (25,25,25) )

        self.scene.render( self.canvas )
        self._render_canvas()
        pygame.display.flip()

    
    def _render_canvas( self ):
        win_width = self.window.get_width()
        win_height = self.window.get_height()

        delta_x = win_width / CANVAS_WIDTH
        delta_y = win_height / CANVAS_HEIGHT

        if delta_x < delta_y:
            self.canvas_scale = delta_x
        else:
            self.canvas_scale = delta_y

        diff_x = win_width - ( CANVAS_WIDTH * self.canvas_scale )
        diff_y = win_height - ( CANVAS_HEIGHT * self.canvas_scale )

        self.window.blit(
            pygame.transform.scale(
                self.canvas,
                ( 
                    CANVAS_WIDTH * self.canvas_scale, 
                    CANVAS_HEIGHT * self.canvas_scale 
                )
            ),
            ( diff_x//2 , diff_y//2)
        )

    def _close(self):
        pygame.quit()
        sys.exit()

