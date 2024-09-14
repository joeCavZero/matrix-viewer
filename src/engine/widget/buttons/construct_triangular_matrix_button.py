from engine.widget.buttons.button import Button
from engine.engine import Engine
from engine.scene.views.triangle_matrix import TriangleMatrixScene
import pygame

class ConstructTriangularMatrixButton(Button):
    def __init__(self, position: tuple[float,float], text: str, engine: Engine):
        super().__init__(position, (100, 50), text, engine)
    
    def update(self):
        self.update_color_on_hover()
        if self.is_hover() and pygame.mouse.get_just_released()[0]:

            n = self.engine.scene.n_input.get_value()

            self.engine.shift_scene(TriangleMatrixScene(n,self.engine))