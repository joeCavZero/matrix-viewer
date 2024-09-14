import pygame
from engine.widget.buttons.button import Button
from engine.scene.scene import Scene
from engine.engine import Engine
from engine.scene.views.triangle_matrix import TriangleMatrixScene
from engine.scene.views.triangle_matrix_menu import TriangleMatrixMenuScene

class RedirectButton(Button):
    def __init__(self, position: tuple[float,float],text: str, type: str, engine: Engine):
        super().__init__(position,(100, 50), text, engine)
        self.type = type
    
    def update(self):
        self.update_color_on_hover()
        if self.is_hover() and pygame.mouse.get_just_released()[0]:
            if self.type == "back":
                self.engine.back_scene()
            elif self.type == "to_triangle_matrix_menu":
                self.engine.shift_scene(TriangleMatrixMenuScene(self.engine))
            elif self.type == "to_triangle_matrix":
                self.engine.shift_scene(TriangleMatrixScene(self.engine))
            
        
    
    
        
