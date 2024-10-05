import pygame
import numpy as np
from src.engine.widget.widget import Widget
class MatrixViewer(Widget):
    from src.engine.engine import Engine
    def __init__( self, position: tuple[float,float], size: tuple[float,float], matrix, rows: int, cols: int, engine: Engine ):
        super().__init__(position, size, engine)
        self.rows = rows
        self.cols = cols
        self.matrix = matrix
        if self.matrix is None:
            self.matrix = np.array([0 for i in range(rows*cols)])
        
        self.font = self.engine.font_manager.get_font("arial-matrix-number")
        self.area = pygame.Surface( (self.size[0], self.size[1]) )
        self.border_color = (255,255,255)
        
        self.last_mouse_pos = (0,0)
        self.inter_pos = pygame.Vector2(0,0)
        self.zoom = 2
        self.moved = True
        
        self.setup_matrix()
    
    def update(self):
        
        if self.is_hover():
            self.border_color = (55,255,55)
            dragging = False
            for event in self.engine.events:
                if event.type == pygame.MOUSEWHEEL:
                    self.zoom += event.y/10
                    self.zoom = pygame.math.clamp(self.zoom, 0.09, 5)
                    self.moved = True
                if pygame.mouse.get_pressed()[0]:
                    dragging = True
                    self.moved = True
                    
                if dragging:
                    SENSIBILITY = 2
                    current_mouse_pos = pygame.mouse.get_pos()
                    
                    self.inter_pos.x += pygame.math.clamp(current_mouse_pos[0] - self._last_mouse_pos[0], -SENSIBILITY, SENSIBILITY)
                    self.inter_pos.y += pygame.math.clamp(current_mouse_pos[1] - self._last_mouse_pos[1], -SENSIBILITY, SENSIBILITY)
        else:
            self.border_color = (255,255,255)
        self._last_mouse_pos = pygame.mouse.get_pos()
        
    def render(self, canvas: pygame.Surface):
        if self.moved:
            self._render_area()
            self.moved = False

        canvas.blit(
            self.area,
            self.position,
        ) 
        self._render_border(canvas)
    
    def _render_border(self, canvas: pygame.Surface):
        BORDER_THICKNESS = 4
        data = [
            (self.position.x, self.position.y, self.size[0], BORDER_THICKNESS),
            (self.position.x, self.position.y, BORDER_THICKNESS, self.size[1]),
            (self.position.x, self.position.y+self.size[1]-BORDER_THICKNESS, self.size[0], BORDER_THICKNESS),
            (self.position.x+self.size[0]-BORDER_THICKNESS, self.position.y, BORDER_THICKNESS, self.size[1])
        ]
        for rect in data:
            pygame.draw.rect( canvas, self.border_color, rect )
    
    def setup_matrix(self):
        pass
    
    def _render_border(self, canvas: pygame.Surface):
        BORDER_THICKNESS = 4
        data = [
            (self.position.x, self.position.y, self.size[0], BORDER_THICKNESS),
            (self.position.x, self.position.y, BORDER_THICKNESS, self.size[1]),
            (self.position.x, self.position.y+self.size[1]-BORDER_THICKNESS, self.size[0], BORDER_THICKNESS),
            (self.position.x+self.size[0]-BORDER_THICKNESS, self.position.y, BORDER_THICKNESS, self.size[1])
        ]
        for rect in data:
            pygame.draw.rect( canvas, self.border_color, rect )
    def _render_area(self):
        font_size = self.font.get_height()*2
        self.area.fill( (0,0,0) )

        num_index = 0
        for num in self.matrix:
            text = None
            if num == 0:
                text = self.font.render(str(num), True, (255,255,255),bgcolor=(255,0,0))
            else:
                text = self.font.render(format(num,".1f"), True, (255,255,255))

            aux_x = num_index % self.cols
            aux_y = num_index // self.cols

            text = pygame.transform.scale(
                text,
                (text.get_width()*self.zoom, text.get_height()*self.zoom)
            )

            area_x = self.inter_pos.x + aux_x*font_size*self.zoom
            area_y = self.inter_pos.y + aux_y*font_size*self.zoom
            if (area_x < self.size[0] and area_x > -font_size*self.zoom) and (area_y < self.size[1] and area_y > -font_size*self.zoom):
                self.area.blit(
                    text,
                    (
                        area_x,
                        area_y
                    )
                )
            num_index += 1