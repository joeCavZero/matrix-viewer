from src.engine.widget.buttons.button import Button
from src.engine.engine import Engine
from src.engine.scene.views.scaled_matrix import ScaledMatrixScene
import numpy as np
import pygame

class ConstructScaledMatrixButton(Button):
    def __init__(self, position: tuple[float,float], text: str, engine: Engine):
        super().__init__(position, (100, 50), text, engine)
    
    def update(self):
        self.update_color_on_hover()
        if self.is_hover() and pygame.mouse.get_just_released()[0]:
            from src.engine.scene.views.scaled_matrix_menu import ScaledMatrixMenuScene
            scene: ScaledMatrixMenuScene = self.engine.scene
            
            
            
            # ==========================
            aux_matrix = [
                [ scene.v1x1.get_value(), scene.v1x2.get_value(), scene.v1x3.get_value(), scene.v1x4.get_value() ],
                [ scene.v2x1.get_value(), scene.v2x2.get_value(), scene.v2x3.get_value(), scene.v2x4.get_value() ],
                [ scene.v3x1.get_value(), scene.v3x2.get_value(), scene.v3x3.get_value(), scene.v3x4.get_value() ]
            ]
            
            # RESOLVER LINHA 2
            v1x1 = aux_matrix[0][0]
            v2x1 = aux_matrix[1][0]
            
            delta = 0
            try:
                delta = v2x1 / v1x1
            except ZeroDivisionError:
                pass
            
            for i in range(4):
                aux_matrix[1][i] -= aux_matrix[0][i] * delta
            
            # RESOLVER LINHA 3 Parte 1
            v1x1 = aux_matrix[0][0]
            v3x1 = aux_matrix[2][0]
            
            delta = 0
            try:
                delta = v3x1 / v1x1
            except ZeroDivisionError:
                pass
            
            for i in range(4):
                aux_matrix[2][i] -= aux_matrix[0][i] * delta
                
            # RESOLVER LINHA 3 Parte 2
            
            v2x2 = aux_matrix[1][1]
            v3x2 = aux_matrix[2][1]
            
            delta = 0
            try:
                delta = v3x2 / v2x2
            except ZeroDivisionError:
                pass
            
            for i in range(4):
                aux_matrix[2][i] -= aux_matrix[1][i] * delta
            
            
            # ==========================
            matrix = np.zeros(12)
            
            for i in range(3):
                for j in range(4):
                    matrix[i*4 + j] = aux_matrix[i][j]
            
            self.engine.shift_scene(ScaledMatrixScene(matrix, self.engine))
            

def escalonada():
        matrix: list[list[float]] = [
            [],
            [],
            []
        ]
        
                
        
        # RESOLVER LINHA 2
        v1x1 = matrix[0][0]
        v2x1 = matrix[1][0]
        
        delta = v2x1 / v1x1
        
        for i in range(4):
            matrix[1][i] -= matrix[0][i] * delta
        
        # RESOLVER LINHA 3 Parte 1
        v1x1 = matrix[0][0]
        v3x1 = matrix[2][0]
        
        delta = v3x1 / v1x1
        
        for i in range(4):
            matrix[2][i] -= matrix[0][i] * delta
            
        # RESOLVER LINHA 3 Parte 2
        
        v2x2 = matrix[1][1]
        v3x2 = matrix[2][1]
        
        delta = v3x2 / v2x2
        
        for i in range(4):
            matrix[2][i] -= matrix[1][i] * delta
            
        #PRINTAR MATRIZ ESCALONADA
        for i in range( len(matrix) ):
            for j in range( len(matrix[i]) ):
                print(f"  {matrix[i][j]}  ", end=" ")
            print("\n", end="")