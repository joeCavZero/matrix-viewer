import pygame
from src.engine.widget.buttons.button import Button
from src.engine.scene.scene import Scene
from src.engine.engine import Engine
from src.engine.scene.views.triangle_matrix import TriangleMatrixScene
from src.engine.scene.views.triangle_matrix_menu import TriangleMatrixMenuScene
from src.engine.scene.views.credits import CreditsScene
class RedirectButton(Button):
    def __init__(self, position: tuple[float,float],text: str, type: str, engine: Engine):
        super().__init__(position,(100, 50), text, engine)
        self.type = type
    
    def update(self):
        self.update_color_on_hover()
        if self.is_hover() and pygame.mouse.get_just_released()[0]:
            match self.type:
                case "back":
                    self.engine.back_scene()
                case "to_triangle_matrix_menu":
                    self.engine.shift_scene(TriangleMatrixMenuScene(self.engine))
                case "to_triangle_matrix":
                    self.engine.shift_scene(TriangleMatrixScene(self.engine))
                case "to_credits":
                    self.engine.shift_scene(CreditsScene(self.engine))
        
    
    
        
