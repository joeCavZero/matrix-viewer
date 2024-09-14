from engine.scene.scene import Scene
import pygame

class TriangleMatrixScene( Scene ):
    def __init__(self,n: int, engine):
        super().__init__(engine)
        

        from engine.widget.buttons.redirect_button import RedirectButton
        self.add_widgets( 
            RedirectButton((20,20), "voltar", "back", self.engine),
            RedirectButton((0,100), "atumalaca", "to_triangle_matrix", self.engine) 
        )
        
    