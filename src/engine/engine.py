import pygame
import sys
from settings import *
from engine.managers.font_manager import FontManager


class Engine:
    
    def __init__(self):
        self._init_core()

        self.window = pygame.display.set_mode( CANVAS_SIZE, pygame.RESIZABLE )
        self.canvas = pygame.Surface( CANVAS_SIZE )
        pygame.display.set_caption( TITLE )
        self.clock = pygame.time.Clock()
        
        self.running = False
        self.scenes_list = []

        from engine.scene.scene import Scene
        self.scene: Scene = None
        self.canvas_scale = 1
        self.font_manager = FontManager()
        self.events: list[pygame.Event] = []

        #FUNNY
        self.ball = Ball( (CANVAS_WIDTH//2, CANVAS_HEIGHT//2) )
        self.paddle = Paddle( [CANVAS_WIDTH//2, CANVAS_HEIGHT-20], self.ball )
    
    def _init_core(self):
        pygame.init()
        pygame.font.init()

    def run(self):
        self.font_manager.load_sysfont( "arial-button", "Arial", 30 )
        self.font_manager.load_sysfont( "arial-title", "Arial", 80 )
        self.font_manager.load_sysfont( "arial-matrix-number", "Arial", 25 )
        
        self.running = True

        from engine.scene.views.menu import MenuScene
        self.shift_scene( MenuScene(self) )

        while self.running:
            self._handle_events()
            self._update()
            self._render()
            self.clock.tick( FPS )
        
        self._close()
    
    def _handle_events(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False

    def _update(self):
        self.ball.update()
        self.paddle.update()
        self.scene.update()
    
    def _render(self):
        self.window.fill( (0,0,0) )
        self.canvas.fill( (25,25,25) )
        
        self.ball.render( self.canvas )
        self.paddle.render( self.canvas )
        self.scene.render( self.canvas )
        self._render_border()
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

    def _render_border( self ):
        
        data = (
            (0,0, CANVAS_WIDTH, BORDER_THICKNES),
            (0,0, BORDER_THICKNES, CANVAS_HEIGHT),
            (0, CANVAS_HEIGHT-BORDER_THICKNES, CANVAS_WIDTH, BORDER_THICKNES),
            (CANVAS_WIDTH-BORDER_THICKNES, 0, BORDER_THICKNES, CANVAS_HEIGHT)
        )
        for rect in data:
            pygame.draw.rect( self.canvas, BORDER_COLOR, rect )
        
    def _close(self):
        pygame.quit()
        sys.exit()

    from engine.scene.scene import Scene
    def shift_scene(self, scene: Scene):
        self.scenes_list.append( scene )
        self.scene = self.scenes_list[-1]


    def back_scene(self):
        if len(self.scenes_list) > 1:
            self.scene = self.scenes_list[-2]
            self.scenes_list.pop(-1)

class Ball:
    def __init__(self, position ):
        self.position = position
        self.direction = (4,4)
        self.radius = 15

    def render(self, canvas):
        pygame.draw.circle( canvas, FUNNY_COLOR, self.position, self.radius )

    def update(self):
        self.position = (
            self.position[0] + self.direction[0],
            self.position[1] + self.direction[1]
        )

        if self.position[0] < self.radius+BORDER_THICKNES or self.position[0] > CANVAS_WIDTH - self.radius-BORDER_THICKNES:
            self.direction = ( -self.direction[0], self.direction[1] )
        if self.position[1] < self.radius+BORDER_THICKNES or self.position[1] > CANVAS_HEIGHT - self.radius -BORDER_THICKNES:
            self.direction = ( self.direction[0], -self.direction[1] )

class Paddle:
    def __init__(self, position, ball: Ball):
        self.position = position
        self.ball = ball
        self.size = (100, 20)
    
    def render(self, canvas):
        pygame.draw.rect( canvas, FUNNY_COLOR, (self.position, self.size) )

    def update(self):
        if self.ball.position[1] > CANVAS_HEIGHT//2:
            self.position[0] += (self.ball.position[0] - self.position[0]) / 10
        
